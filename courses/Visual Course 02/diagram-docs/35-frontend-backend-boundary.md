# Diagram 35 — Frontend / Backend Boundary

![Five numbered stages on dark navy, split by a glowing vertical line. Left of the line, stage 1 REACT UI shows a browser window. Right of the line, stage 2 API ROUTE shows a doorway with a code glyph, stage 3 DOMAIN SERVICE shows interlocking gears, stage 4 DATA STORE shows a database stack, stage 5 RECEIPT shows a printed slip with a green check. FRONTEND is labelled below the left section and BACKEND below the right. A dashed teal line returns from the receipt to the UI.](../diagrams/35-frontend-backend-boundary.png)

**Module:** Building the system
**Role in the course:** where your code runs and who can see it
**Layout:** five stages divided by a vertical trust boundary, with a return path

---

## At a glance

Five stages, and a **glowing vertical line** between the first and the second. One stage on the left labelled **FRONTEND**. Four on the right labelled **BACKEND**.

That line is the most important object in the diagram. It is not a network diagram or a deployment boundary — it is a **trust boundary**. Everything on the left runs on a machine you do not control, in front of a person who can read all of it. Everything on the right runs on a machine you do.

Almost every serious beginner security mistake is a thing that belonged on the right and was put on the left.

---

## What the diagram teaches

### 1. The line means "who can see this"

Code in the browser is delivered to the user. They can read it, pause it, modify it, and call anything it calls, with any values they like. Not because they are an attacker — because that is what a browser is. Developer tools ship with every browser on earth.

That produces a single rule with no exceptions:

**Anything on the left is public. Anything on the left can be changed by the user.**

Which in turn means three categories of thing can never live in the frontend:

- **Secrets.** API keys, database credentials, signing keys, service tokens. Anything shipped to a browser is published.
- **Trust decisions.** Whether this user may perform this action. A check in the UI is a convenience, not a control.
- **Business truth.** What something costs, what a discount is worth, whether a limit has been reached. If the browser decides it, the user decides it.

### 2. Stage 1 is the only frontend stage, and that proportion is the point

One stage left of the line, four right of it.

Beginners building their first application often have the opposite proportion — most of the logic in the browser, with the server as a thin store. The diagram is arguing for the reverse: **the UI presents and collects; everything else happens where you control it.**

The React UI panel shows a window with a sidebar, a teal content block and white cards. Layout and input. No gears, no database, no shield. Its job is to show things to a person and gather what they type.

### 3. The API route is a door, and the metaphor is exact

Stage 2 is drawn as a **doorway** — a frame with a door in it, carrying a `</>` glyph.

A door is the only way in, it is in a wall, and something decides whether you may pass. That is precisely an API route's job: it is the single entrance to the backend, and it is where every request from the outside arrives.

Two consequences beginners routinely miss:

**It is the first thing that runs on your side.** Whatever the UI intended, whatever the UI validated, the route receives an arbitrary HTTP request that may have come from your UI, from a script, from a curl command, or from someone with your API open in a tab.

**It is where checking belongs.** The route is inside your trust boundary and outside your business logic, which makes it the right place for the request pipeline in the next diagram — routing, validating, authenticating, authorising:

![Six numbered gates — ROUTE, VALIDATE, AUTHENTICATE, AUTHORIZE, EXECUTE, RESPOND — with coral arrows dropping from three of them into red STOP tiles.](../diagrams/36-server-request-pipeline.png)

That entire pipeline happens inside this doorway.

### 4. Domain service is separated from data store, and that separation is a real design claim

Stages 3 and 4 could have been one box labelled "the server." They are two, and the split matters.

**DOMAIN SERVICE** — interlocking gears. This is where your rules live. What a valid order looks like, how a discount is calculated, whether this action is permitted given the state of things, what happens when it succeeds. The gears convey mechanism and interconnection.

**DATA STORE** — a database stack. This is where facts are kept. It stores; it does not decide.

Keeping them separate means your rules exist in one readable place rather than being distributed across queries, triggers and UI code. It also means you can change where data lives without rewriting what your business does, which is the practical payoff.

### 5. The receipt is a stage, not a side effect

Stage 5 shows a **printed slip with a green check** — its own numbered platform, at the end of the backend.

