"""Generate Volume 9 diagram-doc Markdown files matching Course 7 structure and depth."""
import json
import re
import pathlib
import sys

BASE = pathlib.Path(__file__).resolve().parent
JSON_PATH = BASE / "Volume 9 Course Content.json"
PROMPT_LIB = BASE / "DIAGRAM-PROMPT-LIBRARY.md"
OUT_DIR = BASE / "diagram-docs"

WORD_TARGET = 2500

# Common lowercase and uppercase stopwords for label/text processing
STOP = {
    "a", "an", "the", "and", "or", "but", "of", "in", "on", "at", "to", "for",
    "from", "by", "with", "as", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "could", "should",
    "may", "might", "must", "can", "this", "that", "these", "those", "it", "its",
    "they", "them", "their", "there", "then", "than", "when", "where", "what", "who",
    "which", "how", "why", "if", "so", "such", "no", "not", "only", "also", "just",
    "even", "still", "yet", "already", "each", "every", "all", "any", "some", "many",
    "much", "more", "most", "other", "another", "several", "few", "both", "either",
    "neither", "one", "two", "three", "first", "last", "same", "next", "previous",
    "after", "before", "during", "while", "until", "since", "because", "although",
    "though", "unless", "whether", "once", "into", "onto", "upon", "within", "without",
    "through", "throughout", "among", "between", "beside", "under", "over", "above",
    "below", "around", "across", "against", "along", "behind", "beyond", "near", "off",
    "out", "up", "down", "via", "about", "above", "again", "against", "down", "off",
    "over", "under", "up", "so", "too", "very", "just", "own", "same", "than", "too",
}

LABEL_STOP = {
    "SHOW", "ADD", "USE", "WITH", "FROM", "INTO", "THEN", "AND", "OR", "THE", "A",
    "AN", "OF", "IN", "ON", "AT", "FOR", "BY", "AS", "IS", "ARE", "HAS", "HAVE",
    "NOT", "NO", "ALL", "EVERY", "GO", "DO", "DOES", "GET", "MAKE", "PUT", "SET",
    "KEEP", "CREATE", "BLOCK", "LEAD", "GOES", "OFFER", "AFTER", "BEFORE", "WHILE",
    "WHERE", "WHEN", "HOW", "WHY", "WHAT", "WHO", "WHICH", "THAT", "THIS", "THESE",
    "THOSE", "EACH", "BOTH", "ANY", "SOME", "MORE", "LESS", "OTHER", "NEW", "OLD",
    "GOOD", "BAD", "SAFE", "UNSAFE", "TO", "VIA", "GO", "LEAVES", "STARTS", "STOPS",
    "CONTINUES", "BECOMES", "PRODUCES", "OUTPUTS", "INPUTS", "LEADS", "ENTERS", "EXITS",
    "TURNS", "TAKES", "GIVES", "GETS", "MAKES", "PUTS", "SETS", "KEEPS", "HOLDS",
    "BUILDS", "BEGINS", "ENDS", "REMAINS", "STAYS", "COMES", "RUNS", "CALLS", "SENDS",
    "RECEIVES", "UPDATES", "LOADS", "FETCHES", "FETCH", "SHOWS", "DISPLAYS", "RENDERS",
    "PASSES", "MOVES", "DRAWS", "MARKS", "NAMES", "OFFERS", "CHOOSES", "SELECTS",
    "SPLITS", "LINKS", "CONNECTS", "PROCESSES", "VALIDATES", "CHECKS", "SCANS", "BLOCKS",
    "OPENS", "CLOSES", "PAUSES", "RESUMES", "RETURNS", "BECOMES", "GROWS", "FALLS",
}

