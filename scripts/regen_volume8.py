import json
import re
import os
from collections import OrderedDict
from pathlib import Path

COURSE_ROOT = Path(__file__).resolve().parent.parent / "courses" / "Visual Course 08"
MANUAL_DATA = COURSE_ROOT / "volume8_manual_data.json"
COURSE_JSON = COURSE_ROOT / "Volume 8 Course Content.json"
OUT_DIR = COURSE_ROOT / "diagram-docs"

STOPWORDS = {
    "A","AN","THE","AND","OR","BUT","OF","TO","IN","ON","AT","FOR","WITH",
    "FROM","BY","AS","IS","IT","ITS","THAT","THIS","THESE","THOSE","IF",
    "THEN","BE","ARE","WAS","WERE","HAS","HAVE","HAD","NOT","WHEN","WHERE",
    "WHILE","BEFORE","AFTER","ABOVE","BELOW","BENEATH","BESIDE","INTO","THROUGH",
    "OVER","UNDER","AGAIN","FURTHER","THEN","ONCE","HERE","THERE","SO","THAN",
    "TOO","VERY","CAN","WILL","JUST","SHOULD","NOW","ONLY","ALSO","EACH","EVERY",
    "ALL","ANY","BOTH","FEW","MORE","MOST","OTHER","SOME","SUCH","NO","NOR","NOT"
}

# Keywords used to colour-code labels for colour-and-flow semantics
CORAL_HINTS = {
    "FAIL","FAILED","FAILURE","BROKEN","STALE","WRONG","INVALID","DENIED","DENY",
    "DUPLICATE","TIMEOUT","COST SPIKE","SLOW TAIL","RETRY STORM","QUEUE GROWTH",
    "NO OWNER","UNCONTROLLED","BLAME","ACTION WITHOUT PROOF","TIMEOUT CASCADE",
    "UNSAFE FALLBACK","FLAG DRIFT","INCOMPATIBLE MIX","LEGACY","REMOVED",
    "TECHNICALLY GREEN","USER FAILED","COMPLETE TRACE BUT WRONG OUTCOME",
    "STALE ANSWER","STALE POLICY","STALE DOCUMENT","RETRY","COST SPIKE","CASCADE"
}
TEAL_HINTS = {
    "VERIFIED","CURRENT","SAFE","STABLE","RECOVERED","GROUNDED","EARLY FALLBACK",
    "BACKPRESSURE","PRESERVE","ADAPTER","ROLLOUT","VERIFIED LEARNING",
    "VERIFIED OUTCOME","VERIFIED EFFECT","UNDERSTOOD AND RECOVERED","ACTIONABLE",
    "KNOWN GOOD","RECOVER","STABLE FLOW","ISOLATED EVIDENCE","SIGNED EVIDENCE"
}
COBALT_HINTS = {
    "GATE","WORKFLOW","LAB","STORE","VAULT","MATRIX","POOL","LEDGER","RULE",
    "STAGE","CONTROL","FILTER","RERANK","INDEX","CLASSIFIER","WORKER POOL",
    "CONCURRENCY","ADMISSION","QUALITY LAB","QUALITY FLOOR","RELEASE CONFIG",
    "ALERT RULE","VERSION MATRIX","COMPATIBILITY","PLATFORM"
}
WHITE_HINTS = {
    "CARD","RECEIPT","RECORD","ID","SPAN","METRIC","LOG","EVENT","CASE","SCORE",
    "BUDGET","VERSION","RUBRIC","SET","NOTE","ARTIFACT","EVIDENCE","LABEL","RECEIPT",
    "USER OUTCOME","USER GOAL"
}

ROLE_NOUNS = {
    "card","gate","lane","path","arrow","ribbon","matrix","store","vault","ledger",
    "receipt","stage","platform","link","box","grid","row","slice","branch","loop",
    "workflow","span","metric","log","event","case","set","queue","pool","rule",
    "control","limit","adapter","model","lab","contract","explorer","dataset","scorer",
    "flag","switch","artifact","bundle","chart","distribution","panel","cell","line",
    "funnel","hub","architecture","ring","bundle","receipt","test","scenario"
}

