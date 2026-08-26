# Diagram 34 — JSON Schema Validation

![A left-to-right flow on dark navy. INPUT DATA shows loose cards reading abc@, 123 and 2025-05-12. JSON SCHEMA shows a code panel with green braces. VALIDATE shows an archway with a magnifier and four checked rows — REQUIRED, TYPE, FORMAT, LIMITS. A teal arrow leads up to ACCEPTED, a white card with a green check. A coral arrow leads down to REJECTED, a white card with a red cross and a warning triangle, beside four coral chips reading REQUIRED MISSING, TYPE MISMATCH, FORMAT INVALID and LIMITS EXCEEDED. A dashed teal line runs from the rejected side back to the input.](../diagrams/34-json-schema-validation.png)

**Module:** Web foundations
**Role in the course:** the gate that stops bad data
**Layout:** three stages, then a two-way branch with a correction loop

---

## At a glance

Data arrives, a schema describes what it should look like, a gate checks it against four criteria, and it comes out either **ACCEPTED** or **REJECTED** — with the rejection telling you specifically which of the four failed.

This is the first diagram in the volume with a genuine gate in it, and the first with a coral branch. It is where the course stops describing how the web works and starts building things that refuse bad input.

---

## What the diagram teaches

### 1. A schema is a description, not code

Stage 2 shows a panel containing green braces and structured lines. It sits between the data and the check, and it does nothing on its own.

That positioning is the concept. A schema is a **written description of what valid data looks like** — a contract, expressed as data itself. The validator reads the schema and applies it. You do not write validation logic; you write a description, and something else enforces it.

The practical consequences follow from that separation:

- **One description, many uses.** The same schema validates incoming requests, documents the API, generates test data, and tells a client what to send.
- **It is inspectable.** Anyone can read what valid means without reading the validation code.
- **It cannot drift from itself.** Hand-written validation in three places drifts. One schema does not.

### 2. Four checks, and they are the four ways data goes wrong

Inside the archway, four rows each with a teal check icon:

**REQUIRED — is it there?** The field exists at all. This is the crudest check and the one that catches the most real problems, because missing data is far more common than malformed data.

**TYPE — is it the right kind of thing?** A string where a string belongs, a number where a number belongs. This is the previous diagram's lesson turned into an enforceable rule — `"28"` versus `28` stops being a subtle bug and becomes a rejection.

**FORMAT — is it well-formed for its kind?** A string can be the right type and still be nonsense as an email address, a date, or a postcode. The input panel's `abc@` and `2025-05-12` are exactly these cases: one is a broken email, one is a well-formed date.

**LIMITS — is it within bounds?** Length, range, count. An age of 4000 is a valid number and not a valid age. A comment of two million characters is a valid string and not something you should store.

The four are ordered from structural to semantic, and that ordering is useful: there is no point checking the format of a field that is not there, or the range of a value that is not a number.

### 3. Both outcomes are drawn, and rejection gets more detail than acceptance

**ACCEPTED** is a single white card with a green check and radiating lines. Clean, simple, done.

**REJECTED** is a white card with a red cross, a coral warning triangle, *and* four coral chips listing what went wrong: **REQUIRED MISSING**, **TYPE MISMATCH**, **FORMAT INVALID**, **LIMITS EXCEEDED**.

The asymmetry is deliberate and it is the most practically valuable thing in the diagram. **A rejection must say why.** Acceptance needs no explanation; refusal is useless without one.

The four chips map one-to-one onto the four checks. That correspondence means a caller receiving a rejection knows not only that they were refused but which criterion they failed and therefore what to change.

Contrast with the common alternative — a bare `400 Bad Request` with no body. Technically correct, and it leaves the caller guessing among four possibilities across every field they sent.

### 4. The dashed loop makes rejection recoverable

A dashed teal line runs from the rejected side, along the bottom of the frame, back to **INPUT DATA**.

Rejection is not a dead end. It is a **correction cycle**: the data was wrong, you were told precisely how, you fix it and resubmit.

That loop only functions if the rejection carried enough detail to act on, which is why the four chips and the loop belong to the same idea. A rejection that says "invalid" produces a caller who retries the same thing. A rejection that says "email: format invalid, expected an email address" produces a caller who fixes the email.

The loop being **teal** rather than coral is a subtle correct choice — the rejection is coral, but the recovery path is a result, and results are teal throughout this library.

### 5. Validation is a boundary, not a sprinkle

The gate is drawn as an **archway** — a structure that data passes through — rather than as a step in a list.

Everything upstream of it is untrusted. Everything downstream can assume the data is shaped correctly. That single guarantee simplifies every piece of code that runs after it, because none of them need to re-check.