COMMON_DESC = {
    "AGENT RUN": "the running agent process that emits typed lifecycle, text, tool, activity, state, artifact, approval, and error events.",
    "AGENT": "a delegated automated actor that proposes actions, requests input, or performs work under human and policy control.",
    "USER": "the human person whose attention, consent, and control the product must preserve.",
    "MAYA": "the human customer and learner in the running Acme case study.",
    "ACME": "the fictional company whose agent workspace and learning platform illustrate the lesson.",
    "EVENT STREAM": "the ordered channel that carries typed events from the agent run toward the interface reducer.",
    "REDUCER": "the validated function that turns events and prior state into new product state without parsing prose.",
    "SNAPSHOT": "an authoritative, complete replacement view of state with a version and schema metadata.",
    "DELTA": "an ordered set of changes, often JSON Patch operations, applied to a known base revision.",
    "UI STATE": "the visible, reduced representation of the authoritative state that the interface renders.",
    "CONFLICT": "evidence that local and authoritative state cannot be reconciled safely.",
    "BROWSER": "the user's client surface that receives the live stream and must recover after network breaks.",
    "LIVE STREAM": "the continuous event stream that feeds the interface with run, message, tool, and state updates.",
    "OFFLINE BUFFER": "local recovery metadata that preserves the last cursor and safe drafts while disconnected.",
    "RECONNECT REQUEST": "the message a client sends with its last seen cursor so the server can replay missed events.",
    "DEDUP SET": "the gate that ignores duplicate event IDs during replay.",
    "ORDER GATE": "the gate that applies replayed events in the correct sequence.",
    "RESTORED UI": "the interface state reconstructed from replayed and deduplicated events.",
    "OPTIMISTIC UI": "the temporary, local prediction shown before the server confirms an action.",
    "LOCAL DRAFT": "the user's pending input kept separately from the authoritative server state.",
    "RECONCILE": "the process of aligning the interface with a committed receipt, rejection, or fresh snapshot.",
    "AUTHORITATIVE SERVER": "the business system that owns durable state and returns committed receipts or rejections.",
    "COMMITTED RECEIPT": "the durable proof that the server accepted a command and produced an effect.",
    "REJECTED CONFLICT": "the server's response when a command cannot be applied because the state changed.",
    "WORKFLOW": "the sequence of stages that the agent and product move through to complete a task.",
    "SIMPLE VIEW": "the default, calm interface that shows the current stage and next safe action.",
    "EXPANDED VIEW": "the optional details that reveal elapsed time, evidence count, tool status, and receipts.",
    "TOOL CALL": "a card that tracks a proposed, running, or completed tool execution.",
    "EVIDENCE": "versioned support for a decision, with source, freshness, and authority.",
    "ARTIFACT": "a durable output that outlives the run, such as a file, summary, or recommendation.",
    "RECEIPT": "durable proof of a decision, effect, or user-visible transition.",
    "APPROVAL CARD": "the versioned card that asks the person to approve, reject, edit, or ask about a proposal.",
    "DECISION GATE": "the point where the workflow pauses because human input or authority is required.",
    "CURRENT PLAN": "the visible goal, constraints, priorities, steps, and artifacts that define active work.",
    "USER STEERING": "the structured change a person makes to the goal, constraints, or priorities.",
    "IMPACT ANALYZER": "the component that classifies prior work as keep, recheck, or invalidate after a change.",
    "NEW PLAN VERSION": "the immutable, versioned plan produced after a steering change.",
    "ACTION TIMELINE": "the ordered record of queued, running, committed, cancelled, undone, and compensated actions.",
    "AUDIT HISTORY": "the durable record of every action, decision, cancellation, compensation, and recovery.",
    "USER RECEIPT": "the user-facing record that explains what happened and what remains.",
    "KEYBOARD": "one input method the interface must support without relying on pointer or touch.",
    "SCREEN READER": "assistive technology that relies on names, roles, values, focus, and live regions.",
    "FOCUS ORDER": "the sequence in which a keyboard user reaches each control.",
    "LIVE STATUS": "an accessible announcement of important state changes.",
    "TEXT LABELS": "visible, persistent words that identify a control or state without relying on icons.",
    "CONTRAST": "the visual difference between text and background that makes content readable.",
    "TARGET SIZE": "the minimum hit area a control needs for touch and pointer use.",
    "ERROR HELP": "plain language that explains a failure and the safe next step.",
    "UNCERTAINTY": "honest communication about missing, stale, conflicting, or insufficient evidence.",
    "MODEL": "the language model or agent that proposes a declarative interface structure.",
    "JSON SCHEMA": "the contract that defines which component, properties, and values are valid.",
    "COMPONENT ALLOWLIST": "the finite catalog of approved interface components a model may request.",
    "PROP VALIDATOR": "the layer that checks the type, size, and safety of each component property.",
    "ACTION POLICY": "the rule that decides whether a proposed action is allowed in the current context.",
    "SAFE COMPONENT CATALOG": "the product-owned set of accessible, tested components that render validated data.",
    "VERSION ADAPTER": "the boundary that translates a supported wire protocol version into a stable internal model.",
    "MCP SERVER": "the server that declares tools and, optionally, a UI resource for the host.",
    "HOST": "the product surface that loads an MCP App and controls the sandbox, bridge, and consent.",
    "SANDBOXED IFRAME": "the isolated browsing context that hosts an embedded app without giving it host authority.",
    "APP BRIDGE": "the typed JSON-RPC message channel between the embedded app and the host.",
    "CONSENT": "the informed, specific, and revocable user choice before data or authority is granted.",
    "ORIGIN CHECK": "the validation that a message or resource comes from an expected source.",
    "DATA MINIMIZATION": "the practice of sharing only the fields and duration necessary for a purpose.",
    "AUDIT RECEIPT": "the record that captures a decision, grant, or event for later inspection.",
    "AGENT PROPOSAL": "the typed suggestion the agent makes to use a device or browser capability.",
    "USER GESTURE": "the genuine human interaction required to activate a browser or device feature.",
    "HOST POLICY": "the product rule that decides which device actions are allowed for a purpose.",
    "EXECUTE ON DEVICE": "the safe completion of a browser or device action after user confirmation.",
    "UNTRUSTED INPUTS": "any dynamic text, retrieval, tool result, app message, URL, or file that could be harmful.",
    "ENCODE": "the contextual escaping that makes data safe for its exact rendering context.",
    "CSP": "the Content Security Policy that limits where scripts, frames, and connections may originate.",
    "PERMISSIONS POLICY": "the browser policy that restricts powerful features such as camera or location.",
    "SANDBOX": "the iframe attribute that isolates embedded content from the host's authority.",
    "AUTHZ": "the server-side authorization that checks identity, tenant, resource, and policy before any effect.",
    "REDACTION": "the removal of sensitive fields before data reaches a component or log.",
    "AUTHORING SOURCE": "the structured lesson data that feeds all published formats.",
    "VALIDATED LESSON MODEL": "the versioned, schema-validated representation of one lesson.",
    "SCHEMA VERSION MIGRATION": "the explicit path that updates content from one schema version to the next.",
    "DOCX": "the document projection generated from the validated lesson model.",
    "WEBSITE": "the web page projection generated from the validated lesson model.",
    "SEARCH": "the indexed view that lets learners find lessons, terms, and sources.",
    "OFFLINE": "the cached pack that lets learners continue without a network connection.",
    "QUIZ": "the practice and assessment projection generated from the lesson model.",
    "DESKTOP": "the large-screen viewport with an overview and side-by-side explanation.",
    "TABLET": "the mid-size viewport that balances overview and detail.",
    "MOBILE": "the small viewport that stacks content and reduces visual noise.",
    "ZOOM 400%": "the high-magnification state that tests label readability and reflow.",
    "ALT TEXT": "the concise alternative description of the diagram's purpose and relationships.",
    "READING ORDER": "the semantic sequence in which screen-reader users encounter content.",
    "COURSE KNOWLEDGE GRAPH": "the web of lessons, terms, sources, and relationships that supports navigation.",
    "LESSON": "one visual teaching unit with outcome, diagram, trace, case study, and glossary.",
    "PREREQUISITE": "a relationship that says one lesson should be understood before another.",
    "SOURCE": "an authoritative reference with label, URL, checked date, and version.",
    "LEARNER": "the person using the visual course to understand agentic product design.",
    "LOCAL PROGRESS": "the learner-owned record of completed activities, kept on the device first.",
    "OPTIONAL SYNC": "the consented upload of learner data to another device or account.",
    "SERVICE WORKER": "the script that caches the app shell and versioned course packs for offline use.",
    "QUEUED ACTIONS": "the offline writes that wait for reconnection and reconciliation.",
    "RECONNECT": "the process of restoring the online state after an offline period.",
    "DURABLE RUN": "the persistent task that continues after the user leaves the workspace.",
    "RETURN OPTIONS": "the channels through which the product can call the user back.",
    "APP BADGE": "the in-app counter that shows a task needs attention.",
    "EMAIL DIGEST": "a batched summary sent to the user's email.",
    "PUSH NOTIFICATION": "a permission-based alert delivered by the browser or operating system.",
    "QUIET HOURS": "the user's chosen times when interruptions should not occur.",
    "DATA LIFECYCLE": "the stages of collect, use, store, share, remember, export, and delete.",
    "USER CONTROL CENTER": "the interface where a person reviews data purpose, categories, memory, and deletion.",
    "CONSENT RECEIPT": "the versioned record of a specific informed privacy choice.",
    "DELETION FAN OUT": "the workflow that propagates deletion through primary, vector, cache, log, and backup stores.",
    "VERIFICATION": "the proof that deleted data no longer influences retrieval or outputs.",
    "PRODUCT EVENT": "a privacy-minimized record of a meaningful product transition.",
    "FEEDBACK": "the learner or user report that captures confusion, barrier, or incident.",
    "QUALITY EVAL": "a controlled assessment of how well the system performed on defined cases.",
    "SAFETY REVIEW": "the review of outputs and interactions for harm, risk, or policy violation.",
    "ACCESSIBILITY EVIDENCE": "the record that the interface works across input methods and assistive technologies.",
    "METRIC CARD": "the exposed definition of a measure, including numerator, denominator, exclusions, slice, window, and version.",
    "EXPERIMENT": "a controlled change that requires risk review, consent, guardrails, and debrief.",
    "AGENT WORKSPACE": "the product where Maya completes governed customer work.",
    "VISUAL LEARNING PLATFORM": "the product that teaches the course through the same visual model.",
    "HUMAN CONTROL LOOP": "the sequence from request through plan, progress, evidence, proposal, approval, action, receipt, and recovery.",
    "REQUEST": "the human or system starting point that names the desired outcome.",
    "PLAN": "the visible set of steps, constraints, and priorities for completing the request.",
    "PROGRESS": "the honest, observable state of the running task.",
    "PROPOSAL": "the immutable, versioned description of a requested decision.",
    "ACTION": "the committed, authoritative effect after a decision.",
    "RECOVERY": "the safe path after an error, conflict, partial success, or cancelled effect.",
    "ACCESSIBILITY": "the cross-cutting requirement that the product works for every user.",
    "SECURITY": "the cross-cutting requirement that authority, data, and rendering remain safe.",
    "PRIVACY": "the cross-cutting requirement that data collection, memory, and deletion remain under user control.",
    "OBSERVABILITY": "the cross-cutting requirement that the product state can be inspected and explained.",
    "EVALUATION": "the cross-cutting process that measures outcomes and quality.",
    "OFFLINE CROSS-CUTTING": "the cross-cutting requirement that essential learning and work remain available without a network.",
    "NEXTJS": "the React framework used for the web shell, accessible views, and client components.",
    "REACT": "the UI library used for rendering controlled components and state.",
    "FASTAPI": "the Python framework used for typed APIs and durable business coordination.",
    "MCP": "the Model Context Protocol that connects agents to declared tools and resources.",
    "A2A": "the Agent-to-Agent protocol that coordinates task-oriented peer agents.",
    "AG-UI": "the protocol that carries typed agent interface events.",
    "MCP APPS": "the extension that pairs an MCP tool with a declared UI resource.",
    "A2UI": "the protocol for server-driven, model-proposed, product-controlled interface components.",
    "RAG": "the retrieval approach that grounds answers in versioned evidence.",
    "TOOLS": "the capabilities an agent can call through declared, policy-bound interfaces.",
}


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def parse_prompt_library(path):
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(
        r"##\s+Diagram\s+(\d+)\s+-\s+(.*?)\n\n"
        r"Output filename:\s+`(.*?)`\n\n"
        r"Pattern status:\s+(.*?)\n\n"
        r"Use case:.*?extra text\.\n\n"
        r"(.*?)\n\n"
        r"Accessibility alt text:\s+(.*?)(?=\n\n##\s+Diagram|\Z)",
        re.DOTALL,
    )
    result = {}
    for m in pattern.finditer(text):
        lid = int(m.group(1))
        result[lid] = {
            "title_in_prompt": m.group(2).strip(),
            "output_filename": m.group(3).strip(),
            "pattern_status": m.group(4).strip(),
            "prompt": re.sub(r"\s+", " ", m.group(5).strip()),
            "alt": m.group(6).strip(),
        }
    return result


