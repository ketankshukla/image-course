# Diagram 214 — Responsive diagrams, zoom, annotations, and reading order

![One visual lesson adapts across desktop, tablet, mobile, and 400 percent zoom with keyboard zoom and pan, annotations, clear reading order, alt text, and a detailed equivalent explanation; tiny text and color-only meaning are rejected.](../diagrams/214-responsive-diagrams-zoom-annotations-reading-order.png)

**Module:** The future visual-learning website
**Role in the course:** Make complex diagrams usable at every screen size and through visual, keyboard, zoom, and screen-reader paths.
**Layout:** The diagram shows one VISUAL LESSON adapting to DESKTOP TABLET MOBILE ZOOM 400%, with a coral risk path, and a teal safe path.

---

## At a glance

**Make complex diagrams usable at every screen size and through visual, keyboard, zoom, and screen-reader paths.**

- The diagram centers on **VISUAL LESSON** and its relationship to **EQUIVALENT PATH**.

- The diagram separates the tested, legitimate flow from failure paths that must fail closed.

- Maya's case: Maya opens the event-driven interface diagram on a phone at 400 percent zoom and cannot read its functional labels in the first prototype.

---

## What the diagram teaches

### 1. Annotations Should Connect A Hotspot To A Stable Concept, Not

Annotations should connect a hotspot to a stable concept, not pixel coordinates alone. The diagram makes this concrete through **ANNOTATIONS**. If the team skips this, a technically responsive image can still be inaccessible if labels become unreadable, pan traps scrolling, focus disappears, hotspots lack names, or important meaning exists only in color. This is the lesson the case study ends with: Preserve the visual overview, add purposeful navigation, and provide an equally complete semantic learning path.

### 2. Focus Must Remain Visible And The Viewport Must Not Trap

Focus must remain visible and the viewport must not trap normal page scrolling. This is visible in the drawing as **HORIZONTAL TRAP**. Without this step, a technically responsive image can still be inaccessible if labels become unreadable, pan traps scrolling, focus disappears, hotspots lack names, or important meaning exists only in color. In the walkthrough, The lesson switches to a single-column layout with a large overview and controls below the caption..

### 3. With The Learning Outcome And Define The Smallest Set

This step asks the team to start with the learning outcome and define the smallest set of visual relationships the diagram must communicate. The diagram shows this through **VISUAL LESSON**, which make the abstract step visible and testable. A large diagram and a small phone screen cannot share one fixed viewing assumption. The diagram is one representation of the lesson, not the only representation. If the team skips this, a technically responsive image can still be inaccessible if labels become unreadable, pan traps scrolling, focus disappears, hotspots lack names, or important meaning exists only in color. Maya's case makes this concrete: Maya opens the event-driven interface diagram on a phone at 400 percent zoom and cannot read its functional labels in the first prototype.

### 4. Author Concise Alt Text, A Complete Textual Trace, Node

Here the product must author concise alt text, a complete textual trace, node or region metadata, annotation order, and any long description. In the drawing, **ALT TEXT**, **READING ORDER**, **TINY TEXT** carry this responsibility. Concise alt text states the purpose and overall relationship; the detailed explanation and trace provide an equivalent learning path without trying to squeeze an essay into alt text. Store normalized positions or semantic node IDs, keep annotation order explicit, and recalculate visible placement as the asset resizes. Without this step, a technically responsive image can still be inaccessible if labels become unreadable, pan traps scrolling, focus disappears, hotspots lack names, or important meaning exists only in color. The result — The visual remains valuable without making the visual channel mandatory or forcing Maya to fight the viewport. — depends on getting this right.

### 5. Responsive Overview Plus Explicit Zoom, Reset, Annotation Navigation, And Full-screen

The diagram enforces this by showing the team how to render a responsive overview plus explicit zoom, reset, annotation navigation, and full-screen controls with native semantics. The visual anchors are **OVERVIEW**, **PAN ZOOM RESET**, **DESKTOP TABLET MOBILE ZOOM**; without them the step would be invisible to the user. Responsive design may scale the overview, change the surrounding layout, and offer deliberate zoom and pan while keeping controls and explanations outside the image usable. Keyboard users need focusable controls for zoom in, zoom out, reset, next annotation, previous annotation, and perhaps directional pan. The case study shows the risk: a technically responsive image can still be inaccessible if labels become unreadable, pan traps scrolling, focus disappears, hotspots lack names, or important meaning exists only in color. This is the lesson the case study ends with: Preserve the visual overview, add purposeful navigation, and provide an equally complete semantic learning path.

