# Diagram 33 — JSON Object Anatomy

![A radial layout on dark navy. At centre, a white JSON OBJECT card showing name: "Ada Lovelace", age: 28, isScientist: true, skills: ["math","logic","coding"], address: { … }. Five satellites connect to it — KEY with a teal key icon, VALUE with a blue gift icon, ARRAY showing three blocks reading "math" "logic" "coding", NESTED OBJECT showing purple blocks and a card with city, zip and country, and DATA TYPES showing four tiles labelled STRING, NUMBER, BOOLEAN and NULL.](../diagrams/33-json-object-anatomy.png)

**Module:** Web foundations
**Role in the course:** reading and writing the data format everything uses
**Layout:** central example with five labelled satellites

---

## At a glance

One real JSON object at the centre, with its five structural concepts arranged around it: **KEY, VALUE, ARRAY, NESTED OBJECT, DATA TYPES**.

The teaching method here is worth noticing. The diagram does not explain JSON abstractly and then show an example. It puts a **correct, complete, readable example** at the centre and points at its parts. Everything a learner needs to know is visible in five lines of actual data.

---

## What the diagram teaches

### 1. The centre object is a complete specimen

The card in the middle contains five pairs, and between them they demonstrate every concept in the diagram:

```
{
  "name":        "Ada Lovelace",
  "age":         28,
  "isScientist": true,
  "skills":      ["math", "logic", "coding"],
  "address":     { … }
}
```

A string. A number. A boolean. An array. A nested object. Five lines, five different value types, no filler.

Note also what the colour coding is doing inside the card. Keys alternate teal and coral, values are blue, the array is a single blue block, and the nested object is purple. A learner scanning the card sees the key/value split before reading a word.

### 2. Keys are strings; values can be anything

The two upper satellites make the asymmetry explicit.

**KEY** — a teal key icon with the note that a key is *a string that identifies a value*. Keys are always strings. Always quoted. This is a rule with no exceptions and it is worth stating flatly, because it is the first thing people get wrong when hand-writing JSON.

**VALUE** — a gift box, with the note that a value *can be a string, number, Boolean, null, array, or another object*. Six possibilities.

That asymmetry is the structural heart of the format. The left side of every pair is one fixed thing. The right side is open, and because one of its options is "another object," the format can describe arbitrarily deep structures with only two rules.

### 3. The four data types are shown as literal values

The **DATA TYPES** platform carries four tiles showing the actual notation rather than the type name alone:

- **`" "`** labelled STRING
- **`123`** labelled NUMBER
- **`true`** labelled BOOLEAN
- **`null`** labelled NULL

Showing the literal form is what makes this useful. The distinctions that cause real bugs are all visible here:

- `"28"` is a string. `28` is a number. They are different values and a strict consumer will reject one where it expects the other.
- `"true"` is a string. `true` is a boolean.
- `null` is a value meaning *known to be absent*. It is not the same as a key being missing, and it is not the same as an empty string.

That last distinction is the one that bites hardest in practice, and the diagram gives it its own tile rather than folding it in.

### 4. An array is ordered, and the diagram says so

The **ARRAY** satellite shows three blocks reading `"math"`, `"logic"`, `"coding"` in a row, with the note *an ordered list of values*.

Two properties in that one word. Arrays have an **order**, which is meaningful and preserved. And they are drawn as a row of separate blocks, which conveys that each element is its own value — and, by implication, that elements can themselves be objects or arrays.

Contrast with the object at the centre, whose pairs are stacked vertically and whose order carries no meaning. Arrays are positional; objects are named. That is the whole difference.

### 5. The nested object is where the format gets its power

The **NESTED OBJECT** satellite shows purple blocks and a card containing:

```
{ "city": "London", "zip": "SW1A 1AA", "country": "UK" }
```

with the note *an object inside another object*.

Look back at the centre card and you can see where this fits: the `address` key's value is shown as `{ … }` — a placeholder that the satellite expands.

This is the recursion that makes JSON able to describe anything. An object contains values; a value can be an object; therefore structure can nest without limit. Two rules, unlimited depth.

Note that `"zip": "SW1A 1AA"` is a **string**, not a number, despite being called a code. Postcodes, phone numbers, account numbers and ISBNs are all strings — anything with leading zeros, spaces, letters, or no arithmetic meaning. Getting this wrong is one of the most common data-modelling mistakes beginners make.

### 6. Why this earns a whole diagram