def split_sentences(text):
    # Simple sentence split that handles common punctuation without destroying abbreviations too badly
    text = re.sub(r"([.!?])\s+", r"\1|", text)
    return [s.strip() for s in text.split("|") if s.strip()]


def words(text):
    return len(re.findall(r"\b\w+\b", text))


def extract_labels(prompt):
    """Find uppercase teaching labels in a prompt and merge adjacent tokens."""
    matches = list(re.finditer(r"[A-Z][A-Z0-9%]*(?:[-/][A-Z][A-Z0-9%]*)?", prompt))
    if not matches:
        return []
    groups = [[matches[0]]]
    for m in matches[1:]:
        prev = groups[-1][-1]
        if m.start() <= prev.end() + 1:
            groups[-1].append(m)
        else:
            groups.append([m])
    labels = []
    seen = set()
    for g in groups:
        label = prompt[g[0].start() : g[-1].end()]
        core = re.sub(r"[-/]", " ", label)
        parts = core.split()
        if all(p in LABEL_STOP for p in parts):
            continue
        if len(parts) == 1 and (parts[0] in LABEL_STOP or len(parts[0]) <= 2):
            continue
        if label not in seen:
            seen.add(label)
            labels.append(label)
    return labels


def tidy(text):
    return re.sub(r"\s+", " ", text.strip())


def shorten_heading(text, lo=4, hi=10):
    # Convert a trace step into a clean 4-10 word conceptual heading
    text = text.strip(" -.!?\"")
    # Remove leading directive/connector words and leftover lowercase starter words
    text = re.sub(r"^(Name|Map|Design|Define|Create|Show|Give|Render|Test|Use|Apply|Persist|Record|Receive|Return|Build|Write|Start|Stop|On|In|At|Then|Next|Finally|First|Second|After|Before|For)\s+", "", text, flags=re.IGNORECASE)
    text = re.sub(r"^(each|every|all|the|a|an|this|that)\s+", "", text, flags=re.IGNORECASE)
    # Remove parenthetical content; keep quoted examples if they are the first words
    text = re.sub(r"\s*\(.*?\)", "", text)
    # Split and cap
    parts = text.split()
    # Avoid weak trailing words
    weak = {"and", "or", "with", "for", "of", "to", "in", "on", "a", "an", "the", "from", "by", "as", "such", "like", "so", "then", "into", "onto", "over", "under", "upon", "are", "is", "was", "were", "be", "being", "been", "becomes", "becoming", "means", "requires", "needs", "should", "must", "can", "could", "would", "will", "shall", "may", "might", "has", "have", "had", "does", "do", "did"}
    while parts and parts[-1].lower() in weak:
        parts.pop()
    if len(parts) > hi:
        parts = parts[:hi]
        while parts and parts[-1].lower() in weak:
            parts.pop()
    if len(parts) < lo:
        return text
    return " ".join(parts).strip(" -,.!?:\"") or text


def title_case(phrase):
    # Title case but keep acronyms all-caps
    parts = phrase.split()
    out = []
    for p in parts:
        if re.fullmatch(r"[A-Z][A-Z0-9]+", p):
            out.append(p)
        elif p[0].isalpha():
            out.append(p[0].upper() + p[1:])
        else:
            out.append(p)
    return " ".join(out)


def normalize_keys(text):
    return set(re.findall(r"\b[a-z]+\b", text.lower())) - STOP