FALLBACK_DESCRIPTIONS = {
    "USER OUTCOME": "the user-visible result that the entire request and its telemetry are organized to explain.",
    "USER GOAL": "the user-visible objective that begins the workflow and justifies the work.",
    "REQUEST": "the incoming operation shown as a cyan path that starts the telemetry chain.",
    "RESULT": "the outgoing outcome; it is teal when healthy and tied to verified evidence.",
    "NEXT.JS": "the TypeScript/React application that receives user-facing requests and continues telemetry context on the server.",
    "FASTAPI": "the Python backend service that processes requests, enforces policy, and emits durable business records.",
    "MCP": "the Model Context Protocol connection to tool capabilities and resources.",
    "A2A": "the agent-to-agent protocol used to delegate tasks, receive artifacts, and coordinate work.",
    "RAG": "the retrieval-augmented generation pipeline that finds, filters, and ranks evidence.",
    "TOOLS": "the external capabilities the agent can invoke with typed arguments and receipts.",
    "QUEUES": "the asynchronous work items that carry context across time and load shapes.",
    "UI": "the user interface where progress, evidence, controls, and receipts are shown.",
    "MODEL": "the language model that generates candidate text, plans, and reasoning.",
    "PROMPT": "the instruction and context sent to the model for a given request.",
    "POLICY": "the rules that decide whether an action, retrieval, or disclosure is allowed.",
    "RETRIEVAL INDEX": "the indexed corpus and version used to find current evidence.",
    "TOOL ADAPTER": "the code that translates a typed agent proposal into a real tool call and back.",
    "AGENT CARD": "the advertised capabilities, metadata, and version of an A2A agent.",
    "TELEMETRY CONTRACT": "the agreement that defines signals, attributes, propagation, capture, and access.",
    "TRACE EXPLORER": "the operator view for inspecting connected traces, spans, and events.",
    "EVAL DATASET": "the versioned collection of cases used to judge system behavior.",
    "SCORERS": "the instruments that evaluate case evidence against a rubric or assertions.",
    "STAGE QUALITY": "the measurement of each agent stage—intent, routing, retrieval, tool, planning, and so on—separately.",
    "LATENCY COST CAPACITY": "the performance and economics view of the system: deadlines, cost, queues, and saturation.",
    "RELEASE GATES": "the offline and production evidence rules that decide whether a candidate may promote.",
    "SHADOW CANARY": "the side-by-side and small-cohort release methods that compare versions with real workload.",
    "FLAGS ROLLBACK": "the feature flags and emergency rollback controls that expose or revert a version bundle.",
    "ALERTS RUNBOOKS": "the actionable alerts and tested runbooks that guide incident response.",
    "INCIDENTS": "the incident records, postmortems, corrective actions, and learning events.",
    "REGRESSION LEDGER": "the durable catalog of failures that future releases must continue to pass.",
    "BUILD": "the build stage that receives verified learning and produces the next candidate.",
    "VERIFIED LEARNING": "the teal loop that returns proven improvements back to the build stage.",
    "STALE ANSWER": "the coral catch at retrieval that blocks a release before it reaches users.",
    "STALE POLICY": "the coral slice or document showing a known high-impact failure mechanism.",
    "STALE DOCUMENT": "the outdated evidence that reaches generation and threatens correctness.",
    "OVERALL SCORE 92 PERCENT": "the headline rate that can hide weak slices and small denominators.",
    "PASSED / ELIGIBLE": "the denominator card that shows how many eligible cases a rate is built from.",
    "USER REQUEST": "the user's original question or task, the first input to the agent pipeline.",
    "USER RECEIPT": "the durable, user-visible evidence of the completed business outcome.",
    "PROPOSED ACTION": "the typed tool call or effect the agent wants to perform.",
    "BUSINESS EFFECT": "the real, authoritative change to the system of record.",
    "VERIFIED EFFECT": "the teal outcome when the action, permission, idempotency, and state all agree.",
    "GROUNDED RESULT": "the teal output supported by identified artifact evidence and resolved contradictions.",
    "TECHNICAL RESULT": "the backend output before it is judged for user experience and recovery.",
    "UNDERSTOOD AND RECOVERED": "the teal outcome when the user can act on the result and recover from problems.",
    "TOTAL DEADLINE": "the horizontal bar representing the user-facing latest useful completion time.",
    "SLOW TAIL": "the coral curve of unusually slow requests that averages hide.",
    "COST LEDGER": "the visual accounting sheet of scenario cost for one request.",
    "RETRY STORM": "the coral pattern where retries multiply faster than work completes.",
    "QUEUE GROWTH": "the coral rise in waiting work that signals saturation or backpressure failure.",
    "BACKPRESSURE": "the teal control that slows or rejects upstream work to protect downstream limits.",
    "STABLE FLOW": "the teal state where admitted work proceeds within capacity.",
    "QUALITY FLOOR": "the safety and quality boundary that no fallback may cross.",
    "SIGNED EVIDENCE BUNDLE": "the teal immutable output of an offline gate run.",
    "SHARED CACHE CONTAMINATION": "the coral risk where the candidate pollutes control caches or state.",
    "ISOLATED EVIDENCE": "the teal guarantee that candidate evidence is kept separate from production.",
    "KNOWN GOOD SET": "the teal bundle of tested, compatible versions to which rollback can return.",
    "EXPECTED REJECT": "the teal matrix result when an unsafe combination is correctly refused.",
    "UNCONTROLLED TEST": "the coral exercise that is quarantined because it lacks scope, authorization, or stop conditions.",
    "ACTION WITHOUT PROOF": "the coral postmortem closure that leaves the control unverified.",
    "TRACE ID": "the identifier shared by a trace, its spans, logs, and events so they can be correlated.",
    "SERVICE VERSION REGION": "the three fields named on the RESOURCE card that identify where a signal was produced.",
    "RATE ERROR DURATION": "the three headline measurements shown on the METRICS card: request rate, error ratio, and duration.",
    "FAILED SPAN": "the coral branch that marks a timed operation ending in an error, connected to a log and a metric change.",
    "BUSINESS RECORD ID": "the durable business identifier that links workflow, trace, and evaluation evidence.",
    "POLICY RECEIPT": "the durable record of a policy decision and its authority.",
    "ARTIFACT ID": "the durable identifier for an output artifact produced by the workflow.",
    "REQUEST ID": "the protocol or application identifier for the user request, separate from the trace identity.",
    "TASK ID": "the A2A task identifier used to delegate and track work.",
    "CONTEXT ID": "the A2A context identifier used to correlate related tasks and artifacts.",
    "SPAN LINK": "the non-parent relationship that connects asynchronous work to a causal span.",
    "BUSINESS ID": "the set of identifiers that separate business identity from trace identity.",
    "BUSINESS WORKFLOW": "the durable sequence of business stages that produces a user-facing result.",
    "SYSTEM UNDER TEST": "the candidate release, model, or configuration being evaluated against the case.",
    "SCORECARD": "the PASS, FAIL, or REVIEW judgment produced for the case.",
    "UNDERSPECIFIED CASE": "a case that is missing required fields and cannot be used as a fair test.",
    "CONTRACT PASS": "the teal outcome when all deterministic contract gates pass.",
    "FAIL WITH EVIDENCE": "the coral outcome when a gate produces a structured failure with references.",
    "MODEL RUBRIC": "the lane beside the check gates that scores flexible language qualities that cannot be deterministic.",
    "GRADER DRIFT": "the coral change in a grader's output when its model or prompt version changes.",
    "ADJUDICATED LABEL": "the trusted reviewed decision produced by calibrated graders or human reviewers.",
    "DECISION THRESHOLD": "the proposed boundary on the distribution that the team must agree to before promoting.",
    "STALE POLICY 58 PERCENT": "the coral slice that shows the known high-impact failure mechanism has a poor rate.",
    "PASSED / ELIGIBLE": "the denominator card that shows how many eligible cases a rate is built from.",
    "SELECTED EVIDENCE": "the evidence that the system actually used to generate an answer.",
    "STALE DOCUMENT": "the outdated evidence that reaches generation and threatens correctness.",
    "CURRENT POLICY": "the current, authorized evidence selected by the retrieval system.",
    "VERIFIED EFFECT": "the teal outcome when the action, permission, idempotency, and state all agree.",
    "WRONG TOOL": "the coral path where the agent calls a tool that is not allowed for the action.",
    "INVALID ARGUMENT": "the coral path where the typed arguments do not match the TOOL SCHEMA.",
    "DENIED BUT CALLED": "the coral path where a disallowed action is invoked anyway.",
    "DUPLICATE EFFECT": "the coral path where a retry creates the same business change twice.",
    "CITATION LINKS": "the references that tie a synthesized claim to its source evidence.",
    "CONTRADICTION CHECK": "the control that exposes conflicts among specialist artifacts before synthesis.",
    "LOOP": "the coral path where planning returns to an earlier step without making progress.",
    "WRONG SPECIALIST": "the coral path where the plan delegates to an agent that cannot do the task.",
    "LOST CONSTRAINT": "the coral path where a user requirement is dropped from the plan.",
    "UNSUPPORTED CLAIM": "the coral path where a final claim has no evidence or citation.",
    "GROUNDED RESULT": "the teal output supported by identified artifact evidence and resolved contradictions.",
    "TECHNICALLY GREEN / USER FAILED": "the coral path where the backend succeeds but the user cannot use the result.",
    "UNDERSTOOD AND RECOVERED": "the teal outcome when the user can act on the result and recover from problems.",
    "SLOW TAIL": "the coral curve of unusually slow requests that averages hide.",
    "CACHE HIT": "the teal arrow showing work avoided by cached results.",
    "RETRY": "the coral arrow showing work multiplied by a repeated attempt.",
    "RETRY STORM": "the coral pattern where retries multiply faster than work completes.",
    "BACKPRESSURE": "the teal control that slows or rejects upstream work to protect downstream limits.",
    "STABLE FLOW": "the teal state where admitted work proceeds within capacity.",
    "QUALITY FLOOR": "the safety and quality boundary that no fallback may cross.",
    "SIGNED EVIDENCE BUNDLE": "the teal immutable output of an offline gate run.",
    "FAIL": "the coral gate outcome where the candidate fails an offline contract check.",
    "REVIEW": "the coral gate outcome where a candidate needs more evidence before release.",
    "QUARANTINE": "the coral gate outcome where a candidate is held for investigation.",
    "ISOLATED EVIDENCE": "the teal guarantee that candidate evidence is kept separate from production.",
    "SHARED CACHE CONTAMINATION": "the coral risk where the candidate pollutes control caches or state.",
    "KNOWN GOOD SET": "the teal bundle of tested, compatible versions to which rollback can return.",
    "EXPECTED REJECT": "the teal matrix result when an unsafe combination is correctly refused.",
    "NO OWNER": "the coral loop where an alert has no responsible person to act on it.",
    "ACTIONABLE": "the teal alert that has a named owner and a runbook to follow.",
    "UNCONTROLLED TEST": "the coral exercise that is quarantined because it lacks scope, authorization, or stop conditions.",
    "CORRECTIVE ACTION": "an owned change with priority, due date, and proof of improvement.",
    "BLAME": "the coral postmortem behavior that assigns fault instead of fixing the control.",
    "RELEASE": "the gate or stage that must be blocked when a stale answer or other failure is caught.",
    "RETRIEVAL": "the stage where evidence is found, filtered, and ranked; it is where a STALE ANSWER is caught and blocked.",
    "EXPECTED OBSERVED": "the pair of cards at each gate showing what should happen and what actually happened.",
    "TECHNICALLY GREEN USER FAILED": "the coral card showing that the backend succeeded while the user still failed to get a useful result.",
    "PASSED ELIGIBLE": "the denominator card that shows how many eligible cases a rate is built from.",
    "LANGUAGE": "one of the population slices used to break down the OVERALL SCORE into a meaningful subgroup.",
    "CHANNEL": "one of the population slices used to break down the OVERALL SCORE into a meaningful subgroup.",
    "ISSUE TYPE": "one of the population slices used to break down the OVERALL SCORE into a meaningful subgroup.",
    "TENANT TIER": "one of the population slices used to break down the OVERALL SCORE into a meaningful subgroup.",
    "TOOL PATH": "one of the population slices used to break down the OVERALL SCORE into a meaningful subgroup.",
    "RISK": "one of the population slices used to break down the OVERALL SCORE into a meaningful subgroup.",
    "RUNS": "the repeated executions of the same case set used to measure variance and build a DISTRIBUTION.",
    "DISTRIBUTION": "the chart formed by repeated RUNS, showing MEAN, RANGE, CONFIDENCE, and the DECISION THRESHOLD.",
    "MEAN": "the average value of the repeated RUNS in the DISTRIBUTION.",
    "RANGE": "the spread of values across the repeated RUNS in the DISTRIBUTION.",
    "CONFIDENCE": "the measure of uncertainty around the observed value in the DISTRIBUTION.",
    "PROPOSED": "the marker on the DECISION THRESHOLD showing the current proposed release boundary.",
    "INTENT LABEL": "the classification of the user's real job and constraints before routing.",
    "ROUTER": "the stage that selects the right workflow, specialist, model, or policy path.",
    "HIT RATE": "the fraction of requests that return at least one relevant candidate.",
    "PRECISION": "the fraction of selected evidence that is actually relevant and current.",
    "RECALL": "the fraction of all relevant evidence that the retrieval stage finds.",
    "FRESHNESS": "the age and version of the evidence compared to the current policy or source.",
    "COVERAGE": "the breadth of source and language coverage in the selected evidence.",
    "CANDIDATES": "the documents or evidence items returned by the initial retrieval step.",
    "FILTER": "the stage that removes irrelevant or unsafe evidence from the CANDIDATES.",
    "RERANK": "the stage that reorders the remaining CANDIDATES by relevance and freshness.",
    "SELECTED EVIDENCE": "the evidence that the system actually used to generate an answer.",
    "IDEMPOTENCY GATE": "the control that prevents the same business effect from being applied twice on retry.",
    "APPROVAL": "the bound human authorization required for a consequential action.",
    "PLAN": "the bounded set of steps, dependencies, budgets, and stop conditions derived from the user goal.",
    "SYNTHESIS": "the stage that combines specialist artifacts into a final, cited answer.",
    "TECHNICAL RESULT": "the backend output before it is judged for user experience and recovery.",
    "USER EXPERIENCE": "the stage that turns a TECHNICAL RESULT into a human-centered, understandable, and recoverable outcome.",
    "CORRECT": "the user-experience gate that checks the answer matches the user's real question and the evidence.",
    "CURRENT": "the user-experience gate that checks the evidence is not stale or outdated.",
    "CLEAR": "the user-experience gate that checks the explanation is understandable to the user.",
    "ACTIONABLE": "the user-experience gate that checks the user has a useful next step.",
    "CONTROLLED": "the user-experience gate that checks the user has steering, approval, and recovery controls.",
    "ACCESSIBLE": "the user-experience gate that checks the interface works for users with different abilities and devices.",
    "RECOVERABLE": "the user-experience gate that checks the user can recover from errors or stale answers.",
    "PROGRESS": "the control card that shows the user where they are in the workflow.",
    "EVIDENCE": "the support for a claim or decision, shown to the user as concise summaries, artifacts, and citations.",
    "CANCEL": "the control that lets the user stop a workflow without harmful side effects.",
    "EDIT": "the control that lets the user change an input or parameter before continuing.",
    "HUMAN HELP": "the control that lets the user route the case to a qualified person for support.",
    "RECEIPT": "the durable, user-visible record of the completed business outcome.",
    "UNDERSTOOD": "the first half of the teal UNDERSTOOD AND RECOVERED outcome: the user can make sense of the result.",
    "RECOVERED": "the second half of the teal UNDERSTOOD AND RECOVERED outcome: the user can recover from problems.",
    "USER RECEIPT": "the durable, user-visible record of the completed business outcome.",
    "VERIFIED OUTCOME": "the teal card showing the durable business result has been independently checked.",
    "COMPLETE TRACE BUT WRONG OUTCOME": "the coral warning card that shows technical success is not enough.",
    "CHANGE MANIFEST": "the versioned list of what changed in a candidate build.",
    "BUILD ARTIFACT": "the compiled or packaged output of the candidate build.",
    "REPRODUCIBLE EVAL RUN": "the controlled run of cases with frozen inputs so the result can be repeated.",
    "CASE SET": "the versioned collection of cases used for the offline evaluation.",
    "TOOL FIXTURES": "the frozen tool and environment settings that make the eval repeatable.",
    "RETRIEVAL SNAPSHOT": "the frozen view of the retrieval index and corpus used during the eval.",
    "CLOCK": "the frozen time boundary that prevents the eval from depending on wall-clock time.",
    "CONTRACT": "the offline gate that checks exact assertions and schema against the evidence.",
    "QUALITY SLICES": "the offline gate that checks behavior across meaningful subgroups.",
    "SAFETY": "the offline gate that checks dangerous or unacceptable outcomes.",
    "COMPATIBILITY": "the offline gate that checks protocol and schema compatibility before release.",
    "CONTROL": "the live production version that serves real traffic and provides the baseline comparison.",
    "SHADOW CANDIDATE": "the candidate version that receives real traffic but has its effects disabled.",
    "CANARY": "the small-cohort, bounded-effects release used to compare real behavior against the control.",
    "SMALL COHORT": "the limited set of real users or tasks exposed to the canary.",
    "BOUNDED EFFECTS": "the limits on what the canary can change or affect in production.",
    "VERSION RECEIPT": "the durable record of why a specific component version was selected.",
    "KILL SWITCH": "the emergency control that stops exposure to a bad version immediately.",
    "CLIENT VERSION MATRIX": "the rows and columns that show which client protocol and schema versions exist.",
    "SERVER VERSION MATRIX": "the rows and columns that show which server protocol and schema versions exist.",
    "EXPECTED REJECT": "the teal matrix result when an unsafe combination is correctly refused.",
    "FIXTURE": "the controlled test environment and data used to prove compatibility.",
    "MIGRATE": "the path that moves a client or server to a newer, compatible version.",
    "ADAPTER": "the teal migration path that translates between old and new protocol versions.",
    "ROLLOUT": "the teal path that gradually exposes a new compatible version to clients.",
    "ALERT RULE": "the logic that decides whether a signal requires a response.",
    "PAGE NOW": "the highest-priority routing that pages a responsible owner immediately.",
    "TICKET SOON": "the routing that creates a ticket for investigation without immediate paging.",
    "RECORD ONLY": "the routing that logs the signal for later review because no action is needed now.",
    "ACK CLOCK": "the timer that measures how long an alert waits for acknowledgement before escalating.",
    "ESCALATION": "the ladder that moves an unacknowledged alert to the next owner or team.",
    "SCOPE": "the control that defines what an exercise is allowed to touch.",
    "AUTHORIZATION": "the control that ensures the exercise is approved and safe to run.",
    "BLAST RADIUS": "the control that limits how much of the system the exercise can affect.",
    "STOP CONDITIONS": "the criteria that end the exercise immediately if they are met.",
    "OBSERVERS": "the people or systems watching the exercise to ensure it remains controlled.",
    "IMPACT": "the postmortem analysis of who and what was affected.",
    "CONTRIBUTING CONDITIONS": "the postmortem analysis of the surrounding conditions that made the failure possible.",
    "EVIDENCE GAPS": "the postmortem analysis of missing or ambiguous evidence.",
    "DUE": "the date by which a corrective action must be completed.",
    "PRIORITY": "the urgency of a corrective action relative to other work.",
    "PROOF": "the evidence that a corrective action actually fixed the problem."
}