The failure mode when this is done piecemeal is defensive code everywhere: every function checking whether the field exists, whether it is the right type, whether it is sane. The archway replaces all of that with one gate and a promise.

This is why validation appears again as a gate in the server request pipeline later in the volume — same idea, applied to a whole request rather than one payload.

### 6. This is where an agent's arguments get checked

Worth flagging early, because it is the reason this diagram sits in a course about building agent systems.

When a model proposes a tool call, the arguments it produces are **input data from an untrusted source**. They arrive as JSON. They may be well-formed and wrong, subtly mistyped, or out of range.

The gate in this diagram is the same gate that appears in the tool-call lifecycle as *client validates*, and the stop sign there is this diagram's coral branch:

![Five numbered stages — MODEL PROPOSES, CLIENT VALIDATES, SERVER AUTHORIZES, DOMAIN EXECUTES, RESULT + RECEIPT — with red octagonal STOP signs hanging beneath the two checking stages.](../diagrams/40-tool-call-lifecycle.png)

A learner who understands this picture already understands why a model's proposed arguments cannot be executed directly.

---

## Case study — Wren Logistics, the delivery window that was a year long

Wren runs same-day courier work in three cities. They built a booking API so that business customers could submit jobs programmatically rather than through the web form.

The API accepted a JSON booking. For the first two months it had no schema — the code read the fields it needed and assumed they were sensible.

### Four things that got through

**A pickup postcode as a number.** A customer's system sent `"postcode": 20144` for a numeric-format postcode. Wren's routing engine expected a string, received a number, and produced a route to a default depot location. One package went to the wrong city.

**A missing contact phone.** The field was optional in the customer's system and required in Wren's process. Bookings arrived without it. The driver reached the address, nobody was in, and there was no way to call. This happened around forty times before anyone connected the pattern to the API.

**An email address of `n/a`.** A well-formed string, entirely reasonable-looking, and not an email. Booking confirmations bounced silently. The customer believed their jobs had not been accepted and re-submitted them, producing duplicate collections.

**A delivery window of 8,760 hours.** A customer's integration had a units bug and sent the window in minutes where Wren expected hours. The booking was accepted with a delivery window of one year. It sat in the dispatch queue, technically valid, un-dispatched, for six days.

That last one is the case that made the schema a priority. The value was a valid number. It was a valid positive number. It was nonsense, and nothing in the system had an opinion about how large a delivery window can be.

### The schema they wrote

Four checks, mapping exactly onto the diagram's four rows.

**Required.** Pickup address, delivery address, contact name, contact phone, requested window. Five fields, no exceptions. The optional-in-their-system, required-in-ours mismatch became impossible.

**Type.** Postcode is a string. Window is a number. Contact phone is a string. Every field's type declared once, enforced everywhere.

**Format.** Email must match an email format. Postcodes must match the pattern for their declared country. Dates must be ISO 8601. `n/a` stopped being an email address.

**Limits.** Delivery window between 1 and 72 hours. Contact name between 2 and 100 characters. At most 20 items per booking. The one-year window became a rejection with a specific message.

### What rejection looks like now

The response to a bad booking is not `400 Bad Request`. It is a list, one entry per problem:

- *`contactPhone`: required field missing*
- *`deliveryWindowHours`: 8760 exceeds maximum of 72*
- *`contactEmail`: "n/a" is not a valid email address*

Three fields, three specific failures, each naming the criterion and the expected condition. A developer receiving that fixes their integration in minutes rather than emailing support.

### The measured effect

- **Support tickets about bookings** fell by about two thirds in the first month.
- **Bookings requiring manual intervention** went from roughly 6% to under 1%.
- **The units bug was found by the customer, not by Wren.** Their integration started receiving a clear rejection naming the maximum, and they diagnosed the minutes/hours confusion themselves within an hour of deploying against the new API.

That last one is the argument for detailed rejections. Wren did not debug their customer's bug. The rejection message did.

### The one they debated

Should a booking with one bad field be rejected entirely, or accepted with that field dropped?

They chose reject-the-whole-thing, and their reasoning was the postcode case: a booking with a silently-dropped field is a booking that looks fine and does the wrong thing. A rejected booking is visibly a problem. **Loud failure beats quiet wrongness**, particularly when a physical vehicle is going to be dispatched somewhere.

---

## Composition

A left-to-right flow across the frame with a branch at the third stage.

**INPUT DATA → JSON SCHEMA → VALIDATE**, then a **teal arrow up to ACCEPTED** and a **coral arrow down to REJECTED**. A dashed teal line runs from beneath the rejected stage, leftward along the base of the frame, and turns up into **INPUT DATA**.

## Element by element