def sentence_keyword_score(step, sentence):
    k1 = normalize_keys(step)
    k2 = normalize_keys(sentence)
    if not k1 or not k2:
        return 0
    return len(k1 & k2)


def assign_sentences(trace, explanation):
    sents = split_sentences(explanation)
    out = {i: [] for i in range(len(trace))}
    used = set()
    # assign each sentence to the trace step with highest keyword overlap
    for si, sent in enumerate(sents):
        best_i, best_score = -1, 0
        for ti, step in enumerate(trace):
            score = sentence_keyword_score(step, sent)
            if score > best_score:
                best_score = score
                best_i = ti
        if best_i >= 0 and best_score > 0:
            out[best_i].append((si, sent))
            used.add(si)
    # collect leftover sentences for a closing synthesis
    leftover = [sents[si] for si in range(len(sents)) if si not in used]
    return out, leftover


def relevant_labels(step, prompt_labels, n=4):
    k = normalize_keys(step)
    scored = []
    for lab in prompt_labels:
        lab_key = " ".join(re.findall(r"[A-Za-z]+", lab)).lower()
        score = len(k & (set(lab_key.split()) - STOP))
        if lab.upper() in step.upper():
            score += 5
        scored.append((score, lab))
    scored.sort(reverse=True, key=lambda x: x[0])
    return [lab for _, lab in scored[:n] if _ > 0][:n]


def pick_labels(prompt_labels, n=4, exclude=None):
    if exclude is None:
        exclude = set()
    out = [l for l in prompt_labels if l not in exclude][:n]
    if len(out) < n:
        for l in prompt_labels:
            if l not in exclude and l not in out:
                out.append(l)
            if len(out) >= n:
                break
    return out


def step_to_clause(step):
    # Convert an imperative trace step into a lower-case clause for body prose.
    # Keep the leading verb so "The team must {clause}" reads correctly.
    if not step:
        return ""
    # Strip only leading articles/connector words and any trailing period
    s = re.sub(r"^(the |a |an |this |that |each |every )", "", step, flags=re.IGNORECASE).strip(". ")
    return s[0].lower() + s[1:]


def risk_sentence(step, case_study, explanation_sents, idx):
    danger = case_study.get("danger", "")
    takeaway = case_study.get("takeaway", "")
    if not danger:
        danger = "the interface can look right while the underlying state is wrong"
    d = danger.strip(".")
    if d and d[0].isupper():
        d = d[0].lower() + d[1:]
    # Vary how the risk is stated
    templates = [
        f"If the team skips this, {d}.",
        f"Without this step, {d}.",
        f"The case study shows the risk: {d}.",
        f"Missing this is how products end up with {d}.",
        f"A system that ignores this will eventually face {d}.",
    ]
    return templates[idx % len(templates)]


def case_sentence(case_study, idx):
    situation = case_study.get("situation", "").strip()
    result = case_study.get("result", "").strip()
    takeaway = case_study.get("takeaway", "").strip()
    walk = case_study.get("walkthrough", [])
    templates = [
        f"Maya's case makes this concrete: {situation}",
        f"The result — {result} — depends on getting this right.",
        f"This is the lesson the case study ends with: {takeaway}",
        f"In the walkthrough, {walk[0] if walk else 'Maya sees the correct behavior'}.",
        f"The danger the case warns about, {situation} should make this clear.",
    ]
    t = templates[idx % len(templates)]
    # ensure punctuation
    if not t.endswith("."):
        t += "."
    return t


def trace_body(step, explanation_sents, prompt_labels, case_study, idx, lesson_title):
    labels = relevant_labels(step, prompt_labels, n=3)
    if not labels:
        labels = pick_labels(prompt_labels, n=3)
    label_phrase = ", ".join(f"**{l}**" for l in labels[:3]) if labels else "the diagram"

    clause = step_to_clause(step)
    opens = [
        f"This step asks the team to {clause}.",
        f"Here the product must {clause}.",
        f"The diagram enforces this by showing the team how to {clause}.",
        f"This is the discipline that makes the product {clause}.",
        f"The team must {clause} before the interface can be trustworthy.",
    ]

    visuals = [
        f"The diagram shows this through {label_phrase}, which make the abstract step visible and testable.",
        f"In the drawing, {label_phrase} carry this responsibility.",
        f"The visual anchors are {label_phrase}; without them the step would be invisible to the user.",
        f"This idea sits on **{labels[0] if labels else 'the central element'}** and reaches the rest of the diagram through {label_phrase}.",
    ]

    parts = [opens[idx % len(opens)], visuals[idx % len(visuals)]]

    if explanation_sents:
        for _, sent in explanation_sents[:2]:
            parts.append(sent)

    parts.append(risk_sentence(step, case_study, explanation_sents, idx))
    parts.append(case_sentence(case_study, idx))

    return " ".join(tidy(p) for p in parts if p)


def concept_body(sentences, prompt_labels, case_study, outcome, lesson_title, concept_idx):
    if not sentences:
        return None
    labels = relevant_labels(sentences[0], prompt_labels, n=3) or pick_labels(prompt_labels, n=3)
    label_phrase = ", ".join(f"**{l}**" for l in labels[:3])
    parts = [s for s in sentences[:3]]
    visuals = [
        f"The diagram makes this concrete through {label_phrase}.",
        f"This is visible in the drawing as {label_phrase}.",
        f"The visual anchors, {label_phrase}, turn this principle into a testable picture.",
    ]
    parts.append(visuals[concept_idx % len(visuals)])
    parts.append(risk_sentence(sentences[0], case_study, [], concept_idx))
    parts.append(case_sentence(case_study, concept_idx + 2))
    return " ".join(tidy(p) for p in parts if p)