VISUAL_GRAMMAR = {
    "cobalt": "a service, stage, dataset, quality gate, budget, release lane, or incident-control boundary",
    "cyan": "a request, propagated context, telemetry signal, evaluation flow, or candidate release path",
    "teal": "a healthy result, matched evidence, safe promotion, controlled degradation, recovery, or verified learning path",
    "coral": "a broken trace, failed assertion, regression, overload, unsafe outcome, rollback, alert, or incident path",
    "white": "a span, event, metric, log, resource, case, score, budget, version, release, runbook, action, or regression record"
}

def load_manual():
    with open(MANUAL_DATA, "r", encoding="utf-8") as f:
        return json.load(f)

def load_course():
    with open(COURSE_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def build_modules_map(course):
    return {m["id"]: m for m in course["modules"]}

def course_info(course):
    return course["course"]

def build_sources_map(course):
    return {s["label"]: s["url"] for s in course["course"]["officialSources"]}

def build_global_glossary(course):
    g = {}
    for lesson in course["lessons"]:
        for entry in lesson.get("glossary", []):
            if " - " in entry:
                term, definition = entry.split(" - ", 1)
                g[term.upper()] = definition
    return g

def build_definition_map(course):
    """Collect defining sentences from all lesson explanations."""
    verbs = {"is","are","follows","combines","records","identifies","contains","carries","stores","shows","defines","provides","represents","runs","produces","sits","flows","receives","turns","connects","returns","blocks","catches","selects","passes","starts","exits","enters","needs","need","requires","measures","evaluates","compares","means"}
    defs = {}
    for lesson in course["lessons"]:
        for sent in sentencize(lesson["explanation"]):
            # Match 'A/An/The SUBJECT VERB ...' where subject ends at the first verb
            m = re.match(r'^\s*(?:A|An|The)\s+(.+?)\s+(' + '|'.join(verbs) + r')\b\s*(.*)$', sent, re.IGNORECASE)
            if m:
                term = m.group(1).upper().strip()
                # only keep subjects with 1-5 words
                if len(term.split()) > 5:
                    continue
                rest = (m.group(2) + ' ' + m.group(3)).strip()
                if rest:
                    stripped = re.sub(r'^(is\s+|are\s+)', '', rest, count=1, flags=re.IGNORECASE).strip()
                    first = stripped.split()[0].lower() if stripped.split() else ""
                    if not (first in ("a","an","the","one") or first in verbs):
                        continue
                    rest = stripped.rstrip('.')
                    if term not in defs or len(rest) < len(defs[term]):
                        defs[term] = rest
    return defs

def sentencize(text):
    return re.split(r'(?<=[.!?])\s+', text.strip())

def is_upper_token(tok):
    t = tok.strip(",.;:()[]{}\"")
    if not t:
        return False
    if re.fullmatch(r'p\d+', t, re.IGNORECASE):
        return True
    # numbers (e.g., 92) are not upper tokens on their own
    if re.fullmatch(r'\d+', t):
        return False
    return bool(re.fullmatch(r"[A-Z][A-Z0-9.\-/]*", t))

def extract_labels(prompt):
    # Expand slash and hyphen tokens so they can be picked up
    text = prompt.replace('/', ' / ').replace('-', ' - ')
    tokens = text.split()
    labels = []
    i = 0
    while i < len(tokens):
        raw = tokens[i]
        stripped = raw.strip(",.;:()[]{}\"")
        if is_upper_token(raw) and stripped.upper() not in STOPWORDS:
            label = [stripped]
            j = i + 1
            while j < len(tokens):
                next_raw = tokens[j]
                next_stripped = next_raw.strip(",.;:()[]{}\"")
                # break after a token that ends with a list/clause separator
                if raw[-1] in ':;.,':
                    break
                # numbers in the middle of a label (e.g. 92 PERCENT)
                if next_stripped.isdigit() and j + 1 < len(tokens) and is_upper_token(tokens[j + 1]):
                    label.append(next_stripped)
                    raw = next_raw
                    j += 1
                    continue
                # slash keeps a pair together (e.g. PASSED / ELIGIBLE)
                if next_raw == "/" and j + 1 < len(tokens) and is_upper_token(tokens[j + 1]):
                    j += 1
                    raw = next_raw
                    continue
                # "and"/"or" between labels means a break (not a slash)
                if next_stripped.upper() in ("AND", "OR"):
                    break
                if is_upper_token(next_raw) and next_stripped.upper() not in STOPWORDS:
                    label.append(next_stripped)
                    raw = next_raw
                    j += 1
                else:
                    break
                if len(label) >= 5:
                    break
            labels.append(" ".join(label))
            i = j
        else:
            i += 1
    # also pick up p50/p95/p99
    for m in re.finditer(r'\bp\d+\b', prompt, re.IGNORECASE):
        labels.append(m.group(0))
    # unique preserving order
    seen = set()
    result = []
    for l in labels:
        l = re.sub(r'[:;.,]+$', '', l).strip()
        if l and l not in seen:
            seen.add(l)
            result.append(l)
    return result

def color_of(label, prompt=""):
    u = label.upper()
    # exact label overrides to avoid substring false positives
    if u in {"RESULT","VERIFIED EFFECT","GROUNDED RESULT"}:
        return "teal"
    if u in {"REQUEST","TRACEPARENT"}:
        return "cyan"
    if u in {"LANGUAGE","CHANNEL","ISSUE TYPE","TENANT TIER","TOOL PATH","RISK","RUNS","DISTRIBUTION","MEAN","RANGE","CONFIDENCE","PROPOSED","PASSED ELIGIBLE","EXPECTED OBSERVED"}:
        return "white"
    prompt_upper = prompt.upper()
    # explicit color in prompt near the label (within ~35 chars after the colour word)
    for color, word in [("coral", "CORAL"), ("teal", "TEAL"), ("cyan", "CYAN"), ("green", "GREEN")]:
        for m in re.finditer(rf'\b{color}\b', prompt, re.IGNORECASE):
            end = m.end()
            if end < len(prompt) and u in prompt_upper[end:end+35]:
                return "teal" if color == "green" else color
    if any(h in u for h in CORAL_HINTS):
        return "coral"
    if any(h in u for h in TEAL_HINTS):
        return "teal"
    cobalt_words = {"GATE","WORKFLOW","LAB","STORE","VAULT","MATRIX","POOL","LEDGER","RULE","CONTROL","STAGE","FILTER","RERANK","INDEX","CLASSIFIER","CONFIG","CONTRACT","EXPLORER","DATASET","SCORER","QUALITY","CAPACITY","RELEASE","CANARY","FLAG","RUNBOOK","INCIDENT","PLATFORM","ARCHITECTURE","CONFIGURATION"}
    white_words = {"CARD","RECEIPT","RECORD","SPAN","METRIC","LOG","EVENT","CASE","SCORE","BUDGET","VERSION","RUBRIC","SET","NOTE","ARTIFACT","EVIDENCE","LABEL","ID","CERTIFICATE","RECEIPTS","TRACE","RESOURCE","RATE","ERROR","ERRORS","DURATION","PERCENT","OVERALL","PASSED","ELIGIBLE"}
    if any(h in u for h in COBALT_HINTS) or any(w in u.split() for w in cobalt_words):
        return "cobalt"
    if any(h in u for h in WHITE_HINTS) or any(w in u.split() for w in white_words):
        return "white"
    return "cyan"

def find_phrase_in_text(label, text):
    # Prefer clauses bounded by sentence or list separators
    clauses = re.split(r'(?<=[;:,.])\s+', text)
    matches = [c.strip() for c in clauses if re.search(r'\b' + re.escape(label) + r'\b', c, re.IGNORECASE)]
    # fallback to full sentence
    if not matches:
        pattern = r'([^.]*\b' + re.escape(label) + r'\b[^.]*\.)'
        matches = re.findall(pattern, text, re.IGNORECASE)
    if not matches:
        pattern2 = r'([^,;.]{0,120}\b' + re.escape(label) + r'\b[^,;.]{0,160})'
        matches = re.findall(pattern2, text, re.IGNORECASE)
    return matches

def clean_phrase(phrase, label, prompt=""):
    # strip leading imperatives and location words
    stripped = phrase.strip()
    for prefix in ["Show ","Arrange ","Build ","Create ","Draw ","Place ","Include ","Add ",
                   "Beneath it ","Under it ","To the side ","Beside them ","On the right ",
                   "On the left ","Near the bottom ","At the bottom ","At the top ","In the center ",
                   "From the left ","From the top "]:
        if stripped.startswith(prefix):
            stripped = stripped[len(prefix):]
    # if the phrase starts with the label, use the rest as definition
    m = re.match(r'^\s*(The\s+|A\s+|An\s+)?' + re.escape(label) + r'\b\s*(is\s+|are\s+)?', stripped, re.IGNORECASE)
    if m:
        rest = stripped[m.end():].strip()
        if rest and not re.fullmatch(r'[;:,\.\-\u2013\u2014\s]+', rest):
            rest = rest[0].lower() + rest[1:]
            return f"The **{label}** is {rest.rstrip('.')}."
    # find the label position
    m = re.search(r'\b' + re.escape(label) + r'\b', stripped, re.IGNORECASE)
    if not m:
        return f"The **{label}** is a key teaching element in this diagram."
    start = m.start()
    end = m.end()
    # look for color word before label
    before = stripped[:start].strip()
    color_word = None
    color_match = re.search(r'\b(coral|teal|cyan|green)\b\s+$', before, re.IGNORECASE)
    if color_match:
        color_word = color_match.group(1).lower()
        if color_word == "green":
            color_word = "teal"
        before = before[:color_match.start()].strip()
    # determine article
    article = "a"
    if before.lower().endswith("the"):
        article = "the"
    elif before.lower().endswith("one") or before.lower().endswith("a") or before.lower().endswith("an"):
        article = "a"
    # look for role noun after label
    after = stripped[end:].strip()
    role = ""
    after_words = re.findall(r"\b\w+\b", after)
    for w in after_words[:6]:
        if w.lower() in ROLE_NOUNS:
            role = w
            break
    if not role and label.split()[-1].lower() in ROLE_NOUNS:
        role = label.split()[-1]
    if role:
        # build with role
        role_end = after.lower().find(role.lower()) + len(role)
        rest = after[role_end:].strip()
        if rest.startswith(",") or rest.startswith(";"):
            rest = rest[1:].strip()
        adj = f"{color_word} " if color_word else ""
        full = f"The **{label}** is {article} {adj}{role}"
        if rest:
            full += f" {rest}"
        return full.rstrip(".") + "."
    else:
        # no clear role: describe as a path/record that fits the surrounding clause
        color = color_of(label, prompt) if prompt else "white"
        role = "record"
        if color == "cobalt":
            role = "platform or boundary"
        elif color == "cyan":
            role = "request or propagation path"
        elif color == "teal":
            role = "healthy or verified result path"
        elif color == "coral":
            role = "failure, risk, or incident path"
        adj = f"{color_word} " if color_word else f"{color} "
        # form a clause from the rest of the phrase without the label
        rest = (before + " " + after).strip()
        # remove dangling articles and a few leading words
        rest = re.sub(r'^(the|a|an|and|or|of|to|in|on|for|with|from|by|as|is|it)\s+', '', rest, flags=re.IGNORECASE)
        full = f"The **{label}** is {article} {adj}{role}"
        if rest and not re.fullmatch(r'[;:,\.\-\u2013\u2014\s]+', rest):
            first = rest.split()[0].lower() if rest.split() else ""
            participles = {"connected","named","shown","shown","marked","caught","blocked","linked","showing","naming","indicating","returning","entering","leaving","flowing","containing"}
            rest = rest[0].lower() + rest[1:]
            if first in participles and not first.endswith('ing'):
                full += f" that is {rest}"
            else:
                full += f" that {rest}"
        return full.rstrip(".") + "."

def _try_lookup(label, maps):
    key = label.upper()
    for d in maps:
        if key in d:
            return d[key]
        # try singular (or plural) variant
        if label.endswith('S') and len(label) > 1:
            singular = label[:-1].upper()
            if singular in d:
                return d[singular]
        if label.endswith('ES') and len(label) > 2:
            singular = label[:-2].upper()
            if singular in d:
                return d[singular]
    return None

def _verb_for(label):
    singular = {"NEXT.JS", "A2A", "MCP", "RAG", "MCP CALL", "A2A TASK", "AGENT CARD"}
    if label in singular:
        return "is"
    if label.endswith('S') and not label.endswith('SS') and len(label) > 1:
        return "are"
    return "is"

def _definition_desc(label, text):
    text = text.strip()
    text = re.sub(r'^(is\s+|are\s+)', '', text, count=1, flags=re.IGNORECASE)
    text = text.rstrip('.')
    if not text:
        return None
    words = text.split()
    first = words[0].lower() if words else ""
    verb_set = {"follows","combines","records","identifies","contains","carries","stores","shows","defines","provides","represents","runs","produces","sits","flows","receives","turns","connects","returns","blocks","catches","selects","passes","starts","exits","enters"}
    if first in verb_set:
        text = text[0].lower() + text[1:]
        return f"The **{label}** {text}."
    # noun phrase: determine article
    if first in ("the","a","an","one"):
        article = ""
    elif first[0] in 'aeiou':
        article = "an"
    else:
        article = "a"
    verb = _verb_for(label)
    text = text[0].lower() + text[1:]
    if article:
        return f"The **{label}** {verb} {article} {text}."
    return f"The **{label}** {verb} {text}."

def describe_label(label, prompt, explanation, global_glossary, definition_map):
    maps = [FALLBACK_DESCRIPTIONS, global_glossary, definition_map]
    # look up exact or singular/plural
    text = _try_lookup(label, maps)
    if text:
        if label in FALLBACK_DESCRIPTIONS or label.upper() in global_glossary or label.upper() in definition_map:
            return _definition_desc(label, text)
        return _definition_desc(label, text)
    # explanation: find a clause that starts with the label and a verb
    matches = find_phrase_in_text(label, explanation)
    good = [m for m in matches if re.match(r'^\s*(The|A|An)?\s*' + re.escape(label) + r'\b\s*(is|are|follows|combines|records|identifies|contains|carries|stores|shows|defines|provides|represents)', m, re.IGNORECASE)]
    if good:
        sent = good[0].strip()
        rest = re.sub(r'^\s*(The|A|An)?\s*' + re.escape(label) + r'\b\s*', '', sent, flags=re.IGNORECASE).strip()
        d = _definition_desc(label, rest)
        if d:
            return d
    # prompt: use a short clause
    matches = find_phrase_in_text(label, prompt)
    if matches:
        phrase = min(matches, key=len).strip()
        desc = clean_phrase(phrase, label, prompt)
        if desc:
            return desc
    # generic colour-based fallback
    color = color_of(label, prompt)
    role = "record"
    if color == "cobalt":
        role = "platform or boundary"
    elif color == "cyan":
        role = "request or propagation path"
    elif color == "teal":
        role = "healthy or verified result path"
    elif color == "coral":
        role = "failure, risk, or incident path"
    verb = _verb_for(label)
    return f"The **{label}** {verb} a {color} {role} in this diagram; it represents one of the key teaching elements."

def layout_summary(prompt):
    # split into sentences and convert leading imperatives to third person
    raw_sents = re.split(r'(?<=[.!?])\s+', prompt.strip())
    sents = []
    for s in raw_sents:
        s = s.strip()
        if s:
            for verb, third in [("Show ","shows "),("Arrange ","arranges "),("Build ","builds "),
                                ("Create ","creates "),("Draw ","draws "),("Place ","places "),
                                ("Include ","includes "),("Add ","adds ")]:
                if s.lower().startswith(verb.lower()):
                    s = third + s[len(verb):]
                    break
            sents.append(s)
    if not sents:
        return prompt.strip()
    if len(sents) == 1:
        summary = f"The diagram {sents[0][0].lower() + sents[0][1:].rstrip('.')}."
    else:
        first = (sents[0][0].lower() + sents[0][1:]).rstrip('.')
        second = (sents[1][0].lower() + sents[1][1:]).rstrip('.')
        summary = f"The diagram {first}; it also {second}."
    summary = re.sub(r'\s+', ' ', summary).strip()
    if len(summary) > 300:
        summary = summary[:summary.rfind(',', 0, 300)] + '.' if ',' in summary[:300] else summary[:300] + '...'
    return summary

def heading_from_trace(trace):
    # produce a 4-10 word conceptual heading from a trace instruction
    words = trace.strip().split()
    # trim to a reasonable chunk, then remove trailing connectors
    n = min(12, len(words))
    heading = " ".join(words[:n])
    # collapse repeated words in parallel lists (e.g. user outcomes, unacceptable outcomes)
    heading = re.sub(r',?\s*(and\s+)?proposed.*$', '', heading, flags=re.IGNORECASE)
    heading = re.sub(r'[,;]\s*$', '', heading)
    heading = re.sub(r'\s+(and|or|a|an|the|for|to|of|in|on|with|from|by|as|is|it|that)$', '', heading, flags=re.IGNORECASE)
    if len(heading.split()) > 10:
        heading = " ".join(heading.split()[:10])
        heading = re.sub(r'\s+(and|or|a|an|the|for|to|of|in|on|with|from|by|as|is|it|that)$', '', heading, flags=re.IGNORECASE)
    return heading

def concept_body(trace, explanation, case_study, prompt, idx):
    # Build a rich, specific paragraph around the trace step
    exp_sents = sentencize(explanation)
    trace_words = set(re.findall(r'\b\w+\b', trace.lower())) - STOPWORDS
    # pick the explanation sentences most related to the trace
    scored = [(s, len(set(re.findall(r'\b\w+\b', s.lower())) & trace_words)) for s in exp_sents]
    scored.sort(key=lambda x: -x[1])
    best = scored[0][0] if scored and scored[0][1] > 0 else (exp_sents[0] if exp_sents else "")
    best2 = scored[1][0] if len(scored) > 1 and scored[1][1] > 0 else ""
    # shorten to a clause if very long
    if len(best) > 180:
        best = best[:best.find(',', 120)] + "." if ',' in best[120:180] else best[:160] + "..."
    if len(best2) > 180:
        best2 = best2[:best2.find(',', 120)] + "." if ',' in best2[120:180] else best2[:160] + "..."

    # visual labels from the prompt that match the trace
    labels = extract_labels(prompt)
    trace_labels = [l for l in labels if l.lower() in trace.lower()]
    if not trace_labels:
        trace_labels = [l for l in labels if any(w in l.lower() for w in trace_words if len(w) > 3)]
    visual = ""
    if trace_labels:
        visual = f"In the diagram, this is represented by **{trace_labels[0]}**"
        if len(trace_labels) > 1:
            visual += f" and **{trace_labels[1]}**"
        if len(trace_labels) > 2:
            visual += f", near **{trace_labels[2]}**"
        visual += "."

    case_name = case_study['situation'].split('.')[0]
    danger = case_study['danger']
    result = case_study['result']
    take = case_study['takeaway']

    def lc(s):
        return s[0].lower() + s[1:] if s else s

    best2_clause = f" {best2}" if best2 and best2 != best else ""
    templates = [
        f"{trace}{best2_clause} {best} {visual} The case study where {case_name} makes the risk concrete: {lc(danger)} When this step is done well, {lc(result)}",
        f"{visual} {trace}{best2_clause} {best} The case study where {case_name} shows the value: {lc(result)} Skip it, and {lc(danger)}. The takeaway is clear: {lc(take)}",
        f"{best} This is why the step is non-negotiable: {lc(trace)}.{best2_clause} {visual} The case study where {case_name} proves it: {lc(result)} If the team omits this, {lc(danger)}"
    ]
    body = templates[idx % len(templates)]
    body = re.sub(r'\s+', ' ', body).strip()
    # ensure it ends with one period
    body = re.sub(r'\.{2,}', '.', body).rstrip('.') + '.'
    return body

def overview_paragraph(explanation, outcome):
    sents = sentencize(explanation)
    # take the first 4-6 sentences, but not the full explanation if it's very long
    n = min(6, max(4, len(sents) // 2 + 1))
    body = " ".join(sents[:n])
    # ensure it mentions outcome
    if outcome not in body:
        body += f" The diagram exists so the team can {outcome[0].lower()}{outcome[1:]}"
    return body

def nextjs_paragraph(items, title):
    if not items:
        return ""
    lead = f"In the {title} surface, the same contract appears through framework-specific patterns."
    body = " ".join(items)
    return lead + " " + body

def python_paragraph(items):
    if not items:
        return ""
    lead = "In the Python surface, the same contract is enforced with typed models and tests."
    body = " ".join(items)
    return lead + " " + body

def summary_paragraph(trace, case, outcome, takeaway):
    if not trace:
        return takeaway
    items = [t.rstrip('.') for t in trace]
    steps = "; ".join(items[:3]) + "."
    if len(items) > 3:
        steps = steps.rstrip('.') + ". The remaining steps extend this: " + "; ".join(items[3:]) + "."
    situation = case['situation'].split('.')[0]
    danger = case['danger'].rstrip('.')
    danger = danger[0].lower() + danger[1:]
    take = takeaway.rstrip('.')
    take = take[0].lower() + take[1:]
    out = outcome.rstrip('.')
    out = out[0].lower() + out[1:]
    return f"Taken together, these steps turn the objective \"{out}\" into an operating contract. {steps} The case of {situation} shows how quickly {danger}. The durable lesson is {take}."

def case_study_section(lesson, manual):
    case = lesson["caseStudy"]
    name = manual["case_study_names"].get(str(lesson["id"]), "Maya and the case study")
    md = [f"## Case study \u2014 {name}", "", case["situation"], "", "### The walkthrough", ""]
    for i, step in enumerate(case["walkthrough"], 1):
        md.append(f"{i}. {step}")
    md.extend(["", "### The result", "", case["result"], "", "### The danger", "", case["danger"], "", "### The takeaway", "", case["takeaway"]])
    return "\n".join(md)

def color_and_flow(lesson, prompt, labels, color_of):
    color_map = {"cobalt":[], "cyan":[], "teal":[], "coral":[], "white":[]}
    for l in labels:
        color_map[color_of(l, prompt)].append(l)
    # ensure color words from prompt are included
    for m in re.finditer(r'\b(coral|teal|cyan)\b\s+([A-Z][A-Z0-9\s\-/]*)', prompt):
        c = m.group(1)
        name = m.group(2).strip()
        name = re.sub(r'\s+(and|or)$', '', name)
        if name and name not in color_map[c]:
            color_map[c].append(name)
    names = {"cobalt":"platform","cyan":"arrow","teal":"arrow","coral":"path","white":"card"}
    lines = []
    for c, els in color_map.items():
        if els:
            lines.append(f"- **{c.capitalize()} {names[c]}** \u2014 {VISUAL_GRAMMAR[c]}. In this diagram it appears on {', '.join([f'**{e}**' for e in els[:8]])}{' and others' if len(els)>8 else ''}.")
    return "\n".join(lines)

def at_a_glance(lesson, prompt, manual):
    outcome = lesson["outcome"]
    trace = lesson.get("trace", [])
    bullets = []
    if trace:
        for t in trace[:3]:
            bullets.append(t[0].upper() + t[1:])
    # add a warning/reward from prompt colors
    coral = [l for l in extract_labels(prompt) if color_of(l, prompt) == "coral"]
    if coral:
        bullets.append(f"A {coral[0]} path shows the failure the design must catch before it reaches the user.")
    else:
        bullets.append(lesson["caseStudy"]["takeaway"])
    return f"**{outcome}**\n\n" + "\n".join(f"- {b}" for b in bullets[:4])

def present_it_bullets(lesson, prompt, manual, labels):
    trace = lesson.get("trace", [])
    case = lesson["caseStudy"]
    analogy = lesson.get("analogy", "")
    bullets = ["Start with the operational question the team actually needs to answer. Point at the central element and ask what a regulator, evaluator, or support operator would ask about this outcome, and which signal type would best answer it."]
    point_verbs = ["Point at", "Highlight", "Trace with your finger", "Put a marker on", "Ask the room to locate", "Walk the room to"]
    lead_ins = [
        "Ask the room what the team would need to know before approving the next release.",
        "Have the group list the operational decisions this stage informs.",
        "Ask what evidence would change the route a support ticket takes.",
        "Get the room to name the owner who would need this evidence in an incident.",
        "Ask what would need to be true for the team to skip this stage safely."
    ]
    question_starts = [
        "what would change if this step were skipped?",
        "what real decision does this evidence support?",
        "what would a missing or corrupted value look like here?",
        "who owns the evidence produced at this step?",
        "which downstream stage would fail if this step were wrong?"
    ]
    for i, t in enumerate(trace):
        labels_in = [l for l in labels if l.lower() in t.lower()]
        if not labels_in:
            # try keywords from t
            words = set(re.findall(r'\b\w+\b', t.lower())) - STOPWORDS
            labels_in = [l for l in labels if any(w in l.lower() for w in words if len(w) > 3)]
        target = f"**{labels_in[0]}**" if labels_in else "the trace"
        if len(labels_in) > 1:
            target += f" and **{labels_in[1]}**"
        verb = point_verbs[i % len(point_verbs)]
        lead = lead_ins[i % len(lead_ins)]
        q = question_starts[i % len(question_starts)]
        bullets.append(f"{lead} {verb} {target} and ask {q} Use the case study to make the failure concrete.")
    if analogy:
        bullets.append(f"Use the analogy. {analogy.split('.')[0]}. Ask the room where the equivalent tracking number, queue, or ledger is in their own system, and where it would first break.")
    bullets.append(f"Tell the case study \u2014 {manual['case_study_names'].get(str(lesson['id']), 'Maya')}. Walk through the walkthrough and stop at the moment the failure first becomes visible. Ask what signal, gate, or version field would have caught it earlier.")
    bullets.append(f"Run the lab. {lesson['lab']} Have each group label the fields that are captured, hashed, redacted, or omitted.")
    bullets.append(f"Pose the checkpoint. {lesson['checkpoint']} Let the room answer before confirming with the answer. Then ask what the team would change in the next build based on the answer.")
    bullets.append(f"Before moving on, ask the room to trace one healthy teal path and one coral path through the diagram, naming the evidence that flips the colour at each stage.")
    bullets.append(f"Close on the contract. {lesson['caseStudy']['takeaway']} Make the group write one sentence that ties the lesson to their own system.")
    return "\n".join(f"- {b}" for b in bullets)

def render_lesson(lesson, course, manual):
    modules = build_modules_map(course)
    module = modules[lesson["moduleId"]]
    sources_map = build_sources_map(course)
    global_glossary = build_global_glossary(course)
    definition_map = build_definition_map(course)

    prompt = lesson["diagramPrompt"]
    title = lesson["title"]
    slug = lesson["slug"]
    module_title = module["title"]
    role = module["purpose"]
    layout = layout_summary(prompt)
    alt = lesson["alt"]
    outcome = lesson["outcome"]
    explanation = lesson["explanation"]
    trace = lesson.get("trace", [])
    nextjs = lesson.get("nextjs", [])
    python = lesson.get("python", [])
    case = lesson["caseStudy"]

    md = []
    md.append(f"# Diagram {lesson['id']} \u2014 {title}")
    md.append("")
    md.append(f"![{alt}](../diagrams/{lesson['id']:03d}-{slug}.png)")
    md.append("")
    md.append(f"**Module:** {module_title}")
    md.append(f"**Role in the course:** {role}")
    md.append(f"**Layout:** {layout}")
    md.append("")
    md.append("---")
    md.append("")

    # At a glance
    md.append("## At a glance")
    md.append("")
    md.append(at_a_glance(lesson, prompt, manual))
    md.append("")
    md.append("---")
    md.append("")

    # What the diagram teaches
    md.append("## What the diagram teaches")
    md.append("")
    oh = manual["overview_headings"].get(str(lesson["id"]), outcome.rstrip('.'))
    md.append(f"### 1. {oh}")
    md.append("")
    md.append(overview_paragraph(explanation, outcome))
    md.append("")
    for i, t in enumerate(trace, 2):
        md.append(f"### {i}. {heading_from_trace(t)}")
        md.append("")
        md.append(concept_body(t, explanation, case, prompt, i-2))
        md.append("")
    if trace:
        md.append(f"### {len(trace)+2}. Putting it together")
        md.append("")
        md.append(summary_paragraph(trace, case, outcome, case['takeaway']))
        md.append("")
    if lesson.get("analogy"):
        md.append("### Analogy")
        md.append("")
        md.append(lesson["analogy"])
        md.append("")
    if nextjs and python:
        md.append("### The Next.js surface")
        md.append("")
        md.append(nextjs_paragraph(nextjs, "Next.js"))
        md.append("")
        md.append("### The Python surface")
        md.append("")
        md.append(python_paragraph(python))
        md.append("")
    elif nextjs:
        md.append("### The Next.js surface")
        md.append("")
        md.append(nextjs_paragraph(nextjs, "Next.js"))
        md.append("")
    elif python:
        md.append("### The Python surface")
        md.append("")
        md.append(python_paragraph(python))
        md.append("")

    md.append("---")
    md.append("")

    # Case study
    md.append(case_study_section(lesson, manual))
    md.append("")
    md.append("---")
    md.append("")

    # Composition
    md.append("## Composition")
    md.append("")
    md.append(manual["compositions"][str(lesson["id"])])
    md.append("")

    # Element by element
    md.append("## Element by element")
    md.append("")
    labels = extract_labels(prompt)
    # also include labels from case/walkthrough? keep to prompt for now
    seen = set()
    for l in labels:
        if l in seen:
            continue
        seen.add(l)
        desc = describe_label(l, prompt, explanation, global_glossary, definition_map)
        md.append(f"- **{l}** \u2014 {desc}")
    md.append("")

    md.append("---")
    md.append("")

    # Colour and flow semantics
    md.append("## Colour and flow semantics")
    md.append("")
    md.append(color_and_flow(lesson, prompt, labels, color_of))
    md.append("")
    md.append(f"The overall flow moves from the inputs on the left through the {module_title.lower()} stages and exits as either a teal healthy path or a coral failure path. White cards carry the records, cobalt platforms hold the boundaries, and the cyan arrows show propagation and requests.")
    md.append("")
    md.append("---")
    md.append("")

    # How to present it
    md.append("## How to present it")
    md.append("")
    md.append(present_it_bullets(lesson, prompt, manual, labels))
    md.append("")
    md.append("---")
    md.append("")

    # Lab and checkpoint
    md.append("## Lab and checkpoint")
    md.append("")
    md.append(f"**Lab:** {lesson['lab']}")
    md.append("")
    md.append(f"**Checkpoint:** {lesson['checkpoint']}")
    md.append("")
    md.append(f"**Answer:** {lesson['answer']}")
    md.append("")
    md.append("---")
    md.append("")

    # Glossary
    md.append("## Glossary")
    md.append("")
    for entry in lesson.get("glossary", []):
        if " - " in entry:
            term, definition = entry.split(" - ", 1)
            md.append(f"- **{term}** \u2014 {definition}")
        else:
            md.append(f"- {entry}")
    md.append("")
    md.append("---")
    md.append("")

    # Sources
    md.append("## Sources")
    md.append("")
    for src in lesson.get("sources", []):
        url = sources_map.get(src)
        if url:
            md.append(f"- [{src}]({url})")
        else:
            md.append(f"- {src}")
    md.append("")
    md.append("---")
    md.append("")

    # Related lessons
    related = lesson.get("related", [])
    if related:
        md.append("## Related lessons")
        md.append("")
        related_lessons = {l["id"]: l for l in course["lessons"]}
        for rid in related:
            rl = related_lessons.get(rid)
            if rl:
                md.append(f"- Diagram {rid} \u2014 {rl['title']}")
        md.append("")
        md.append("---")
        md.append("")

    return "\n".join(md)

def main():
    manual = load_manual()
    course = load_course()
    os.makedirs(OUT_DIR, exist_ok=True)
    for lesson in course["lessons"]:
        if lesson["id"] < 173 or lesson["id"] > 196:
            continue
        out_path = os.path.join(OUT_DIR, f"{lesson['id']:03d}-{lesson['slug']}.md")
        md = render_lesson(lesson, course, manual)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"Wrote {out_path}")

if __name__ == "__main__":
    main()