**INPUT DATA**
Four loose cards on a blue platform, deliberately unstructured: a green card with `{ }` braces, a white card reading **123**, a blue card reading **abc@**, and a white card reading **2025-05-12**. Raw values, some of which are about to fail.

**JSON SCHEMA**
A dark application window on a blue platform, containing large **green braces** wrapping structured rows of blue and teal lines. A description, not executable logic.

**VALIDATE**
A blue **archway** structure with a **teal magnifying glass** mounted at its top. Inside the arch, four dark rows each with a teal icon: a check and **REQUIRED**, a **T** and **TYPE**, an **@** and **FORMAT**, a bar chart and **LIMITS**.

**ACCEPTED**
A white card carrying a large **green check disc** and text lines, with radiating cyan accent marks, on a blue platform.

**REJECTED**
A white card carrying a large **red ✗ disc** and text lines, with a **coral warning triangle** at its lower right. To the right, four **coral chips** each with a white exclamation icon: **REQUIRED MISSING**, **TYPE MISMATCH**, **FORMAT INVALID**, **LIMITS EXCEEDED**, connected by short dashed coral leaders.

**The correction loop**
A dashed teal line from the rejected stage, running the full width of the frame's base, turning upward into the input data platform.

## Colour and flow semantics

- **Cyan arrows** carry data through the first three stages.
- The branch splits into **teal for accepted** and **coral for rejected** — the library's standard grammar for success and refusal.
- The **four coral chips** correspond one-to-one with the four checks inside the arch, so failure names its cause.
- The **return loop is teal, not coral**, because recovery is a result rather than a failure.
- The **archway form** marks validation as a boundary data passes through rather than a step in a list.

## How to present it

**Point at the loose input cards first.** `abc@`, `123`, `2025-05-12`. Ask which of these are valid. The answer — it depends entirely on what they are supposed to be — is the reason schemas exist.

**Ask what a schema is.** Push past "validation code." It is a *description* of valid data, written as data. Then ask what you get from that separation: one source of truth, usable for validation, documentation, test data and client guidance.

**Walk the four checks and ask for an example of each.** Required is easy. Type connects straight back to the previous diagram's string-versus-number lesson. Format is the one people forget — a string can be the right type and still be nonsense. Limits is the one almost nobody implements, and Wren's one-year delivery window is the story to tell.

**Ask why the rejection side has four chips and the acceptance side has none.** The answer — a refusal is useless without a reason — is the most immediately actionable idea here. Then ask what their own API returns on a bad request. If the answer is `400` with no body, that is the finding.

**Trace the dashed loop and ask what makes it work.** Only a detailed rejection produces a corrected resubmission. A vague one produces the same request again. The loop and the chips are one idea.

**Run the reject-or-drop debate.** One bad field in a ten-field payload: refuse everything, or accept and drop it? Let the room argue, then give them Wren's reasoning — a silently dropped field produces a booking that looks fine and dispatches a van to the wrong place. Loud failure beats quiet wrongness.

**Connect it forward.** Say plainly that this gate is where a model's proposed tool arguments get checked later in the course. Untrusted input arriving as JSON is exactly the situation this diagram describes, whether it came from a customer's integration or from a language model.

**Timing.** Twenty-five minutes. Thirty-five if you have the room write the four checks for a payload of their own, which is where the limits check usually gets discovered.

---

## Lab and checkpoint

**Lab:** Take one real payload from an API you consume or provide. Write a JSON schema for it with four checks: required fields, correct types, format rules, and value limits. Then generate three invalid payloads, one per check, and write the rejection message each should produce. Run the schema validator and confirm the message is specific enough to correct the payload.

**Checkpoint:** Why is a detailed rejection better than a vague `400`?

**Answer:** Because a vague `400` gives the caller no information about which field is wrong or why. A detailed rejection with field-level reasons lets the caller fix the data and resubmit. Without detail, the same broken payload is likely to be sent again.

## Glossary

- **Format** — a pattern a string must match, such as a date or email format.
- **JSON Schema** — a declarative description of what a JSON value is allowed to contain.
- **Limit** — a bound on a value, such as a minimum, maximum, length, or range.
- **Loud failure** — a refusal that names the problem rather than silently dropping or accepting bad data.
- **Recovery loop** — the path back to the client with a detailed rejection so they can correct and resubmit.
- **Required** — the rule that certain keys must be present.
- **Schema** — a data description used to validate, document, and test other data.
- **Type check** — the rule that a value must be a string, number, Boolean, array, object, or null.
- **Validation** — the process of checking that input matches the schema.

## Sources

- JSON Schema specification
- RFC 8259 JSON data format
- API validation and error-message design