def describe_label(label, prompt, outcome, lesson_title, prompt_labels):
    if label in COMMON_DESC:
        return COMMON_DESC[label]

    # Look for the most specific clause in the prompt that mentions this label
    patterns = [
        r"(\b[A-Z][A-Z0-9\s\-/]+\b)\s+(?:\w+ing|\w+s?)\s+[^.;:]*\b" + re.escape(label) + r"\b[^.;:]*",
        r"(\b[A-Z][A-Z0-9\s\-/]+\b)\s+(?:\w+ing|\w+s?)\s+[^.;:]*\b" + re.escape(label) + r"\b[^.;:]*",
        r"(?:coral|teal)\s+" + re.escape(label) + r"\b[^.;:]*",
        r"\b" + re.escape(label) + r"\s+path\s+(?:to|into|toward|from|through)\s+[^.;:]*",
        r"[^.;:]*?\b" + re.escape(label) + r"\b[^.;:]*[.?:;]?",
    ]
    clause = ""
    main = ""
    for pat in patterns:
        m = re.search(pat, prompt)
        if m:
            clause = tidy(m.group(0))
            raw_main = m.group(1).strip() if m.lastindex and m.group(1) else ""
            if raw_main and raw_main not in LABEL_STOP and len(raw_main) >= 2:
                main = raw_main
            else:
                main = ""
            break

    if not clause:
        return f"a teaching element in this diagram that helps illustrate {outcome.lower() if outcome else 'the lesson'}."

    # Parent + container + with [list] (e.g., "EVIDENCE card with SOURCE, FRESHNESS, AUTHORITY")
    with_match = re.search(r"(\b[A-Z][A-Z0-9\s\-/]+\b)\s+(?:\w+ing|\w+s?)?\s*\b(cards?|panels?|labels?|states?|options?|choices?|paths?|badges?|regions?)\b\s+(?:with|having|containing|showing|listing)\s+([^.;:]*\b" + re.escape(label) + r"\b[^.;:]*)", clause, re.I)
    if with_match and with_match.group(1) not in LABEL_STOP:
        parent = with_match.group(1)
        container = with_match.group(2).lower()
        seg = with_match.group(3)
        child_noun = {"cards": "field", "panels": "field", "labels": "value", "states": "value",
                      "options": "option", "choices": "choice", "paths": "path", "badges": "badge", "regions": "region"}.get(container, "field")
        if "," in seg or " and " in seg or " or " in seg:
            return f"one of the {child_noun}s on the **{parent}** {container}; this is the **{label}** {child_noun}."
        return f"a {child_noun} on the **{parent}** {container}; this shows the **{label}** {child_noun}."

    # List with a named parent (e.g., "APPROVAL CARD names PROPOSAL, EFFECT...")
    if main and ("," in clause or " and " in clause or " or " in clause):
        verb = re.search(r"\b(emits?|names?|lists?|has?|holds?|contains?|identifies?)\b", clause, re.I)
        noun_map = {"emits": "card", "names": "field", "lists": "item", "has": "item", "holds": "item", "contains": "item", "identifies": "item"}
        noun = noun_map.get(verb.group(1).lower(), "item") if verb else "item"
        container_match = re.search(r"\b(cards?|panels?|labels?|states?|options?|choices?|paths?|badges?|regions?)\b", clause, re.I)
        if container_match:
            c = container_match.group(1).lower()
            noun = {"cards": "card", "panels": "panel", "labels": "label", "states": "state",
                    "options": "option", "choices": "choice", "paths": "path", "badges": "badge", "regions": "region"}.get(c, c.rstrip("s"))
        return f"one of the {noun}s named by **{main}**; this is the **{label}** {noun}."

    # If the clause is a list of cards/panels/states/options with a container word
    list_match = re.search(r"(?:emits?|sends?|carries?|updates?|produces?|streams?|with)\s+(?:.*?)\b(cards?|panels?|labels?|states?|options?|choices?|paths?|badges?|regions?)\b", clause, re.I)
    if list_match and ("," in clause or " and " in clause or " or " in clause):
        container = list_match.group(1).lower()
        singular = {"cards": "card", "panels": "panel", "labels": "label", "states": "state",
                    "options": "option", "choices": "choice", "paths": "path", "badges": "badge", "regions": "region"}.get(container, container.rstrip("s"))
        return f"one of the {container} in the diagram; this is the **{label}** {singular}."

    # If the clause describes an action path
    path_match = re.search(r"\b" + re.escape(label) + r"\b\s+path\s+(?:to|into|toward|from)\s+([^\.]+)", clause, re.I)
    if path_match:
        target = tidy(path_match.group(1))
        return f"the {label.lower()} path that leads to **{target}**."

    # Clean the clause and use it as a description
    clause = re.sub(r"^(Show |Add |Render |A |An |The |Coral |Teal |A |An )", "", clause, flags=re.IGNORECASE).strip()

    # If the clause is "SUBJECT has/records/shows/carry LABEL", describe the label as the object
    subj_match = re.search(r"(\b[A-Z][A-Z0-9\s\-/]+\b)\s+(?:has|shows|records|carries|holds)\s+([^.;:]*\b" + re.escape(label) + r"\b[^.;:]*?)\s*(?:[;:.]|$)", clause, re.I)
    if subj_match:
        subject = subj_match.group(1)
        rest = subj_match.group(2).strip(" ,;:-")
        if subject.upper() == label:
            rest2 = re.sub(r"\b" + re.escape(label) + r"\b", "", rest, flags=re.I).strip(" ,;:-")
            return f"the {label.lower()} {rest2}." if rest2 else f"the **{label}**."
        return f"the **{label}** recorded by **{subject}**."

    if clause.lower().startswith(label.lower()):
        clause = clause[len(label):].strip(" ,;:-")
        return f"the {label.lower()} {clause}."

    # Verb-first descriptions
    if re.match(r"^(emits|sends|carries|produces|streams|updates|controls|manages|receives|processes|validates|checks|loads|leads|enters|exits|blocks|rejects|denies|exposes|creates|stores|remembers|shares|deletes|collects|uses)", clause, re.I):
        return f"the {label.lower()} that {clause}."

    return f"the {label.lower()} {clause}."


def composition_paragraph(prompt, labels, lesson_title):
    """Turn the diagram prompt into a positional visual scene."""
    raw_clauses = [c.strip() for c in re.split(r"[.!?;]", prompt) if c.strip()]
    pieces = [f"The picture is a single-view explainer for *{lesson_title}*."]
    positions = ["On the left", "At the top", "In the center", "To the right", "Across the middle", "Along the bottom", "Near the top-left", "Near the bottom-right"]
    for i, c in enumerate(raw_clauses[:5]):
        c = c.strip()
        if not c:
            continue
        # Convert imperative show/add/render/offer into descriptive sentences
        if c.lower().startswith("show "):
            c = "the diagram shows " + c[5:]
        elif c.lower().startswith("add "):
            c = "the diagram also includes " + c[4:]
        elif c.lower().startswith("render "):
            c = "the diagram renders " + c[7:]
        elif c.lower().startswith("offer "):
            c = "the diagram offers " + c[6:]
        # Ensure the clause begins with a lowercase word when it follows an intro
        c = c[0].lower() + c[1:]
        intro = positions[min(i, len(positions) - 1)] + ", "
        pieces.append(intro + c + ".")
    if len(labels) >= 2:
        pieces.append(f"The eye travels from **{labels[0]}** through the central flow to **{labels[-1]}**, with the contrast between coral risk paths and teal recovery paths giving the reader the core message at a glance.")
    return " ".join(pieces)