JSON is the format that carries everything else in both volumes. It is the request body and the response body in the previous diagram. It is what a schema validates in the next one. It is what a tool call is made of, what an agent's arguments arrive in, what an artifact is returned as, and what a receipt is written in.

A learner who is fluent in these five concepts can read every payload in the rest of the course. One who is not will guess at every one of them.

The immediate next use is the gate that checks whether a payload is acceptable:

![A left-to-right flow — INPUT DATA, JSON SCHEMA, VALIDATE with REQUIRED, TYPE, FORMAT and LIMITS rows — branching to a teal ACCEPTED card and a coral REJECTED card with four failure chips.](../diagrams/34-json-schema-validation.png)

Every one of that diagram's four checks is a question about the concepts on this one.

---

## Case study — Cobalt Fitness, the membership ID that lost its zero

Cobalt runs eleven gyms. They were replacing a spreadsheet-and-email process for member sign-up with a proper web form that posted to their membership system.

The integration worked in testing. It broke in production, for a specific and initially baffling subset of members: everyone whose membership ID began with a zero.

### The symptom

Member `0044821` was created in the system as `44821`.

The member could not check in — the barcode on their card did not match the record. Staff would search for `0044821`, find nothing, and create a duplicate account. Over three weeks this produced about ninety duplicate records and a number of members who had paid and could not get through the door.

### The cause, in one line of JSON

The form was sending:

```
{ "memberId": 0044821 }
```

Unquoted. A number.

JSON numbers do not have leading zeros — there is no way to represent one, because numerically `0044821` and `44821` are the same value. The parser did the only thing it could and produced `44821`.

The correct representation was:

```
{ "memberId": "0044821" }
```

A string. Quoted. Preserved exactly.

### Why testing missed it

Their test data was generated sequentially starting from 1000, so no test member had a leading zero. The bug was invisible until it met real data.

This is worth dwelling on, because it is the general shape of type bugs: they do not fail everywhere, they fail on the *subset of values where the type distinction matters*. Sequential test IDs never exercise it. Neither would a test suite of a hundred random numbers.

### The three other type problems they found

Once they started checking types deliberately, they found three more in the same payload.

**Phone numbers as numbers.** `"phone": 7911123456` — which silently dropped the leading zero of `07911123456` and, for one international member, mangled a `+` prefix entirely. Phone numbers are strings.

**Postcodes as numbers where they were purely numeric.** Their system had members in several countries. Numeric postcodes parsed as numbers; alphanumeric ones as strings. The same field carried two different types depending on the value, which broke the membership system's indexing. Postcodes are strings.

**Empty versus missing versus null.** Their form sent `"middleName": ""` when the field was blank. Their membership system treated empty string as a *provided* value and stored it, which meant the printed cards read "Ada  Lovelace" with a double space. What they meant was `null` — known to be absent — or omitting the key entirely.

They settled on a rule: **omit the key if the question was not asked; use `null` if it was asked and the answer is nothing; use `""` only if an empty string is genuinely the answer.** In practice that third case almost never occurs.

### The rule they wrote down

*If you will never do arithmetic on it, it is a string.*

Member IDs, phone numbers, postcodes, account numbers, invoice references, ISBNs, order numbers. None of these are ever added, subtracted, or averaged. All of them can have leading zeros, spaces, or letters. All of them are strings.

Ages, quantities, prices and counts are numbers, because you do arithmetic on them.

### What it cost to fix

The code change was adding quotes in one place. The data cleanup was three weeks of work reconciling ninety duplicate accounts, refunding two members who had been double-charged, and manually correcting phone numbers that had been stored mangled.

The developer's note in the commit: *the type is not a formatting detail, it is part of the value.*

---

## Composition

A radial layout with a central card and five satellites on blue platforms, connected by cyan and teal arrows.

**Centre:** a large white card on a glowing blue pedestal, showing a JSON object between white braces.

**Upper left:** **KEY**. **Upper right:** **VALUE**. **Lower left:** **ARRAY**. **Lower right:** **NESTED OBJECT**. **Bottom centre:** **DATA TYPES**.

## Element by element

**JSON OBJECT** *(centre)*
A white card with large white `{` and `}` braces, containing five rows. Each row has a coloured key tile, a colon, and a value tile:
- **name** *(teal)* : **"Ada Lovelace"** *(blue)*
- **age** *(coral)* : **28** *(blue)*
- **isScientist** *(teal)* : **true** *(blue)*
- **skills** *(coral)* : **["math", "logic", "coding"]** *(blue)*
- **address** *(teal)* : **{ … }** *(purple)*