### 6. 320 CSS Pixels, Landscape And Portrait, 200 And 400 Percent

This is the discipline that makes the product test 320 CSS pixels, landscape and portrait, 200 and 400 percent zoom, reflow, keyboard, touch, screen readers, reduced motion, and high contrast. This idea sits on **KEYBOARD** and reaches the rest of the diagram through **KEYBOARD**, **DESKTOP TABLET MOBILE ZOOM**, **PAN ZOOM RESET**. CSS positioning must not create a different semantic sequence. Visual quality includes contrast, non-color cues, readable functional labels, adequate target sizes, reduced-motion behavior, high-resolution assets, and a reliable full-screen or new-window view without losing learner position. Missing this is how products end up with a technically responsive image can still be inaccessible if labels become unreadable, pan traps scrolling, focus disappears, hotspots lack names, or important meaning exists only in color. In the walkthrough, The lesson switches to a single-column layout with a large overview and controls below the caption..

### 7. Preserve The Learner's Selected Annotation And Scroll Position When

The team must preserve the learner's selected annotation and scroll position when the layout, route, or offline state changes before the interface can be trustworthy. The diagram shows this through **VISUAL LESSON**, **DESKTOP TABLET MOBILE ZOOM**, **OVERVIEW**, which make the abstract step visible and testable. A system that ignores this will eventually face a technically responsive image can still be inaccessible if labels become unreadable, pan traps scrolling, focus disappears, hotspots lack names, or important meaning exists only in color. The danger the case warns about, Maya opens the event-driven interface diagram on a phone at 400 percent zoom and cannot read its functional labels in the first prototype. should make this clear.

### 8. The standard in practice

The lesson is not a perfect prototype; it is a product contract. Make complex diagrams usable at every screen size and through visual, keyboard, zoom, and screen-reader paths.. The diagram makes that contract visible through **VISUAL LESSON**, **DESKTOP TABLET MOBILE ZOOM**, **OVERVIEW**, so the team can argue about the contract before choosing a framework. The contract is not framework-specific; it is the set of observable promises the product makes to the person using it. Maya's case warns that a technically responsive image can still be inaccessible if labels become unreadable, pan traps scrolling, focus disappears, hotspots lack names, or important meaning exists only in color. The practical standard is this: Preserve the visual overview, add purposeful navigation, and provide an equally complete semantic learning path.

### 9. The Next.js and Python surfaces

The same contract appears in both stacks, but the boundary moves with the architecture.
**In Next.js / React:**
- Use a semantic figure with external caption and explanation, responsive intrinsic dimensions, and a client viewer only for zoom, pan, and annotation state.
- Keep diagram files free of lesson numbers and long titles; render those as HTML headings and captions so they reflow, localize, and remain accessible.
- Store annotation coordinates and semantic order in lesson data, announce selected annotations concisely, and respect prefers-reduced-motion during viewport transitions.
- Keep the most sensitive payloads and policy decisions on the server and stream only user-visible, safe view models to client components.
**In Python / FastAPI:**
- Validate every diagram's dimensions, opaque background, filename, byte size, alt text, explanation, and annotation references during the content build.
- Generate a contact sheet and automated image inventory for editorial review while preserving the original source PNG bytes in the published asset set.
- Run link and relation checks that ensure every hotspot target exists and every diagram has a nonvisual equivalent before publication.
- Treat every framework callback or protocol event as raw input; validate and transform it into the product's own event vocabulary before it reaches the reducer or domain model.
Both implementations must avoid the same trap: a technically responsive image can still be inaccessible if labels become unreadable, pan traps scrolling, focus disappears, hotspots lack names, or important meaning exists only in color.
![One validated, versioned lesson model containing the complete visual teaching structure produces the document, website, search, offline package, and quizzes while preventing copy-and-paste drift.](../diagrams/213-reusable-visual-lesson-content-model.png)

Diagram 213 — *A reusable visual lesson content model* is the next lens on this idea. The same concepts reappear there with different emphasis, so the two diagrams should be read as a pair.

### 10. Analogy

A museum map has a wall overview, a handheld version, clear symbols, a numbered audio tour, and staff explanations. Shrinking the wall map until the words disappear is not a mobile strategy. The analogy keeps the lesson grounded. The diagram's **VISUAL LESSON** plays the same role as the central object in the analogy: it must be visible, labeled, and trustworthy without the user having to infer meaning from a long narrative. The parallel works because both situations require separating the object from the record, the attempt from the proof, and the promise from the evidence.

---

## Case study — Maya

Maya opens the event-driven interface diagram on a phone at 400 percent zoom and cannot read its functional labels in the first prototype.