def color_and_flow(prompt, labels, grammar):
    # Detect explicit coral/teal labels (case-sensitive on the uppercase label)
    coral_re = re.findall(r"coral\s+([A-Z][A-Z0-9\s\-/]+)", prompt)
    teal_re = re.findall(r"teal\s+([A-Z][A-Z0-9\s\-/]+)", prompt)
    coral_labels = [tidy(c) for c in coral_re]
    teal_labels = [tidy(c) for c in teal_re]
    paragraphs = ["The course visual grammar applies directly to this diagram."]
    # Cobalt
    platform = labels[0] if labels else "the main workspace"
    paragraphs.append(f"- **Cobalt platform** — {grammar.get('cobaltPlatform', 'a bounded product region')}. Here the cobalt surface under **{platform}** and the surrounding workspace frames the product boundary; it tells the reader that this is a bounded product region, not an uncontrolled chat surface. It marks the product's responsibility to keep the user's workspace distinct from raw model output or runtime internals.")
    # Cyan
    paragraphs.append(f"- **Cyan arrow** — {grammar.get('cyanArrow', 'a typed event or navigation path')}. Cyan arrows carry the flow of events, updates, and proposals from left to right, linking the typed cards and records to the reducer or next gate. When the reader sees cyan, they should expect a deliberate, validated transition rather than an accidental or hidden connection.")
    # Teal
    if teal_labels:
        paragraphs.append(f"- **Teal arrow** — {grammar.get('tealArrow', 'an authoritative or consented path')}. The teal **{'**, **'.join(teal_labels[:3])}** path shows the safe, authoritative, and consented route through the diagram. This color tells the reader that the product has enough evidence and authority to proceed safely.")
    else:
        paragraphs.append(f"- **Teal arrow** — {grammar.get('tealArrow', 'an authoritative or consented path')}. Teal marks the authoritative and safe path, such as the committed receipt or restored state, distinguishing it from the raw request. This color tells the reader that the product has enough evidence and authority to proceed safely.")
    # Coral
    if coral_labels:
        paragraphs.append(f"- **Coral path** — {grammar.get('coralPath', 'a conflict or risk path')}. The coral **{'**, **'.join(coral_labels[:3])}** path shows the risk, conflict, or blocked outcome the product must prevent. It signals that the product should pause, surface the conflict, and offer a recovery path rather than proceed silently.")
    else:
        paragraphs.append(f"- **Coral path** — {grammar.get('coralPath', 'a conflict or risk path')}. Coral marks the conflict, stale state, or blocked action that appears when a control is missing or bypassed. It signals that the product should pause, surface the conflict, and offer a recovery path rather than proceed silently.")
    # White card
    card_labels = [l for l in labels if any(k in l for k in ["CARD", "RECEIPT", "ARTIFACT", "EVENT", "PROPOSAL", "RECORD"])][:4]
    if card_labels:
        paragraphs.append(f"- **White card** — {grammar.get('whiteCard', 'a structured record or proposal')}. **{'**, **'.join(card_labels)}** appear as white cards, showing that they are records, proposals, or evidence rather than raw data or system internals. The white background separates user-meaningful records from raw system logs or generated text.")
    else:
        paragraphs.append(f"- **White card** — {grammar.get('whiteCard', 'a structured record or proposal')}. The labeled cards and records throughout the diagram are white, marking them as structured events, proposals, receipts, or recovery options. The white background separates user-meaningful records from raw system logs or generated text.")
    # overall flow
    paragraphs.append("The overall flow moves from the initiating actor or request, through validation and reduction, toward either the teal recovery or completion path or the coral failure path. The color of each arrow and card is a trust cue, not a decoration.")
    return "\n\n".join(paragraphs)


def how_to_present(lesson, prompt_labels, trace, case_study, analogy, lab, checkpoint):
    bullets = []
    situation = case_study.get('situation', 'Maya is interacting with the agent')
    short_sit = re.split(r"[.!?]", situation)[0].strip() if situation else 'Maya is interacting with the agent'
    bullets.append(f"**Start with the user moment.** {short_sit}. Ask the room what they need to see to feel in control. Invite someone to describe the moment before any solution appears.")
    if prompt_labels:
        bullets.append(f"**Point at {prompt_labels[0]} and ask what it represents.** Then trace the flow from there through the next two or three elements, naming the color and direction of each arrow. Encourage them to name the incoming trigger, the visible state, and the decision the product must make.")
    # bullets per trace step, tied to a label
    for i, step in enumerate(trace):
        lab_for_step = relevant_labels(step, prompt_labels, n=1)
        target = lab_for_step[0] if lab_for_step else (prompt_labels[i % len(prompt_labels)] if prompt_labels else "the diagram")
        bullets.append(f"**Point at {target} for step {i+1}.** {title_case(shorten_heading(step))}. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.")
    # Analogy
    if analogy:
        bullets.append(f"**Use the analogy.** {analogy} Draw the parallel to the diagram and ask what would break if the two situations were handled the same way.")
    # Case
    sit = case_study.get('situation', '')
    short_sit = re.split(r"[.!?]", sit)[0].strip() if sit else ''
    bullets.append(f"**Tell the case study.** {short_sit} Walk through the walkthrough and stop at the moment the old design would have failed. Pause at the step where the old design would have failed and ask how the new interface prevents it.")
    # Lab
    bullets.append(f"**Run the lab.** {lab} Ask pairs to present one part of the diagram and explain how the other parts reference it without merging their identities.")
    # Checkpoint
    bullets.append(f"**Pose the checkpoint.** {lesson.get('checkpoint', '')} Let the room answer before confirming the principle. Collect answers, then confirm the principle and note any exceptions the team should watch for.")
    # Takeaway close
    bullets.append(f"**Close on the contract.** {lesson.get('caseStudy', {}).get('takeaway', lesson.get('outcome', ''))} Ask the team what their own product's equivalent of the contract would be.")
    # Trim or expand to 6-12
    if len(bullets) < 6:
        bullets.append("**Ask which current interface the team would have to rebuild to match this diagram.** The answer reveals how deeply prose parsing is baked into the product.")
    if len(bullets) > 12:
        bullets = bullets[:12]
    return "\n\n".join(f"- {b}" for b in bullets)


def at_a_glance(lesson, prompt_labels, prompt, case_study):
    lines = []
    outcome = lesson.get("outcome", "")
    lines.append(f"**{outcome}**")
    # Takeaways from labels and prompt
    take = []
    if prompt_labels:
        take.append(f"The diagram centers on **{prompt_labels[0]}** and its relationship to **{prompt_labels[-1]}**.")
    # Coral/teal observation (case-sensitive on the label so we capture only uppercase labels)
    coral = re.findall(r"coral\s+([A-Z][A-Z0-9\s\-/]+)", prompt)
    teal = re.findall(r"teal\s+([A-Z][A-Z0-9\s\-/]+)", prompt)
    if teal:
        names = [tidy(t) for t in teal[:2]]
        take.append(f"The teal **{'**, **'.join(names)}** path shows the safe, authoritative, or consented route.")
    if coral:
        names = [tidy(t) for t in coral[:2]]
        take.append(f"The coral **{'**, **'.join(names)}** path shows the risk the product must prevent.")
    if not teal and not coral:
        take.append(f"The diagram separates the tested, legitimate flow from failure paths that must fail closed.")
    sit = case_study.get("situation", "")
    if sit:
        take.append(f"Maya's case: {sit}")
    lines.extend(f"- {t}" for t in take[:4])
    return "\n\n".join(lines)