**KEY** *(upper left)*
A teal rounded tile carrying a white **key** icon, beside a white note card reading *"The key is a string that identifies a value."*

**VALUE** *(upper right)*
A blue rounded tile carrying a white **gift box** icon, beside a white note card reading *"The value can be a string, number, Boolean, null, array, or another object."*

**ARRAY** *(lower left)*
A teal tray holding three teal blocks reading **"math"**, **"logic"**, **"coding"** in a row, beside a white note card reading *"An ordered list of values."*

**NESTED OBJECT** *(lower right)*
A cluster of **purple 3D blocks**, beside a white card showing braces containing **city : "London"**, **zip : "SW1A 1AA"**, **country : "UK"**, and a note card reading *"An object inside another object."*

**DATA TYPES** *(bottom centre)*
A wide platform carrying four tiles with their literal notation above their type names: **`" "`** / STRING (blue), **`123`** / NUMBER (coral), **`true`** / BOOLEAN (teal), **`null`** / NULL (purple).

## Colour and flow semantics

- **Cyan and teal arrows** radiate between the centre and the satellites in both directions — this is a definition map, not a flow.
- **Key tiles alternate teal and coral**; **value tiles are blue**; the **nested object is purple** in both the centre card and its satellite, so the eye connects `{ … }` to its expansion.
- The **four type tiles** are each given the colour used for that type elsewhere in the diagram, which quietly reinforces the mapping.
- No coral warning semantics here — coral is used decoratively on alternating keys, unlike the rest of the library where it means risk.

## How to present it

**Read the centre card aloud as a sentence.** "Name is Ada Lovelace, age is twenty-eight, is-scientist is true, skills are math logic and coding, address is another object." JSON is readable, and hearing it read as English removes most of the intimidation immediately.

**Ask what is different about the left and right of each colon.** Keys are always strings; values can be six things. That asymmetry, plus the fact that one of the six is "another object," is the entire format.

**Point at the four type tiles and ask about the quotes.** `"28"` versus `28`. `"true"` versus `true`. Ask which is which and why it matters. Then ask what `null` means as distinct from a missing key — the distinction that causes the most confusion and the most bugs.

**Tell the Cobalt story.** The leading zero is the perfect illustration because it is impossible to argue with: JSON numbers cannot have leading zeros, so the value is destroyed by the choice of type. Then ask the room for their own equivalent field. Every domain has one.

**Give them the rule and test it.** *If you will never do arithmetic on it, it is a string.* Then read out a list — member ID, age, postcode, quantity, phone number, price, invoice number, temperature — and have the room call string or number. The arguments are the learning.

**Point at `"zip": "SW1A 1AA"` in the nested object.** A code with letters and a space. Ask what would happen to a purely numeric postcode under the same field if types were chosen per value. One field, two types, broken indexing — which is what Cobalt hit.

**Ask what `{ … }` in the centre card means.** Then show that the nested-object satellite is its expansion. Recursion, in one visual move: values can be objects, so structure nests without limit.

**Connect it forward twice.** This is the `{ }` from both body panels of the previous diagram. And it is what the next diagram validates. JSON is the thread running through the whole course.

**Timing.** Twenty minutes. Thirty if you run the string-or-number drill, which is the exercise that prevents the most future bugs.

---

## Lab and checkpoint

**Lab:** Take one real JSON object from an API you use. Identify every key, its value type, any arrays, and any nested objects. For each value, apply the rule: *if you will never do arithmetic on it, it is a string.* If any field is currently a number but should be a string, write the bug that could result and the test that would catch the type change.

**Checkpoint:** What is the difference between `null` and a missing key?

**Answer:** `null` is an explicit value that means "this key was set to nothing." A missing key means "this key was never set." Code that treats them the same may behave differently depending on the producer, and serialisers may or may not emit missing keys.

## Glossary

- **Array** — an ordered list of values, written in square brackets.
- **Boolean** — a true or false value.
- **JSON** — a lightweight data format that uses objects with key/value pairs.
- **Key** — the string on the left of a colon that identifies a value.
- **Nested object** — a JSON object stored as a value inside another object.
- **Null** — the explicit value that represents no value.
- **Number** — a numeric value in JSON, with no leading zeros.
- **Object** — a collection of key/value pairs, written in braces.
- **String** — a text value, always written in quotes.
- **Value** — the data on the right of a colon, which can be a string, number, Boolean, null, array, or object.

## Sources

- JSON standard (ECMA-404 / RFC 8259)
- JSON data types and schema validation
- API payload design and type selection