Making the record of what happened a first-class stage is a thread running through both volumes. Something changed; there is now durable evidence of it; that evidence is part of the work rather than an afterthought.

For a beginner course this is the moment where "save it to the database" becomes "record what happened, in a form someone can read later." The two are not the same, and the difference is what makes a system explicable when someone asks why.

### 6. The dashed return crosses the boundary, and only the result crosses

A dashed teal line runs from the receipt, along the base of the frame, back to the React UI — crossing the vertical boundary from right to left.

What crosses back is **the outcome**, not the internals. The UI learns that the thing succeeded and what the result was. It does not learn the database schema, the credentials, or how the decision was made.

That is the correct shape of an API response, and it is worth pointing at: the boundary is crossed by data in both directions, and by nothing else.

---

## Case study — Thistle Tickets, the key in the bundle

Thistle sells tickets for independent music venues. Their booking site was built by a founder teaching themselves React — competent, motivated, and working alone.

The site worked. It took payments, issued tickets, and ran for five months before a customer emailed to say they had found something.

### What the customer found

Thistle's frontend called a third-party email service directly to send ticket confirmations. Calling it required an API key. The key was in the React code.

The customer — a developer buying tickets for a gig — had opened developer tools out of curiosity, looked at the network requests, and found the key in plain text in the JavaScript bundle.

They emailed rather than doing anything with it. Thistle was extremely lucky in who found it.

### What the key allowed

The email service key was not scoped. It permitted:

- Sending email from Thistle's verified domain, to anyone, with any content.
- Reading the full contact list — about 14,000 customer email addresses.
- Reading delivery logs, including who had bought what.

A phishing campaign from a genuinely verified thistletickets.com sender, to 14,000 people who had bought tickets from them, would have been extremely effective.

### Why it happened

The founder's reasoning was entirely logical and entirely wrong: *the key is needed to send the email, the email is sent when the booking completes, the booking completes in the browser, therefore the key goes in the browser.*

Every step follows from the previous one. The error is at the start — the email should never have been sent from the browser.

### The other two things the audit found

Once they knew to look at the boundary, two more problems surfaced immediately.

**Price was calculated in the frontend.** The UI computed the total from ticket price, quantity and any discount code, then posted the total to the payment step. A user could change the posted total to anything. Nobody had, as far as the logs showed, but the possibility had been live for five months.

**The admin panel was hidden, not protected.** The link was not rendered for non-admin users, and the admin routes checked a flag held in the browser. Changing that flag in developer tools revealed the admin interface, and the backend routes it called did not re-check. The frontend was the only thing standing between a customer and the refund function.

That third one is the clearest illustration of the diagram's rule. The check existed. It was on the wrong side of the line, which meant it was a suggestion.

### The rebuild

**The email key moved to the backend.** The browser now posts a completed booking to an API route. The route sends the confirmation. The key exists only on the server, in an environment variable, and was rotated immediately.

**Price moved to the domain service.** The browser posts *what was chosen* — ticket type, quantity, discount code — and the backend computes what it costs. The UI still displays a total, because users need to see one, but that displayed number is now a preview rather than an instruction. The backend never trusts it.

This is the general form of the fix and worth stating as a rule: **the frontend sends intent; the backend determines consequence.**

**Authorisation moved behind the door.** Every admin route now checks the user's role server-side. Hiding the link remains — it is good UX — but it is no longer the control. The founder's note: *hiding is not protecting.*

### What it cost

Two weeks of rework, a key rotation, and a disclosure to their payment provider. No breach, no fraudulent charges, no misuse of the contact list — entirely because of who happened to find it.

The founder's summary is the reason this diagram sits where it does in the course: *I understood React and I understood the server. I had never thought about the line between them as meaning anything.*

---

## Composition

Five stages run left to right, each on a blue platform with a numbered blue disc and a white uppercase label above it. Cyan arrows connect the stages.

A **glowing vertical cyan line** runs from top to bottom of the frame between stages 1 and 2. Below the line's left section, the word **FRONTEND**; below its right section, **BACKEND**.

A **dashed teal line** runs from beneath stage 5, along the base of the frame, crosses the boundary, and turns upward into stage 1.

## Element by element