def build_sources(lesson, official_map):
    srcs = lesson.get("sources", [])
    if not srcs:
        return ""
    lines = []
    for s in srcs:
        url = official_map.get(s)
        if url:
            lines.append(f"- [{s}]({url})")
        else:
            lines.append(f"- {s}")
    return "\n".join(lines)


def build_related(lesson, lessons_by_id):
    related = lesson.get("related", [])
    if not related:
        return ""
    lines = ["## Related lessons", ""]
    for rid in related:
        other = lessons_by_id.get(rid, {})
        if other:
            lines.append(f"- Diagram {rid} — {other.get('title', '')}")
        else:
            lines.append(f"- Diagram {rid}")
    lines.append("")
    lines.append("---")
    return "\n".join(lines)


def synthesis_body(lesson, prompt_labels, case_study):
    outcome = lesson.get("outcome", "")
    danger = case_study.get("danger", "")
    takeaway = case_study.get("takeaway", "")
    anchors = ", ".join(f"**{l}**" for l in prompt_labels[:3]) if prompt_labels else "the central elements"
    parts = [
        f"The lesson is not a perfect prototype; it is a product contract. {outcome}.",
        f"The diagram makes that contract visible through {anchors}, so the team can argue about the contract before choosing a framework.",
        "The contract is not framework-specific; it is the set of observable promises the product makes to the person using it.",
    ]
    if danger:
        d = danger.strip(".")
        if d and d[0].isupper():
            d = d[0].lower() + d[1:]
        parts.append(f"Maya's case warns that {d}.")
    if takeaway:
        parts.append(f"The practical standard is this: {takeaway}")
    return " ".join(parts)


def build_what_diagram_teaches(lesson, prompt_labels, explanation, trace, nextjs, python, analogy, case_study):
    assigned, leftover = assign_sentences(trace, explanation)
    sections = []

    # Concept subsections from first/second half of explanation
    halves = []
    if leftover:
        mid = len(leftover) // 2 if len(leftover) > 1 else 1
        halves = [leftover[:mid], leftover[mid:]]
    else:
        # Use explanation itself split in half
        sents = split_sentences(explanation)
        if len(sents) >= 2:
            mid = len(sents) // 2
            halves = [sents[:mid], sents[mid:]]

    for ci, half in enumerate(halves[:2]):
        body = concept_body(half, prompt_labels, case_study, lesson.get("outcome"), lesson.get("title"), ci)
        if not body:
            continue
        heading = shorten_heading(half[0])
        sections.append((title_case(heading), body))

    # Trace step subsections
    for i, step in enumerate(trace):
        heading = shorten_heading(step)
        body = trace_body(step, assigned.get(i, []), prompt_labels, case_study, i, lesson.get("title"))
        sections.append((title_case(heading), body))

    # Synthesis: a closing conceptual section that ties the diagram to the case study
    sections.append(("The standard in practice", synthesis_body(lesson, prompt_labels, case_study)))

    # Next.js and Python
    if nextjs and python:
        sections.append(("The Next.js and Python surfaces", nextjs_python_body(nextjs, python, prompt_labels, case_study)))
    elif nextjs:
        sections.append(("The Next.js surface", stack_body(nextjs, "Next.js / React", prompt_labels, case_study)))
    elif python:
        sections.append(("The Python surface", stack_body(python, "Python / FastAPI", prompt_labels, case_study)))

    # Analogy
    if analogy:
        sections.append(("Analogy", analogy_body(analogy, prompt_labels, case_study)))

    # Ensure word count by expanding if needed (see main loop)
    return sections


def nextjs_python_body(nextjs, python, prompt_labels, case_study):
    parts = []
    parts.append("The same contract appears in both stacks, but the boundary moves with the architecture.")
    parts.append("**In Next.js / React:**")
    for item in nextjs:
        parts.append(f"- {item}")
    parts.append("- Keep the most sensitive payloads and policy decisions on the server and stream only user-visible, safe view models to client components.")
    parts.append("**In Python / FastAPI:**")
    for item in python:
        parts.append(f"- {item}")
    parts.append("- Treat every framework callback or protocol event as raw input; validate and transform it into the product's own event vocabulary before it reaches the reducer or domain model.")
    danger = case_study.get("danger", "")
    if danger:
        parts.append(f"Both implementations must avoid the same trap: {danger[0].lower() + danger[1:] if danger[0].isupper() else danger}")
    return "\n".join(parts)


def stack_body(items, name, prompt_labels, case_study):
    parts = [f"In the {name} stack, the diagram becomes enforceable code."]
    for item in items:
        parts.append(f"- {item}")
    return "\n".join(parts)


def analogy_body(analogy, prompt_labels, case_study):
    parts = [analogy]
    parts.append(f"The analogy keeps the lesson grounded. The diagram's **{prompt_labels[0] if prompt_labels else 'main element'}** plays the same role as the central object in the analogy: it must be visible, labeled, and trustworthy without the user having to infer meaning from a long narrative.")
    parts.append("The parallel works because both situations require separating the object from the record, the attempt from the proof, and the promise from the evidence.")
    return " ".join(parts)


def layout_summary(prompt, prompt_labels):
    """Create a concise, positional one-sentence layout from the prompt."""
    clauses = [c.strip() for c in re.split(r"[.!?;]", prompt) if c.strip()]
    if not clauses:
        return tidy(prompt)[:160]
    first = clauses[0]
    # Convert Show to The diagram shows, etc.
    if first.lower().startswith("show "):
        first = "The diagram shows " + first[5:]
    # Add a brief note about the explicit color paths if they exist
    extras = []
    if re.search(r"\bcoral\b", prompt, re.I):
        extras.append("with a coral risk path")
    if re.search(r"\bteal\b", prompt, re.I):
        extras.append("and a teal safe path")
    summary = tidy(first)
    if extras:
        summary = f"{summary.rstrip('.')}, {', '.join(extras)}."
    if len(summary) > 180:
        summary = summary[:177].rsplit(" ", 1)[0] + "..."
    return summary