### The walkthrough

1. The lesson switches to a single-column layout with a large overview and controls below the caption.
2. Maya opens the zoom viewer, uses keyboard controls, and moves through annotations in the authored logical order.
3. Each annotation has a short explanation linked to the matching node, while normal page scrolling remains available.
4. Maya can also skip the image and learn from the outcome, alt summary, visual trace, analogy, and case study in the same order.

### The result

The visual remains valuable without making the visual channel mandatory or forcing Maya to fight the viewport.

### The danger

A technically responsive image can still be inaccessible if labels become unreadable, pan traps scrolling, focus disappears, hotspots lack names, or important meaning exists only in color.

### The takeaway

Preserve the visual overview, add purposeful navigation, and provide an equally complete semantic learning path.

---

## Composition

The picture is a single-view explainer for *Responsive diagrams, zoom, annotations, and reading order*. On the left, the diagram shows one VISUAL LESSON adapting to DESKTOP TABLET MOBILE ZOOM 400%. At the top, layers OVERVIEW, NUMBERLESS FUNCTIONAL LABELS, HOTSPOTS, ANNOTATIONS, PAN ZOOM RESET, KEYBOARD, READING ORDER, ALT TEXT, DETAILED EXPLANATION. In the center, coral TINY TEXT, HORIZONTAL TRAP, COLOR ONLY, IMAGE OF TEXT. To the right, teal EQUIVALENT PATH. The eye travels from **VISUAL LESSON** through the central flow to **EQUIVALENT PATH**, with the contrast between coral risk paths and teal recovery paths giving the reader the core message at a glance.

## Element by element

- **VISUAL LESSON** — the visual lesson one VISUAL LESSON adapting to DESKTOP TABLET MOBILE ZOOM 400%..
- **DESKTOP TABLET MOBILE ZOOM** — the desktop tablet mobile zoom VISUAL LESSON adapting to DESKTOP TABLET MOBILE ZOOM 400%.
- **OVERVIEW** — the overview Layers OVERVIEW, NUMBERLESS FUNCTIONAL LABELS, HOTSPOTS, ANNOTATIONS, PAN ZOOM RESET, KEYBOARD, READING ORDER, ALT TEXT, DETAILED EXPLANATION..
- **NUMBERLESS FUNCTIONAL LABELS** — the numberless functional labels Layers OVERVIEW, NUMBERLESS FUNCTIONAL LABELS, HOTSPOTS, ANNOTATIONS, PAN ZOOM RESET, KEYBOARD, READING ORDER, ALT TEXT, DETAILED EXPLANATION..
- **HOTSPOTS** — one of the labels named by **NUMBERLESS**; this is the **HOTSPOTS** label.
- **ANNOTATIONS** — one of the labels named by **NUMBERLESS**; this is the **ANNOTATIONS** label.
- **PAN ZOOM RESET** — one of the labels named by **NUMBERLESS**; this is the **PAN ZOOM RESET** label.
- **KEYBOARD** — one input method the interface must support without relying on pointer or touch.
- **READING ORDER** — the semantic sequence in which screen-reader users encounter content.
- **ALT TEXT** — the concise alternative description of the diagram's purpose and relationships.
- **DETAILED EXPLANATION** — one of the labels named by **NUMBERLESS**; this is the **DETAILED EXPLANATION** label.
- **TINY TEXT** — the tiny text HORIZONTAL TRAP, COLOR ONLY, IMAGE OF TEXT..
- **HORIZONTAL TRAP** — the horizontal trap TINY TEXT, HORIZONTAL TRAP, COLOR ONLY, IMAGE OF TEXT..
- **COLOR ONLY** — the color only TINY TEXT, HORIZONTAL TRAP, COLOR ONLY, IMAGE OF TEXT..
- **IMAGE OF TEXT** — the image of text TINY TEXT, HORIZONTAL TRAP, COLOR ONLY, IMAGE OF TEXT..
- **EQUIVALENT PATH** — the equivalent path ..

---

## Colour and flow semantics

The course visual grammar applies directly to this diagram.

- **Cobalt platform** — A browser surface, state store, component catalog, product boundary, workspace, or learning-platform region. Here the cobalt surface under **VISUAL LESSON** and the surrounding workspace frames the product boundary; it tells the reader that this is a bounded product region, not an uncontrolled chat surface. It marks the product's responsibility to keep the user's workspace distinct from raw model output or runtime internals.