**1 REACT UI** *(frontend)*
A 3D browser window with a blue title bar, a dark sidebar with a teal avatar dot and text lines, a large teal content block, and four white cards. Presentation and input only — no logic iconography.

**The boundary**
A single vertical glowing cyan line, running the full height of the frame, unbroken except where the dashed return path crosses it.

**2 API ROUTE** *(backend)*
A white doorway frame containing a dark door with a teal `</>` glyph and a small handle. The single entrance.

**3 DOMAIN SERVICE**
Three interlocking gears — one large teal, one medium blue, one small white — conveying mechanism and interconnection. Where the rules live.

**4 DATA STORE**
A stacked blue database cylinder with teal indicator lights. Facts, kept.

**5 RECEIPT**
A white printed slip with a curled top edge, text lines, and a **teal check badge** at its lower right.

**The return path**
A dashed teal line crossing from the backend to the frontend, carrying the outcome and nothing else.

## Colour and flow semantics

- **Cyan arrows** carry the request rightward through the stages.
- The **glowing vertical line** is the only boundary of its kind in the volume, and it separates trust rather than infrastructure.
- **Teal** marks the gears, the door glyph and the receipt check — the working parts on the trusted side.
- The **dashed teal return** is the only element that crosses the boundary in the reverse direction.
- No coral appears — this diagram describes structure rather than failure, and the failures it prevents happen off-picture.

## How to present it

**Point at the line and ask what it separates.** Not client and server, not React and Node — **what the user can see and change** versus what they cannot. Everything else follows from that reading.

**Ask what happens to a secret placed on the left.** It is published. Say it plainly: shipping a key to a browser is publishing it, whether or not anyone reads it. Then tell the Thistle story and ask who found the key. A curious customer, and that was luck.

**Run the three-category drill.** Secrets, trust decisions, business truth. For each, ask the room where it lives in something they have built. In a beginner room, at least one person will realise something is on the wrong side while you are talking.

**Ask about price specifically.** "Where is the total calculated?" It is the most common instance of business truth in the frontend, and the fix generalises: the frontend sends intent, the backend determines consequence. That sentence is the most portable thing in this document.

**Ask whether hiding is protecting.** Thistle's admin panel is the clean version — the check existed, on the wrong side of the line, so it was a suggestion. Then ask what their own UI hides that the backend does not re-check.

**Ask why the door is a door.** Single entrance, in a wall, with something deciding whether you pass. Then note that the request pipeline in the next diagram is what happens *inside* that doorway — this makes the two diagrams a zoom rather than two topics.

**Ask why domain service and data store are separate stages.** Rules versus facts. A store that decides is a store you cannot reason about, and rules spread across queries and triggers are rules nobody can read.

**Trace the return and ask what crosses back.** The outcome, not the internals. That is the correct shape of an API response, and stating it prevents the common beginner habit of returning whole database rows.

**Timing.** Twenty-five minutes. Thirty-five if you run the three-category drill against the room's own projects, which is where the real findings surface.

---

## Lab and checkpoint

**Lab:** Take one feature from a project you have built. Classify every piece of data and logic it uses into three categories: secrets, trust decisions, and business truth. For each one, write whether it currently lives on the frontend or backend side of the boundary. If anything in the first two categories is on the frontend, write the attack or failure that would result and the smallest move that would place it on the backend.

**Checkpoint:** Why is the frontend sending intent and the backend determining consequence?

**Answer:** Because the user can see and change anything in the frontend. If the frontend calculates business truth, the user can change the calculation. The backend must determine consequence from a trusted position, using facts the user cannot alter.

## Glossary

- **Backend** — the server side of the boundary, where secrets, trust decisions, and business truth live.
- **Boundary** — the line that separates what the user can see and change from what they cannot.
- **Business truth** — the logic and rules that determine consequences, such as pricing or totals.
- **Door** — the single gateway through which all requests pass to be evaluated.
- **Domain service** — the server code that applies business rules before data changes.
- **Frontend** — the client side of the boundary, which the user can inspect and modify.
- **Secret** — a credential or key that must never reach the browser.
- **Trust decision** — a check that must be made on the trusted backend, not on the client.

## Sources

- Frontend/backend trust boundary patterns
- OWASP insecure direct object reference and mass assignment
- API response design and the principle of least exposure