def render_markdown(lesson, module, prompt_data, course_data, lessons_by_id):
    lid = lesson["id"]
    slug = lesson["slug"]
    title = lesson["title"]
    outcome = lesson.get("outcome", "")
    explanation = lesson.get("explanation", "")
    trace = lesson.get("trace", [])
    nextjs = lesson.get("nextjs", [])
    python = lesson.get("python", [])
    analogy = lesson.get("analogy", "")
    case = lesson.get("caseStudy", {})
    lab = lesson.get("lab", "")
    checkpoint = lesson.get("checkpoint", "")
    answer = lesson.get("answer", "")
    glossary = lesson.get("glossary", [])
    related = lesson.get("related", [])

    prompt = prompt_data[lid]["prompt"] if lid in prompt_data else lesson.get("diagramPrompt", "")
    alt = lesson.get("alt", prompt_data.get(lid, {}).get("alt", ""))

    prompt_labels = extract_labels(prompt)

    # Module title
    module_title = module.get("title", "") if module else ""

    # Role in the course: use outcome if short, else stability
    role = outcome
    if words(role) > 25:
        role = lesson.get("stability", outcome)

    # Layout from prompt
    layout = layout_summary(prompt, prompt_labels)

    sections = build_what_diagram_teaches(lesson, prompt_labels, explanation, trace, nextjs, python, analogy, case)

    # Build element list
    element_items = []
    for label in prompt_labels:
        desc = describe_label(label, prompt, outcome, title, prompt_labels)
        element_items.append(f"- **{label}** — {desc}")

    official_map = {s["label"]: s["url"] for s in course_data.get("officialSources", [])}

    parts = []
    parts.append(f"# Diagram {lid} — {title}")
    parts.append("")
    parts.append(f"![{alt}](../diagrams/{lid:03d}-{slug}.png)")
    parts.append("")
    parts.append(f"**Module:** {module_title}")
    parts.append(f"**Role in the course:** {role}")
    parts.append(f"**Layout:** {layout}")
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append("## At a glance")
    parts.append("")
    parts.append(at_a_glance(lesson, prompt_labels, prompt, case))
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append("## What the diagram teaches")
    parts.append("")
    for i, (heading, body) in enumerate(sections, 1):
        parts.append(f"### {i}. {heading}")
        parts.append("")
        parts.append(body)
        parts.append("")
    parts.append("---")
    parts.append("")
    parts.append(f"## Case study — {case.get('name', 'Maya')}")
    parts.append("")
    parts.append(case.get("situation", ""))
    parts.append("")
    parts.append("### The walkthrough")
    parts.append("")
    for i, w in enumerate(case.get("walkthrough", []), 1):
        parts.append(f"{i}. {w}")
    parts.append("")
    parts.append("### The result")
    parts.append("")
    parts.append(case.get("result", ""))
    parts.append("")
    parts.append("### The danger")
    parts.append("")
    parts.append(case.get("danger", ""))
    parts.append("")
    parts.append("### The takeaway")
    parts.append("")
    parts.append(case.get("takeaway", ""))
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append("## Composition")
    parts.append("")
    parts.append(composition_paragraph(prompt, prompt_labels, title))
    parts.append("")
    parts.append("## Element by element")
    parts.append("")
    parts.append("\n".join(element_items))
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append("## Colour and flow semantics")
    parts.append("")
    parts.append(color_and_flow(prompt, prompt_labels, course_data.get("visualGrammar", {})))
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append("## How to present it")
    parts.append("")
    parts.append(how_to_present(lesson, prompt_labels, trace, case, analogy, lab, checkpoint))
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append("## Lab and checkpoint")
    parts.append("")
    parts.append(f"**Lab:** {lab}")
    parts.append("")
    parts.append(f"**Checkpoint:** {checkpoint}")
    parts.append("")
    parts.append(f"**Answer:** {answer}")
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append("## Glossary")
    parts.append("")
    for item in glossary:
        if " - " in item:
            term, defin = item.split(" - ", 1)
            parts.append(f"- **{term}** — {defin}")
        elif " — " in item:
            term, defin = item.split(" — ", 1)
            parts.append(f"- **{term}** — {defin}")
        else:
            parts.append(f"- {item}")
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append("## Sources")
    parts.append("")
    parts.append(build_sources(lesson, official_map))
    parts.append("")
    if related:
        parts.append(build_related(lesson, lessons_by_id))
    else:
        parts.append("---")
    return "\n".join(parts)


def expand_if_short(lesson, sections, prompt_labels, case, outcome):
    # If the rendered article would be short, add additional conceptual and present-it bullets.
    # This is a place to inject more specific detail when the generator is terse.
    extra = []
    if len(sections) < 9:
        extra.append((
            title_case(shorten_heading("What goes wrong when the product confuses interface state with business authority")),
            f"The diagram keeps interface state and business authority in separate lanes for a reason. **{prompt_labels[0] if prompt_labels else 'The central element'}** can update the screen quickly, but it cannot commit a payment, send a refund, or approve an exception until the **authoritative server** returns a durable receipt. If the product lets a local animation or optimistic label grant the same authority as a committed record, the interface becomes a source of false evidence. This is the same failure the case study warns about: {case.get('danger', 'the interface can look right while the underlying state is wrong')}. The antidote is to show prediction as prediction, evidence as evidence, and effect only after a receipt."
        ))
    if len(sections) < 10:
        extra.append((
            title_case(shorten_heading("The event contract is a product contract, not a protocol detail")),
            f"Every protocol adapter, framework callback, and model output is a source of raw data; the product owns the typed vocabulary that appears on screen. That means schemas, ordering rules, version fields, privacy rules, and unknown-event behavior must be documented and tested before a designer draws a single component. {outcome}. If the team treats the protocol as the contract, a renamed field or a new framework version can silently break the interface. The diagram forces the team to name the product event types, the regions they update, and the recovery behavior when an event is late, duplicate, or invalid."
        ))
    return extra


def main():
    raw = load_json(JSON_PATH)
    course = raw["course"]
    modules = {m["id"]: m for m in raw.get("modules", [])}
    lessons = {l["id"]: l for l in raw.get("lessons", [])}
    prompt_data = parse_prompt_library(PROMPT_LIB)
    official_map = {s["label"]: s["url"] for s in course.get("officialSources", [])}

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    report = []
    for lid in range(197, 221):
        lesson = lessons.get(lid)
        if not lesson:
            report.append(f"Lesson {lid} not found")
            continue
        module = modules.get(lesson.get("moduleId"))
        md = render_markdown(lesson, module, prompt_data, course, lessons)
        # Expand if needed
        prompt = prompt_data.get(lid, {}).get("prompt", lesson.get("diagramPrompt", ""))
        prompt_labels = extract_labels(prompt)
        if words(md) < WORD_TARGET:
            # simplistic expansion: no further in this pass; we will warn
            pass
        path = OUT_DIR / f"{lid:03d}-{lesson['slug']}.md"
        path.write_text(md, encoding="utf-8")
        report.append(f"{path.name}: {words(md)} words")

    print("\n".join(report))


if __name__ == "__main__":
    main()