- **Cyan arrow** — A typed event, validated state update, user action, artifact reference, notification, or navigation path. Cyan arrows carry the flow of events, updates, and proposals from left to right, linking the typed cards and records to the reducer or next gate. When the reader sees cyan, they should expect a deliberate, validated transition rather than an accidental or hidden connection.

- **Teal arrow** — Authoritative state, accessible completion, informed consent, safe approval, preserved work, or verified recovery. Teal marks the authoritative and safe path, such as the committed receipt or restored state, distinguishing it from the raw request. This color tells the reader that the product has enough evidence and authority to proceed safely.

- **Coral path** — Conflict, stale UI, unsafe rendering, deceptive state, expired approval, privacy failure, lost work, or blocked action. Coral marks the conflict, stale state, or blocked action that appears when a control is missing or bypassed. It signals that the product should pause, surface the conflict, and offer a recovery path rather than proceed silently.

- **White card** — An event, component, stage, proposal, artifact, receipt, consent record, lesson, checkpoint, or recovery option. The labeled cards and records throughout the diagram are white, marking them as structured events, proposals, receipts, or recovery options. The white background separates user-meaningful records from raw system logs or generated text.

The overall flow moves from the initiating actor or request, through validation and reduction, toward either the teal recovery or completion path or the coral failure path. The color of each arrow and card is a trust cue, not a decoration.

---

## How to present it

- **Start with the user moment.** Maya opens the event-driven interface diagram on a phone at 400 percent zoom and cannot read its functional labels in the first prototype. Ask the room what they need to see to feel in control. Invite someone to describe the moment before any solution appears.

- **Point at VISUAL LESSON and ask what it represents.** Then trace the flow from there through the next two or three elements, naming the color and direction of each arrow. Encourage them to name the incoming trigger, the visible state, and the decision the product must make.

- **Point at VISUAL LESSON for step 1.** With The Learning Outcome And Define The Smallest Set. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at ALT TEXT for step 2.** Author Concise Alt Text, A Complete Textual Trace, Node. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at OVERVIEW for step 3.** Responsive Overview Plus Explicit Zoom, Reset, Annotation Navigation, And Full-screen. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at KEYBOARD for step 4.** 320 CSS Pixels, Landscape And Portrait, 200 And 400 Percent. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at HOTSPOTS for step 5.** Preserve The Learner's Selected Annotation And Scroll Position When. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Use the analogy.** A museum map has a wall overview, a handheld version, clear symbols, a numbered audio tour, and staff explanations. Shrinking the wall map until the words disappear is not a mobile strategy. Draw the parallel to the diagram and ask what would break if the two situations were handled the same way.

- **Tell the case study.** Maya opens the event-driven interface diagram on a phone at 400 percent zoom and cannot read its functional labels in the first prototype Walk through the walkthrough and stop at the moment the old design would have failed. Pause at the step where the old design would have failed and ask how the new interface prevents it.

- **Run the lab.** Prototype one diagram viewer and test it at five viewport sizes, 200 and 400 percent zoom, keyboard only, touch, two screen readers, reduced motion, and forced colors. Record focus order, annotation order, scroll behavior, label readability, and the nonvisual equivalent. Ask pairs to present one part of the diagram and explain how the other parts reference it without merging their identities.

- **Pose the checkpoint.** Should the detailed diagram explanation be placed entirely inside the image alt attribute? Let the room answer before confirming the principle. Collect answers, then confirm the principle and note any exceptions the team should watch for.

- **Close on the contract.** Preserve the visual overview, add purposeful navigation, and provide an equally complete semantic learning path. Ask the team what their own product's equivalent of the contract would be.

---

## Lab and checkpoint

**Lab:** Prototype one diagram viewer and test it at five viewport sizes, 200 and 400 percent zoom, keyboard only, touch, two screen readers, reduced motion, and forced colors. Record focus order, annotation order, scroll behavior, label readability, and the nonvisual equivalent.

**Checkpoint:** Should the detailed diagram explanation be placed entirely inside the image alt attribute?

**Answer:** No. Alt text should concisely identify the purpose and core relationship. Put the full trace and explanation in visible structured content so everyone can use it and navigate it.

---

## Glossary

- **Reading order** — semantic sequence in which content is understood
- **Annotation** — explanation tied to a visual node or region
- **Reflow** — content adapting without two-dimensional scrolling for ordinary reading

---

## Sources

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/)
- [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [Next.js accessibility](https://nextjs.org/docs/architecture/accessibility)

## Related lessons

- Diagram 208 — Accessibility, plain language, uncertainty, and trust cues
- Diagram 213 — A reusable visual lesson content model
- Diagram 216 — Progress, checkpoints, quizzes, accessibility, and offline use

---