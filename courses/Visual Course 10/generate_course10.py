import json
import re
import os
import math
from pathlib import Path

BASE = Path(__file__).resolve().parent
OUT = BASE / 'diagram-docs'
OUT.mkdir(parents=True, exist_ok=True)

JSON_PATH = BASE / 'Volume 10 Course Content.json'

with open(JSON_PATH, encoding='utf-8') as f:
    course = json.load(f)

modules = {m['id']: m for m in course['modules']}
lessons = course['lessons']
visual_grammar = course['course']['visualGrammar']

STOP_WORDS = {
    'a','an','the','and','or','but','to','of','in','on','at','for','with','by','from','as','is','are','was','were','be','been','being','have','has','had','do','does','did','will','would','could','should','may','might','must','can','this','that','these','those','it','he','she','me','us','them','my','your','our','their','its','his','her','if','no','not','up','so','about','into','through','over','under','again','further','then','once','here','there','when','where','why','how','all','any','both','each','few','more','most','other','some','such','only','own','same','than','very','just','also','back','after','use','two','one','a2a','mcp','ag','ui','dpop'
}

COMMON_DESCRIPTIONS = {
    "USER PROBLEM": "the starting gap between the outcome a person needs and what the current system reliably provides; it is the only input that should begin the architecture decision.",
    "HUMAN JUDGMENT": "a guard rail added to the decision path that frames the choice with human oversight and responsibility rather than model authority.",
    "AUTHORITATIVE SYSTEM": "a guard rail added to the decision path that represents the business systems trusted to establish customer, policy, payment, and receipt truth.",
    "FIT": "the teal path that selects the smallest sufficient pattern for the user problem.",
    "AGENT EVERYWHERE": "the coral default of applying the agent label to every problem, leading to unnecessary cost, risk, and confusion.",
    "COST": "a consequence of the coral AGENT EVERYWHERE path; it represents the wasted money and effort from applying an agent to problems a simpler pattern would solve.",
    "RISK": "a consequence of the coral AGENT EVERYWHERE path; it represents the added danger from letting unconstrained agency touch business truth.",
    "CONFUSION": "a consequence of the coral AGENT EVERYWHERE path; it represents the unclear responsibility that follows from labeling every tool an agent.",
    "DOCUMENT": "a bounded choice in the decision path; it represents information that is fixed enough to present without reasoning or action.",
    "WORKFLOW": "a bounded choice for a path that follows known, repeatable steps with little uncertainty.",
    "ASSISTANT": "a bounded choice where the system helps a person decide but does not act on its own.",
    "AGENT": "a bounded choice where the system selects or sequences actions under explicit constraints and evidence.",
    "AUTOMATION": "a bounded choice where a stable decision rule is executed without model reasoning.",
    "LOW": "a risk class for use cases with limited, manageable harm that may still need review.",
    "MODERATE": "a risk class for use cases with real but bounded harm that require review before action.",
    "HIGH": "a risk class for use cases that can cause serious harm and need strong human authority.",
    "PROHIBITED": "a risk class for use cases that must not proceed automatically because the harm is unacceptable.",
    "ADVISE": "the lowest human authority gate; the system may suggest or draft, but not commit.",
    "REVIEW": "a human authority gate where a person examines a proposal before it proceeds.",
    "APPROVE": "a human authority gate where a person explicitly authorizes a specific bounded action.",
    "EXECUTE": "the highest human authority gate; the action proceeds, often automatically within a tiny reversible envelope after explicit approval.",
    "ILLUSTRATIVE": "a warning that the sample values or scores are teaching examples and must not be presented as measured product results.",
    "SCENARIO": "a label that separates exercise, simulated, or proposed evidence from measured results in the portfolio.",
    "MEASURED": "a label that attaches only to results collected from the implemented project with valid instrumentation and evidence.",
    "BLUEPRINT PACK": "the shared handoff artifact that contains the architecture, contracts, fixtures, and evidence the two projects share.",
    "NEXTJS REACT PROJECT": "the separate Next.js implementation project that owns the web experience, accessible UI, and Vercel deployment.",
    "PYTHON FASTAPI PROJECT": "the separate Python implementation project that owns domain rules, adapters, durable work, and service deployment.",
    "ONE ACME DEMO": "the single reproducible demonstration that both projects converge on to prove the shared user journey.",
    "PORTFOLIO PROOF": "the evidence pack that makes the project credible and traceable to tests, deployment, and measured results.",
    "HIGH HARM LOW REVERSIBILITY": "the coral condition that forces a use case to stay human-controlled because the harm is high and the action cannot be undone.",
    "HUMAN ONLY": "the coral outcome for high-harm, low-reversibility work that must remain under direct human control.",
    "DIRECT MODEL TO BUSINESS WRITE": "the coral anti-pattern where a model or its output can write directly to authoritative business records.",
    "ONE GIANT VECTOR STORE": "the coral anti-pattern that collapses operational state, source data, memory, evidence, artifacts, and audit into one ungoverned index.",
    "LEAK": "a consequence of the coral ONE GIANT VECTOR STORE: sensitive data becomes reachable.",
    "STALE": "a consequence of the coral ONE GIANT VECTOR STORE: outdated copies are used.",
    "NO DELETE": "a consequence of the coral ONE GIANT VECTOR STORE: data cannot be fully removed.",
    "ONE PROTOCOL FOR EVERYTHING": "the coral anti-pattern of forcing a single transport on every relationship regardless of need.",
    "USE CACHE AS TRUTH": "the coral anti-pattern of treating cached data as the authoritative record.",
    "VECTOR AS AUTHORITY": "the coral anti-pattern of treating the vector index as the source of truth.",
    "RAW PROMPTS EVERYWHERE": "the coral anti-pattern of collecting every prompt and tool argument for debugging.",
    "VANITY METRIC": "the coral anti-pattern of optimizing a number without user value.",
    "UNBOUNDED COST": "the coral anti-pattern of allowing model and tool spending to grow without controls.",
    "DIRECT PROD": "the coral anti-pattern of promoting code straight to production without gates.",
    "IRREVERSIBLE MIGRATION": "the coral anti-pattern of deploying a data change that cannot be undone.",
    "LAYER FIRST": "the coral anti-pattern of building an entire layer before integrating it end to end.",
    "BIG BANG": "the coral anti-pattern of one final integration reveal.",
    "HAPPY PATH ONLY": "the coral anti-pattern of testing only success.",
    "MOCK EVERYTHING": "the coral anti-pattern of replacing every boundary and testing an imaginary system.",
    "SELF APPROVAL": "the coral anti-pattern of the author certifying their own risk.",
    "PERMANENT EXCEPTION": "the coral anti-pattern of leaving a waiver open forever.",
    "SILENT RETRY": "the coral anti-pattern of repeating an action without observation or evidence.",
    "OWNER UNKNOWN": "the coral anti-pattern of an alert or decision with no accountable person.",
    "DIAGRAM BY AUTHORITY": "the coral anti-pattern of approving a picture instead of a defensible design.",
    "NO ALTERNATIVE": "the coral anti-pattern of presenting only one option.",
    "COPY PASTE ARCHITECTURE DRIFT": "the coral anti-pattern of copying the other project’s internals instead of sharing contracts and fixtures.",
    "FAT ROUTE": "the coral anti-pattern of putting the whole architecture in one FastAPI route.",
    "MODEL DIRECT TO DB": "the coral anti-pattern of letting the model write to the database directly.",
    "SECRETS IN BROWSER": "the coral anti-pattern of exposing credentials to the client.",
    "RAW PROTOCOL IN COMPONENTS": "the coral anti-pattern of letting React speak provider protocol directly.",
    "ENVIRONMENT DRIFT": "the coral difference between test and production that the test probes catch.",
    "TOKEN PASSTHROUGH": "the coral anti-pattern of forwarding a broad token to every downstream service.",
    "CROSS TENANT": "the coral anti-pattern of one tenant reaching another tenant’s data.",
    "SECRET IN CLIENT": "the coral anti-pattern of exposing a secret in the browser.",
    "HANDWRITTEN DRIFT": "the coral divergence when hand-coded types silently reinterpret the canonical contract.",
    "SCREENSHOT ONLY": "the coral anti-pattern of relying on a screenshot as the only evidence.",
    "INFLATED CLAIM": "the coral anti-pattern of presenting an unsupported metric or result.",
}

COMPOSITIONS = {
    221: "The picture is a left-to-right decision map. On the left, a **USER PROBLEM** card begins the scene and sends a cyan path toward the center. In the center, five white choice cards—**DOCUMENT**, **WORKFLOW**, **ASSISTANT**, **AGENT**, **AUTOMATION**—sit on a cobalt platform. Two rails, **HUMAN JUDGMENT** and **AUTHORITATIVE SYSTEM**, frame the top and bottom of the choice row. A teal **FIT** path leaves the problem and reaches the smallest sufficient choice, while a coral **AGENT EVERYWHERE** path forks to the right and spills into **COST**, **RISK**, and **CONFUSION**. The whole composition reads from uncertainty on the left to consequence on the right.",
    222: "The picture is a scorecard at the center of the scene. From the left, four candidate cards—**FAQ**, **POLICY REVIEW**, **REFUND COMMIT**, **ACCOUNT DELETE**—enter the **SCORECARD**. Inside the scorecard, six white cards—**VALUE**, **FREQUENCY**, **UNCERTAINTY**, **REVERSIBILITY**, **DATA**, **EVIDENCE**—represent the dimensions. A teal **POLICY REVIEW** arrow moves toward a **PILOT** card on the right. Below, a coral **HIGH HARM LOW REVERSIBILITY** arrow points to **HUMAN ONLY**. The bottom of the scorecard marks the sample scores **ILLUSTRATIVE**. The whole composition shows a decision funnel, not a calculator.",
    223: "The picture is a risk classifier. At the top, a **USE CASE** card enters a row of four class boxes—**LOW**, **MODERATE**, **HIGH**, **PROHIBITED**. Below them, five evidence cards—**IMPACT**, **LIKELIHOOD**, **EXPOSURE**, **REVERSIBILITY**, **DETECTABILITY**—feed the classification. In the middle, four **HUMAN AUTHORITY** gates—**ADVISE**, **REVIEW**, **APPROVE**, **EXECUTE**—stack vertically. On the right, a coral **UNACCEPTABLE OUTCOME** box triggers three teal response cards—**BLOCK**, **SAFE STATE**, **INCIDENT**. The composition reads top-down from use case to consequence.",
    224: "The picture is a contract-and-gate diagram. In the center, a **PILOT CONTRACT** card holds seven criteria cards—**USER OUTCOME**, **QUALITY**, **SAFETY**, **LATENCY**, **COST**, **ACCESSIBILITY**, **RECOVERY**. From each criterion, cyan arrows reach six **EVIDENCE** cards—**EVAL**, **TEST**, **TRACE**, **FEEDBACK**, **INCIDENT**. A teal **CONTINUE** path on the right requires all gates. A coral **EXIT CRITERIA** path on the lower right branches to **PAUSE**, **ROLLBACK**, and **REDESIGN**. The bottom notes that **SAMPLE TARGETS** are **ILLUSTRATIVE**. The composition makes the evidence chain the hero.",
    225: "The picture is a vertical trust-zone stack. From top to bottom, the zones are **USER**, **WEB APP**, **AGENT SERVICE**, **MODEL**, **MCP CLIENT**, **MCP SERVER**, **TOOL**, **BUSINESS SYSTEM**, each on a cobalt platform. Between the zones, gates—**CONTEXT**, **CAPABILITY**, **IDENTITY**, **POLICY**, **AUTHORITY**—appear as white cards. A teal **BOUNDED REQUEST** arrow descends from the user to a **RECEIPT** at the bottom. A coral **DIRECT MODEL TO BUSINESS WRITE** arrow is blocked by a red mark. The composition shows that no layer skips the one below it.",
    226: "The picture is a data architecture map. Six cobalt platform cards—**OPERATIONAL STATE**, **SOURCE DATA**, **MEMORY**, **EVIDENCE**, **ARTIFACTS**, **AUDIT**—sit as separate stores across the scene. White attribute cards—**IDS**, **VERSION**, **TENANT**, **OWNER**, **RETENTION**, **LINEAGE**—float above them. Teal **REFERENCES** arrows link the stores without copying secrets. On the right, a coral **ONE GIANT VECTOR STORE** card creates **LEAK**, **STALE**, and **NO DELETE**. The composition argues for separation, not consolidation.",
    227: "The picture is a protocol routing map. On the left, a **CLIENT EXPERIENCE** card connects by an **AG-UI** cyan arrow to an **AGENT SERVICE** platform in the center. From the agent service, four cyan arrows branch: **MCP** to **TOOLS AND CONTEXT**, **A2A** to **PEER AGENTS**, **HTTP** to **BUSINESS APIS**, **QUEUE** to **DURABLE WORK**, and a short **INTERNAL CALLS** arrow stays inside the **DOMAIN**. Each arrow carries a **CONTRACT** and **VERSION** card. A coral **ONE PROTOCOL FOR EVERYTHING** arrow on the right is blocked. The composition shows one service speaking several dialects.",
    228: "The picture is a deployment topology. On the left, **INTERNET** flows to a **VERCEL EDGE** and a **NEXTJS WEB** platform. In the center, a **PYTHON API** connects to a **WORKER POOL**, **POLICY**, **DATABASE**, **VECTOR**, **QUEUE**, **ARTIFACT STORE**, and **PROVIDERS**. Labeled **FAILURE DOMAINS**—**REGION**, **SERVICE**, **TENANT**, **PROVIDER**—appear as boundaries. **OWNER** and **SLO** cards sit beside components. A teal **DEGRADED MODE** path shows how service continues. A coral **CASCADE** is blocked by **BULKHEADS**. The composition makes ownership and blast radius visible.",
    229: "The picture is a contract kit at the center. A **CONTRACT KIT** card holds seven white cards—**JSON SCHEMA**, **OPENAPI**, **ASYNCAPI**, **EXAMPLES**, **FIXTURES**, **ERROR CASES**, **VERSION RULES**. Cyan arrows feed a **TYPESCRIPT** implementation on the left and a **PYDANTIC** implementation on the right. Both enter a **CONFORMANCE RUNNER** and produce a **SAME BEHAVIOR** card at the bottom. A coral **HANDWRITTEN DRIFT** arrow is blocked. The composition shows the contract as the source of truth for both stacks.",
    230: "The picture is a Next.js responsibility map. A **NEXTJS APP** platform in the center contains white cards for **SERVER COMPONENTS**, **ROUTE HANDLERS**, **SERVER ACTIONS**, **CLIENT ISLANDS**, **EVENT REDUCER**, **ACCESSIBLE UI**, **AUTH GATE**, and **ARTIFACT VIEW**. A cyan **TYPED CONTRACT** arrow connects the app to a **PYTHON API** on the right. Two coral blocked paths—**SECRETS IN BROWSER** and **RAW PROTOCOL IN COMPONENTS**—appear at the bottom. The composition keeps privileged work on the server side of the web boundary.",
    231: "The picture is a Python service map. A **PYTHON SERVICE** platform in the center contains white cards for **API ROUTERS**, **DOMAIN CORE**, **POLICY**, **ORCHESTRATOR**, **MCP ADAPTER**, **A2A ADAPTER**, **AG-UI ADAPTER**, **REPOSITORIES**, **WORKERS**, and **AUDIT**. A **PYDANTIC CONTRACT** ring surrounds the boundary. On the right, two coral blocked paths—**FAT ROUTE** and **MODEL DIRECT TO DB**—are marked with red. The composition shows FastAPI as one edge of a layered domain.",
    232: "The picture is an integration test loop. A **USER JOURNEY** arrow enters from the left and crosses **NEXTJS**, **API CONTRACT**, **FASTAPI**, **WORKFLOW**, **MCP AND A2A**, **BUSINESS SYSTEM**, and finally **RECEIPT**. A **TRACE ID** and **TEST PROBES** overlay the path. On the left, stacked test layers—**MOCK**, **CONTRACT**, **INTEGRATION**, **E2E**, **CHAOS**—feed the journey. A teal **SAME OUTCOME** path confirms the loop. A coral **ENVIRONMENT DRIFT** is caught by the probes. The composition shows one journey proven several ways.",
    233: "The picture is an identity and policy gate. **USER** and **SERVICE** identities enter from the left into an **AUTHENTICATION** gate. From there a cyan arrow reaches **AUTHORIZATION POLICY**, which holds five attribute cards—**TENANT**, **RESOURCE**, **ACTION**, **PURPOSE**, **SCOPE**. A **SECRETS VAULT** card at the top feeds only the server side. An **AUDIT RECEIPT** card records the decision. Teal **LEAST PRIVILEGE** path exits. Three coral blocked paths—**TOKEN PASSTHROUGH**, **CROSS TENANT**, **SECRET IN CLIENT**—are stopped. The composition makes every access decision explicit.",
    234: "The picture is a storage decision map. A **DATA NEED** card at the top points downward to five store platforms—**DATABASE**, **VECTOR INDEX**, **QUEUE**, **CACHE**, **ARTIFACT STORE**. Each store has a white card label: **TRUTH**, **SIMILARITY**, **DURABILITY**, **SPEED**, **LARGE FILES**. Around the stores, attribute cards—**TENANT**, **RETENTION**, **BACKUP**, **DELETE**, **ENCRYPT**—float. Two coral blocked paths—**USE CACHE AS TRUTH** and **VECTOR AS AUTHORITY**—are marked red. The composition maps data to the right job.",
    235: "The picture is a telemetry control plane. A **USER TASK** card at the left branches into six cyan streams—**TRACES**, **METRICS**, **LOGS**, **EVALS**, **ANALYTICS**, **COST**. They join through a central ring of **TRACE ID**, **TASK ID**, and **VERSION MANIFEST**. Above the streams, **PRIVACY FILTER** and **SAMPLING** cards sit as gates. A teal **DECISION EVIDENCE** path exits to the right. Three coral blocked paths—**RAW PROMPTS EVERYWHERE**, **VANITY METRIC**, **UNBOUNDED COST**—are stopped. The composition shows telemetry as a governed evidence system.",
    236: "The picture is a delivery pipeline. On the left, **CODE** enters a row of **CI** gates—**LINT**, **TEST**, **CONTRACT**, **SECURITY**, **A11Y**, **EVAL**, **BUILD**, **PROVENANCE**. Below, a promotion ladder runs **DEV** to **PREVIEW** to **STAGING** to **PRODUCTION**. In the center, **MIGRATION**, **FEATURE FLAG**, **CANARY**, **ROLLBACK**, and **RESTORE** cards sit between stages. A teal **VERIFIED RELEASE** path exits. Two coral blocked paths—**DIRECT PROD** and **IRREVERSIBLE MIGRATION**—are stopped. The composition reads left to right as a trust-but-verify release path.",
    237: "The picture is a roadmap of vertical slices. At the top, an **OUTCOME** card decomposes into six **VERTICAL SLICES**—**STATIC CASE**, **TYPED SERVICE**, **EVIDENCE**, **PROPOSAL**, **COMMIT RECEIPT**, **RECOVERY**. Each slice crosses five layers—**WEB**, **API**, **DATA**, **TEST**, **OPS**—shown as a ladder beneath it. Below the slices, **BACKLOG** cards hold **OWNER**, **DEPENDENCY**, **ACCEPTANCE**, and **DEMO**. Two coral blocked paths—**LAYER FIRST** and **BIG BANG**—are marked red. The composition shows a journey sliced all the way through.",
    238: "The picture is a test pyramid. At the base, a shared **FIXTURES** card and a **FAILURE INJECTION** card feed a stack of test layers—**UNIT**, **PROPERTY**, **CONTRACT**, **INTEGRATION**, **WORKFLOW**, **SECURITY**, **EVAL**, **ACCESSIBILITY**, **ACCEPTANCE**. The layers narrow as they rise. At the top, an **EVIDENCE MANIFEST** card collects the output. Two coral blocked paths—**HAPPY PATH ONLY** and **MOCK EVERYTHING**—are stopped at the base. The composition shows that deep evidence needs many kinds of proof.",
    239: "The picture is a readiness gate. A **RELEASE CANDIDATE** card at the left enters five gate platforms—**THREAT**, **EVALUATION**, **ACCESSIBILITY**, **PRIVACY**, **OPERATIONS**. Each gate has four white cards—**OWNER**, **EVIDENCE**, **PASS**, **FAIL**—and an **EXCEPTION EXPIRY** card. A teal **RELEASE** arrow on the right exits only after **REQUIRED PASS**. Two coral blocked paths—**SELF APPROVAL** and **PERMANENT EXCEPTION**—are stopped. The composition shows release as a cross-functional decision, not a single sign-off.",
    240: "The picture is an operational loop. An **ALERT** card at the left enters a cycle of six white steps—**TRIAGE**, **CONTAIN**, **COMMUNICATE**, **RECOVER**, **VERIFY**, **LEARN**—arranged in a ring. Around the ring, supporting cards—**RUNBOOK**, **ON CALL**, **SUPPORT**, **OWNER**, **STATUS**, **INCIDENT COMMAND**, **EVIDENCE**—float. A teal path from **SERVICE RESTORED** leads to a **REGRESSION FIXTURE**. Two coral blocked paths—**SILENT RETRY** and **OWNER UNKNOWN**—are blocked. The composition shows operations as a closed learning loop.",
    241: "The picture is an architecture review board. At the center, an **ARCHITECTURE REVIEW BOARD** ring encloses six white cards—**CONTEXT**, **REQUIREMENTS**, **OPTIONS**, **DECISION**, **CONSEQUENCES**, **EVIDENCE**. Two **OPTION** cards on the left are compared across six attribute cards—**VALUE**, **RISK**, **COST**, **COMPLEXITY**, **REVERSIBILITY**, **OPERATIONS**. On the right, output cards—**ADR** and **ACTIONS**—leave the board. Two coral blocked paths—**DIAGRAM BY AUTHORITY** and **NO ALTERNATIVE**—are stopped. The composition shows a review as an evidence-based comparison.",
    242: "The picture is a game-day map. At the top, **GAME DAY CONTROL** holds five cards—**HYPOTHESIS**, **SCOPE**, **SAFETY**, **STOP**, **OBSERVE**. From it, five failure injections—**PROVIDER DOWN**, **QUEUE DUPLICATE**, **STALE POLICY**, **TOKEN REPLAY**, **REGION LOSS**—drop into a team workflow ring of **DETECT**, **CONTAIN**, **DEGRADE**, **RECOVER**, **RECONCILE**, **VERIFY**. On the right, **EVIDENCE** and **ACTIONS** cards exit. The composition shows a controlled, contained, and observed failure exercise.",
    243: "The picture is a portfolio evidence chain. From left to right, a path of seven cards—**REQUIREMENT**, **ARCHITECTURE**, **CONTRACT**, **CODE**, **TEST**, **DEPLOYMENT**, **MEASURED RESULT**—runs across the center. Above and below the chain, supporting artifacts—**README**, **CASE STUDY**, **DEMO**, **ADR**, **THREAT MODEL**, **EVAL**, **RUNBOOK**—float. Two labels, **SCENARIO** and **MEASURED**, are attached to separate parts of the chain. Two coral blocked paths—**INFLATED CLAIM** and **SCREENSHOT ONLY**—are stopped. The composition shows a credible story backed by linked evidence.",
    244: "The picture is a graduation handoff map. In the center, a **BLUEPRINT PACK** splits into two project platforms—**NEXTJS REACT PROJECT** on the left and **PYTHON FASTAPI PROJECT** on the right. The center of the split holds shared cards—**CONTRACTS**, **FIXTURES**, **USER JOURNEY**, **ACCEPTANCE**, **THREAT**, **EVAL**, **OPERATIONS**, **EVIDENCE**. Each project has cards for **OWN REPO**, **README**, **DEPLOY**, and **TEST**. At the bottom, both projects converge on **ONE ACME DEMO** and **PORTFOLIO PROOF**. A coral **COPY PASTE ARCHITECTURE DRIFT** path is blocked. The composition shows one blueprint, two implementations, one proof.",
}


def word_count(text):
    return len(re.findall(r'\b\w+\b', text))


def split_sentences(text):
    return re.split(r'(?<=[.!?])\s+(?=[A-Z"\'])', text)


def title_case(phrase):
    small = {'a','an','the','and','but','or','for','nor','on','in','at','to','from','by','with','of','as'}
    words = phrase.split()
    out = []
    for i, w in enumerate(words):
        if w.isupper():
            out.append(w)
        elif i == 0 or w.lower() not in small:
            out.append(w.capitalize())
        else:
            out.append(w.lower())
    return ' '.join(out)


def shorten(text, minw=4, maxw=12):
    text = text.strip().rstrip('.').strip()
    # first, split at strong delimiters that naturally end a heading
    for d in ['; ', ' — ', ' – ', '. ', ' before ', ' so that ', ' while ', ' because ', ' and keep ', ' as well as ']:
        if d in text:
            part = text.split(d)[0].strip()
            words = part.split()
            if len(words) <= maxw and len(words) >= minw:
                return ' '.join(words).rstrip(' ,:;')
    # try to end before a list or coordinate conjunction
    for d in [': ', ', and ', ', or ', ', but also ', ', which ']:
        if d in text:
            part = text.split(d)[0].strip()
            words = part.split()
            if minw <= len(words) <= maxw:
                return ' '.join(words).rstrip(' ,:;')
    words = text.split()
    if len(words) > maxw:
        cut = maxw
        for i in range(maxw, minw-1, -1):
            if words[i-1].endswith((',',':',';')):
                cut = i
                break
        # avoid ending on a conjunction or article
        while cut > minw and words[cut-1].lower() in ('and','or','but','a','an','the','to','of','in'):
            cut -= 1
        return ' '.join(words[:cut]).rstrip(' ,:;')
    return ' '.join(words).rstrip(' ,:;')


def rephrase_step(step):
    step = step.strip()
    replacements = [
        (r'^Write\s+', 'Start with '),
        (r'^List\s+', 'Name '),
        (r'^Define\s+', 'Define '),
        (r'^Score\s+', 'Evaluate '),
        (r'^Apply\s+', 'Apply '),
        (r'^Turn\s+', 'Turn '),
        (r'^Create\s+', 'Create '),
        (r'^Place\s+', 'Place '),
        (r'^Record\s+', 'Record '),
        (r'^Build\s+', 'Build '),
        (r'^Run\s+', 'Run '),
        (r'^Choose\s+', 'Choose '),
        (r'^Name\s+', 'Name '),
        (r'^Use\s+', 'Use '),
        (r'^Separate\s+', 'Separate '),
        (r'^Match\s+', 'Match '),
        (r'^Bind\s+', 'Bind '),
        (r'^Classify\s+', 'Classify '),
        (r'^Assign\s+', 'Assign '),
        (r'^Map\s+', 'Map '),
        (r'^Show\s+', 'Show '),
        (r'^Start\s+', 'Start with '),
        (r'^Add\s+', 'Add '),
        (r'^Set\s+', 'Set '),
        (r'^Inventory\s+', 'Inventory '),
        (r'^Describe\s+', 'Describe '),
        (r'^Then\s+', ''),
        (r'^Begin\s+', 'Begin with '),
        (r'^Freeze\s+', 'Freeze '),
        (r'^Design\s+', 'Design '),
        (r'^Organize\s+', 'Organize '),
        (r'^Resolve\s+', 'Resolve '),
        (r'^Publish\s+', 'Publish '),
        (r'^Emit\s+', 'Emit '),
        (r'^Render\s+', 'Render '),
        (r'^Provide\s+', 'Provide '),
        (r'^Keep\s+', 'Keep '),
        (r'^Make\s+', 'Make '),
        (r'^Evaluate\s+', 'Evaluate '),
        (r'^Test\s+', 'Test '),
        (r'^Review\s+', 'Review '),
    ]
    for pat, repl in replacements:
        if re.match(pat, step, re.I):
            step = re.sub(pat, repl, step, count=1, flags=re.I)
            break
    # collapse doubled small words and remove trailing filler
    step = re.sub(r'\b(the|a|with|and|or)\s+\1\b', r'\1', step, flags=re.I)
    step = re.sub(r'\s*,?\s*(?:etc\.?|\.\.\.|and so on)$', '', step, flags=re.I)
    words = step.split()
    if len(words) > 14:
        cut = 14
        for i in range(14, 7, -1):
            if words[i-1].endswith((',',':',';')):
                cut = i
                break
        # avoid ending on an article/conjunction if the count is already long
        while cut > 8 and words[cut-1].lower() in ('a','an','the','and','or','but','to','with','by','for','from','of','in','on'):
            cut -= 1
        words = words[:max(6, cut)]
    step = ' '.join(words).rstrip(' ,:;')
    if not step:
        return 'Architecture principle'
    step = re.sub(r'^(?:the|a)\s+', '', step, flags=re.I)
    return title_case(step)


def extract_labels(prompt):
    pat1 = r"\b[A-Z][A-Z0-9\-]*(?:\s+[A-Z][A-Z0-9\-]*)+\b"
    pat2 = r"\b[A-Z]{2,}\b"
    multi = re.findall(pat1, prompt)
    # mask multi-word labels to test if a single word appears independently
    masked = prompt
    for mw in multi:
        masked = re.sub(r'(?<!\w)' + re.escape(mw) + r'(?!\w)', ' ' * len(mw), masked)
    singles = re.findall(pat2, masked)
    seen = set()
    result = []
    for m in multi + singles:
        m = m.strip()
        if not m or m in seen:
            continue
        ws = m.split()
        if all(w.lower() in STOP_WORDS for w in ws):
            continue
        seen.add(m)
        result.append(m)
    return result


def extract_color_phrases(prompt):
    teal = re.findall(r'\b[Tt]eal\s+([^.;]+)', prompt)
    coral = re.findall(r'\b[Cc]oral\s+([^.;]+)', prompt)
    return {'teal': [t.strip() for t in teal], 'coral': [c.strip() for c in coral]}


def extract_color_labels(prompt, labels):
    """Parse prompt and composition for teal/coral label assignments, handling response verbs."""
    label_set = set(labels)
    label_color = {}
    # find every color word and the phrase that follows until a sentence end or another color word
    for m in re.finditer(r'\b(teal|coral)\b', prompt, re.I):
        start = m.start()
        color = m.group(1).lower()
        # extend to end of sentence or next color word
        rest = prompt[start:]
        end = re.search(r'[.;]|\b(?:teal|coral)\b', rest[5:], re.I)
        end_pos = 5 + (end.start() if end else 0)
        if not end:
            end_pos = len(rest)
        phrase = rest[:end_pos]
        # token pattern: color words, labels (single or multi-word, case-sensitive uppercase), same-effect verbs, response verbs
        token_pat = r"\b(teal|coral)\b|\b((?-i:[A-Z][A-Z0-9\-]+(?:\s+[A-Z][A-Z0-9\-]+)*))\b|\b(blocked by|caught by|prevented by|stopped by|blocked by the|blocked|caught|prevented|stopped|triggers?|leads? to|leads|lead to|lead|branches? to|branches|branch to|branch|creates?|create|produces?|produce|makes?|make|becomes?|become)\b"
        current = color
        for tm in re.finditer(token_pat, phrase, re.I):
            tok = tm.group(0)
            if tok.lower() in ('teal', 'coral'):
                current = tok.lower()
                continue
            if tok.lower() in {'triggers', 'trigger', 'leads to', 'lead to', 'leads', 'lead', 'branches to', 'branch to', 'branches', 'branch', 'blocked by', 'blocked by the', 'caught by', 'prevented by', 'stopped by'}:
                # response path: assume teal unless another color is stated later in the phrase
                next_color = re.search(r'\b(teal|coral)\b', phrase[tm.end():], re.I)
                current = next_color.group(1).lower() if next_color else 'teal'
                continue
            if tok.lower() in {'creates', 'create', 'produces', 'produce', 'makes', 'make', 'becomes', 'become'}:
                # effect keeps the subject's color
                continue
            # tok is a label candidate
            if tok in label_set and tok not in label_color:
                label_color[tok] = current
    # derive ordered teal and coral lists from first occurrence order
    teal = [k for k, v in label_color.items() if v == 'teal']
    coral = [k for k, v in label_color.items() if v == 'coral']
    if not teal and not coral:
        return {'teal': [], 'coral': []}
    return {'teal': teal, 'coral': coral}


def labels_in_color(label, color_phrases, color):
    for ph in color_phrases.get(color, []):
        if re.search(r'\b' + re.escape(label) + r'\b', ph, re.I):
            return ph
    return None


def find_sentence_for_label(label, text):
    if not text:
        return None
    pat = re.compile(r'\b' + re.escape(label) + r'\b', re.I)
    for s in split_sentences(text):
        if pat.search(s):
            return s.strip()
    words = [w for w in re.findall(r'\b\w+\b', label) if w.lower() not in STOP_WORDS and len(w) > 2]
    if words:
        for s in split_sentences(text):
            if all(re.search(r'\b' + re.escape(w) + r'\b', s, re.I) for w in words):
                return s.strip()
    return None


def list_context_for_label(label, prompt):
    # find colon lists; take a short container from the words immediately before the colon
    for match in re.finditer(r':\s*([A-Z][A-Z0-9\-,\s]+?)(?:\.|;|$)', prompt):
        lst = match.group(1).strip()
        items = [it.strip() for it in re.split(r',|\band\b', lst) if it.strip()]
        if label not in items:
            continue
        start = match.start()
        before = prompt[:start].strip().split()
        # take the last few words before the colon
        container_words = before[-4:] if len(before) >= 4 else before
        container = ' '.join(container_words)
        container = re.sub(r'^(?:Show|Add|Then|Use|Place|Teal|Coral|a|an|the|with)\s+', '', container, flags=re.I)
        return container, items
    return None, None


def describe_label(label, lesson, color_phrases, prompt, all_labels):
    # 1. lesson-specific text
    sources = [
        lesson.get('explanation', ''),
        lesson.get('outcome', ''),
        ' '.join(lesson.get('trace', [])),
        lesson['caseStudy'].get('situation', ''),
        lesson['caseStudy'].get('takeaway', ''),
        ' '.join(lesson['caseStudy'].get('walkthrough', []))
    ]
    for src in sources:
        s = find_sentence_for_label(label, src)
        if s:
            return s
    # 2. glossary
    for g in lesson.get('glossary', []):
        term, _, defn = g.partition(' - ')
        if term:
            if term.lower() in label.lower() or label.lower() in term.lower():
                return f"{defn.strip()}."
    # 3. common dictionary
    if label in COMMON_DESCRIPTIONS:
        return COMMON_DESCRIPTIONS[label]
    # 4. color phrase
    color_map = extract_color_labels(prompt, all_labels)
    if label in color_map['teal']:
        ph = next((p for p in color_phrases.get('teal', []) if re.search(r'\b' + re.escape(label) + r'\b', p, re.I)), 'the safe path')
        return f"the safe, verified, or authoritative element marked in teal; in this diagram {ph}."
    if label in color_map['coral']:
        ph = next((p for p in color_phrases.get('coral', []) if re.search(r'\b' + re.escape(label) + r'\b', p, re.I)), 'the dangerous path')
        return f"the dangerous, unacceptable, or broken element marked in coral; in this diagram {ph}."
    # 5. list context
    container, items = list_context_for_label(label, prompt)
    if container:
        return f"one of the {container.lower()} in this diagram; {label} is the {label.lower()} entry among {', '.join(items[:3])}{' ...' if len(items)>3 else ''}."
    # 6. prompt window
    m = re.search(r'([^,;.]{0,100}\b' + re.escape(label) + r'\b[^,;.]{0,100})', prompt, re.I)
    if m:
        window = m.group(1).strip()
        # strip imperative and color prefixes
        window = re.sub(r'^(?:Show|Add|Then|Use|Place|Connect|Feed|Draw|Inject|Output|Mark|Each|One|A|And)\s+', '', window, flags=re.I)
        window = re.sub(r'^(?:Teal|Coral)\s+', '', window, flags=re.I)
        # if the window is just the label, give a terse generic description
        if re.sub(r'[^\w]', '', window).lower() == re.sub(r'[^\w]', '', label).lower():
            return f"the {label} card shown in this diagram; it is one of the labeled elements the architecture uses."
        return f"a labeled visual element in this diagram; the prompt shows it as {window}."
    return f"a labeled visual element in this diagram that represents {label.lower()}; it anchors one part of the architecture story."


def relevant_labels(heading, labels, n=3):
    hwords = set(w.lower() for w in re.findall(r'\b\w+\b', heading) if w.lower() not in STOP_WORDS and len(w) > 2)
    scored = []
    for lab in labels:
        lwords = [w.lower() for w in re.findall(r'\b\w+\b', lab) if w.lower() not in STOP_WORDS and len(w) > 2]
        score = sum(1 for w in lwords if w in hwords)
        if not score:
            for hw in hwords:
                if hw in lab.lower():
                    score = 1
                    break
        scored.append((score, lab))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [lab for _, lab in scored[:n] if _ > 0] or labels[:n]


def visual_sentence(heading, labels, idx):
    rlabels = relevant_labels(heading, labels, 3)
    positions = ["left", "center", "top", "right", "bottom", "lower right", "upper left"]
    pos = positions[idx % len(positions)]
    frames = [
        "In the diagram, {labels} appear at the {pos}, turning this idea into something a reviewer can point at.",
        "The visual places {labels} at the {pos}; the arrows between them are the physical expression of this principle.",
        "Look at {labels} on the {pos}: the diagram uses those elements to show where this decision lives.",
        "The picture shows {labels} as the visual anchor for this idea, with the surrounding paths showing the flow.",
        "At the {pos}, {labels} is the element that makes this concept concrete before any code is written.",
    ]
    label_str = ', '.join(f'**{l}**' for l in rlabels)
    return frames[idx % len(frames)].format(labels=label_str, pos=pos)


def consequence_sentence(heading, lesson, idx):
    danger = lesson['caseStudy'].get('danger', '')
    if not danger:
        danger = "the boundary becomes invisible and decisions become unaccountable"
    frames = [
        "If the team skips this, {danger}.",
        "Skip this step and {danger}.",
        "Without this, {danger}.",
        "The danger is that, without this, {danger}.",
        "Ignoring this means {danger}.",
    ]
    return frames[idx % len(frames)].format(danger=danger[0].lower() + danger[1:] if danger else danger)


def case_sentence(lesson, idx):
    situation = lesson['caseStudy'].get('situation', '')
    takeaway = lesson['caseStudy'].get('takeaway', '')
    frames = [
        "The Acme case—{situation}—shows the result: {takeaway}",
        "Maya's situation, {situation}, makes the point: {takeaway}",
        "In the case study, {situation}. The lesson is {takeaway}",
        "The scenario—{situation}—confirms that {takeaway}",
    ]
    return frames[idx % len(frames)].format(situation=situation, takeaway=takeaway)


def acme_sentence(lesson, idx):
    cs = lesson['caseStudy']
    items = [cs.get('situation',''), cs.get('danger',''), cs.get('result','')] + list(cs.get('walkthrough',[]))
    items = [i for i in items if i]
    if not items:
        return ''
    item = items[idx % len(items)]
    frames = [
        'In the Acme case, {item}.',
        "Maya's example shows that {item}.",
        'The walkthrough makes this concrete: {item}.',
        'The project confirms the point: {item}.'
    ]
    return frames[idx % len(frames)].format(item=item.rstrip('.'))


def negative_from_chunk(chunk):
    """Find a sentence in the chunk that contains a warning or consequence."""
    markers = ['wasteful', 'hide', 'conceal', 'risk', 'danger', 'fail', 'fails', 'wrong', 'unsafe', 'unacceptable', 'without this', 'if the team', 'skip', 'ignoring', 'breaks', 'break']
    for s in split_sentences(chunk):
        if any(m in s.lower() for m in markers):
            return s.strip()
    return None


def body_for_conceptual(heading, chunk, step, lesson, labels, idx):
    parts = []
    if chunk:
        chunk = chunk.strip().rstrip('.')
        if chunk:
            parts.append(chunk)
    if step and idx % 2 == 0:
        action = step.rstrip('.')
        action = action[0].lower() + action[1:]
        action = re.sub(r'\s+before writing the next layer\.?$', '', action)
        openers = [
            'To put this into practice, the team should ',
            'This means the team must ',
            'The trace asks the team to ',
            'Start by making the team '
        ]
        parts.append(f"{openers[idx % len(openers)]}{action}")
    parts.append(visual_sentence(heading, labels, idx).rstrip('.'))
    if idx % 4 == 1:
        neg = negative_from_chunk(chunk) or lesson['caseStudy'].get('danger', '')
        if neg:
            parts.append(f"If this is skipped, {neg[0].lower()+neg[1:] if neg else neg}".rstrip('.'))
    if idx % 4 == 3:
        a = acme_sentence(lesson, idx)
        if a:
            parts.append(a.rstrip('.'))
    final = '. '.join(p.strip() for p in parts if p) + '.'
    final = re.sub(r'\.\s+\.', '. ', final)
    final = re.sub(r'\.\.', '.', final)
    return final


def distribute_sentences(headings, explanation, cap=6):
    if not explanation or not headings:
        return [''] * len(headings)
    sentences = split_sentences(explanation)
    if not sentences:
        return [''] * len(headings)
    hwords = []
    for h in headings:
        words = [w for w in re.findall(r'\b\w+\b', h) if w.lower() not in STOP_WORDS and len(w) > 3]
        hwords.append(words)
    assigned = [[] for _ in headings]
    for s in sentences:
        best = -1
        best_key = (-1, 0, -1)
        for i, words in enumerate(hwords):
            score = sum(1 for w in words if w.lower() in s.lower())
            # prefer higher score, then fewer assigned, then earlier heading
            key = (score, -len(assigned[i]), i)
            if key > best_key:
                best_key = key
                best = i
        assigned[best].append(s)
    # ensure no heading is empty by stealing from the richest one
    for i, a in enumerate(assigned):
        if not a:
            donor = max(range(len(assigned)), key=lambda j: len(assigned[j]))
            if len(assigned[donor]) > 1:
                mid = len(assigned[donor]) // 2
                a.append(assigned[donor].pop(mid))
    # apply cap and redistribute overflow
    for i in range(len(assigned)):
        while len(assigned[i]) > cap:
            extra = assigned[i].pop(cap)
            donor = min(range(len(assigned)), key=lambda j: len(assigned[j]))
            assigned[donor].append(extra)
    # sort sentences within each heading by original order
    indices = {id(s): idx for idx, s in enumerate(sentences)}
    for i in range(len(assigned)):
        assigned[i].sort(key=lambda s: indices.get(id(s), 0))
    return [' '.join(a) for a in assigned]


def make_what_the_diagram_teaches(lesson, labels, color_phrases):
    explanation = lesson.get('explanation', '')
    trace = lesson.get('trace', [])
    takeaway = lesson['caseStudy'].get('takeaway', '')
    headings = [lesson['title']]
    for step in trace:
        headings.append(rephrase_step(step))
    headings.append(shorten(takeaway))
    if not headings:
        return ''
    # distribute every explanation sentence to the heading it best supports
    chunks = distribute_sentences(headings, explanation, cap=8)
    steps = [''] + list(trace) + ['']
    sections = []
    for i, h in enumerate(headings):
        body = body_for_conceptual(h, chunks[i], steps[i], lesson, labels, i)
        sections.append(f"### {i+1}. {h}\n\n{body}")
    if lesson.get('analogy'):
        tie = visual_sentence("Analogy", labels, len(headings))
        a = acme_sentence(lesson, len(headings))
        body = f"{lesson['analogy'].rstrip('.')}. {tie} {a}".rstrip('.') + '.'
        body = re.sub(r'\.\s+\.', '. ', body)
        body = re.sub(r'\.\.', '.', body)
        sections.append(f"### Analogy\n\n{body}")
    if lesson.get('nextjs'):
        intro = "The Next.js surface must own the human experience while keeping authority and secrets on the server side. In this diagram, that means the web boundary stops the coral anti-patterns before they reach the browser."
        bullets = '\n'.join(f"- {item}" for item in lesson['nextjs'])
        closing = f"Together these choices prevent the mistakes in the Acme case—{lesson['caseStudy']['situation']}—from becoming the architecture."
        sections.append(f"### The Next.js surface\n\n{intro}\n\n{bullets}\n\n{closing}")
    if lesson.get('python'):
        intro = "The Python surface must keep business rules, protocols, and persistence in cleanly separated layers. In this diagram, that means FastAPI is one edge of a domain that does not leak into adapters or the model."
        bullets = '\n'.join(f"- {item}" for item in lesson['python'])
        closing = f"These boundaries make the Acme case—{lesson['caseStudy']['situation']}—testable and replaceable."
        sections.append(f"### The Python surface\n\n{intro}\n\n{bullets}\n\n{closing}")
    return '\n\n'.join(sections)


def make_case_study(lesson):
    cs = lesson['caseStudy']
    title = shorten(cs['situation'], 4, 10) or 'Acme'
    walk = '\n'.join(f"{i+1}. {item}" for i, item in enumerate(cs.get('walkthrough', [])))
    return f"## Case study — {title}\n\n{cs['situation']}\n\n### The walkthrough\n\n{walk}\n\n### The result\n\n{cs['result']}\n\n### The danger\n\n{cs['danger']}\n\n### The takeaway\n\n{cs['takeaway']}"


def make_element_by_element(lesson, labels, color_phrases, prompt):
    lines = []
    for lab in labels:
        desc = describe_label(lab, lesson, color_phrases, prompt, labels)
        lines.append(f"- **{lab}** — {desc}")
    if not lines:
        lines.append(f"- **{lesson['title']}** — the central visual idea of the diagram.")
    return '\n'.join(lines)


def color_labels_for_phrase(phrase, all_multi):
    # extract labels in a color phrase, but do not color single words that are only subwords of a multi-word label
    candidates = re.findall(r'\b[A-Z][A-Z0-9\-]*(?:\s+[A-Z][A-Z0-9\-]*)*\b', phrase)
    out = []
    for c in candidates:
        if ' ' in c:
            out.append(c)
        else:
            if not any(re.search(r'(?<!\w)' + re.escape(c) + r'(?!\w)', mw) for mw in all_multi if ' ' in mw):
                out.append(c)
    return out


def make_color_semantics(lesson, labels, color_phrases, prompt):
    color_map = extract_color_labels(prompt, labels)
    teal_labels = list(color_map['teal'])
    coral_labels = list(color_map['coral'])
    rest = [lab for lab in labels if lab not in teal_labels and lab not in coral_labels]
    # pick structural / white / platform labels heuristically
    platform_hint = ['service','app','system','store','zone','pool','pyramid','board','kit','domain','platform','project','pack','app','web','topology','pipeline','loop']
    white_hint = ['gate','receipt','owner','record','policy','schema','fixture','test','manifest','contract','version','evidence','artifact','requirement','constraint','option','slice','document','case','slo','identity','authority','audit','proposal','decision','commit']
    cyan_hint = ['request','event','deployment','test','arrow','path','journey','command','query','flow','stream','branch','handoff','connection']
    platform_labels = [lab for lab in rest if any(h in lab.lower() for h in platform_hint)]
    if len(platform_labels) < 3:
        platform_labels = rest[:6]
    platform_labels = platform_labels[:6]
    white_labels = [lab for lab in rest if any(h in lab.lower() for h in white_hint)]
    if len(white_labels) < 3:
        white_labels = rest[:8]
    white_labels = white_labels[:8]
    cyan_labels = [lab for lab in rest if any(h in lab.lower() for h in cyan_hint)]
    if len(cyan_labels) < 2:
        cyan_labels = rest[:4]
    cyan_labels = cyan_labels[:4]
    lines = ["The course visual grammar uses color to separate platforms, requests, safe paths, danger, and records. In this diagram those colors are assigned as follows:"]
    if platform_labels:
        lines.append(f"- **Cobalt platform** — a product, service, environment, or boundary. The main structural cards such as {', '.join(f'**{l}**' for l in platform_labels)} sit on glowing cobalt platforms.")
    if cyan_labels:
        lines.append(f"- **Cyan arrow** — a typed request, event, artifact, deployment, test, or evidence handoff. The cyan paths between {', '.join(f'**{l}**' for l in cyan_labels)} carry the forward motion of the architecture.")
    if teal_labels:
        lines.append(f"- **Teal arrow** — an authoritative decision, verified contract, passing gate, safe release, or recovered service. The teal elements {', '.join(f'**{l}**' for l in teal_labels)} show the path the design wants to keep open.")
    if coral_labels:
        lines.append(f"- **Coral path** — an unacceptable outcome, failed boundary, broken contract, unsafe release, or unrecovered effect. The coral elements {', '.join(f'**{l}**' for l in coral_labels)} show what must be blocked or contained.")
    if white_labels:
        lines.append(f"- **White card** — a requirement, schema, service, test, gate, owner, artifact, or receipt. The white cards such as {', '.join(f'**{l}**' for l in white_labels)} are the readable records the diagram communicates.")
    return '\n'.join(lines)


def make_layout(lesson, labels, color_phrases):
    color_map = extract_color_labels(lesson['diagramPrompt'] + ' ' + COMPOSITIONS.get(lesson['id'], ''), labels)
    teal_labels = list(color_map['teal']) or color_phrases.get('teal', [])
    coral_labels = list(color_map['coral']) or color_phrases.get('coral', [])
    def first_label(src, default):
        for item in src:
            if isinstance(item, str) and re.search(r'\b([A-Z][A-Z0-9\-]*(?:\s+[A-Z][A-Z0-9\-]*)*)\b', item):
                m = re.search(r'\b([A-Z][A-Z0-9\-]*(?:\s+[A-Z][A-Z0-9\-]*)*)\b', item)
                return m.group(1)
        return default
    teal_label = first_label(teal_labels, 'the safe path')
    coral_label = first_label(coral_labels, 'the dangerous path')
    first = labels[0] if labels else 'the input'
    # prefer a teal label as the destination
    last_candidates = [l for l in labels if l == teal_label or l in color_map['teal']]
    if not last_candidates and len(labels) > 1:
        last_candidates = [labels[1]]
    last = last_candidates[0] if last_candidates else (labels[-1] if labels else 'the outcome')
    return f"{first} begins on the left and the diagram flows toward {last}; a teal **{teal_label}** path is the desired route and a coral **{coral_label}** path is blocked or contained."


def make_how_to_present(lesson, labels, color_phrases):
    bullets = []
    used = set()
    # open with the human problem, using a label only if it is not used again
    opening_target = labels[0] if labels else None
    if opening_target:
        used.add(opening_target)
        bullets.append(f"Point to **{opening_target}** and ask the room to state the human problem or outcome before naming any technology, protocol, or model.")
    # trace bullets: pick a relevant label for each step and ask a layered question
    for i, step in enumerate(lesson.get('trace', [])):
        tlabels = relevant_labels(step, labels, 3)
        target = None
        for t in tlabels:
            if t not in used:
                target = t
                used.add(target)
                break
        if not target and labels:
            target = labels[i % len(labels)]
            used.add(target)
        if target:
            action = step[0].lower() + step[1:]
            action = re.sub(r'\s+before writing the next layer\.?$', '', action).rstrip('.')
            qtypes = [
                f"Point to **{target}** and ask what would have to change for the team to {action}, and who would own that change.",
                f"Point to **{target}** and ask what evidence would show the team has already {action}, and what test would fail first if it is missing.",
                f"Point to **{target}** and ask who else in the room must agree before the team can {action}, and what would change their mind.",
                f"Point to **{target}** and ask what the smallest version of {action} looks like, and what would be left out of that version."
            ]
            bullets.append(qtypes[i % len(qtypes)])
    # color path bullets
    for color in ['teal', 'coral']:
        for ph in color_phrases.get(color, [])[:1]:
            if color == 'teal':
                bullets.append(f"Trace the **{color}** path ({ph}) and ask what evidence would prove the real system follows it, who collects that evidence, and how often it is refreshed.")
            else:
                bullets.append(f"Show the **{color}** path ({ph}) and ask what control, owner, or test would catch it before a user is harmed, and what the safe state would be if it is triggered.")
    # gate / rail / boundary labels
    gate_labels = [l for l in labels if any(w in l.lower() for w in ['gate','rail','policy','authority','filter','owner','control','audit','check','vault','boundary','domain','zone'])]
    for gl in gate_labels[:3]:
        bullets.append(f"Point to **{gl}** and ask who owns it, what evidence it needs, what happens when that evidence is missing, and which test proves the gate cannot be bypassed.")
    # analogy
    if lesson.get('analogy'):
        bullets.append(f"Use the analogy: {lesson['analogy']} Ask how the same failure would appear in the team's current code or process.")
    # synthesis
    bullets.append(f"Return to the whole diagram and ask the room to name one thing they will stop, one thing they will start, and one thing they will own differently before the next build.")
    # lab and checkpoint
    bullets.append(f"Run the lab: {lesson['lab']}")
    bullets.append(f"Pose the checkpoint: *{lesson['checkpoint']}*")
    return '\n'.join(f"- {b}" for b in bullets[:14])


def make_at_a_glance(lesson, labels, color_phrases):
    outcome = lesson.get('outcome', '')
    title = lesson['title']
    takeaway = lesson['caseStudy'].get('takeaway', '')
    bold = f"**{title}** — {outcome}"
    bullets = []
    if takeaway:
        bullets.append(f"The central takeaway is: {takeaway}")
    if labels:
        bullets.append(f"The visual begins with **{labels[0]}** and ends with the diagram's outcome, not a technology name.")
    for color in ['teal', 'coral']:
        for ph in color_phrases.get(color, [])[:1]:
            if color == 'teal':
                bullets.append(f"The safe or selected path is marked **{color}**: {ph}.")
            else:
                bullets.append(f"The blocked or dangerous path is marked **{color}**: {ph}.")
    if lesson.get('analogy'):
        bullets.append(f"The analogy is: {lesson['analogy']}")
    return f"{bold}\n\n" + '\n'.join(f"- {b}" for b in bullets[:5])


def make_glossary(glossary):
    lines = []
    for g in glossary:
        term, _, defn = g.partition(' - ')
        if term and defn:
            lines.append(f"- **{term.strip()}** — {defn.strip()}")
        else:
            lines.append(f"- {g}")
    return '\n'.join(lines)


def make_sources(sources):
    return '\n'.join(f"- {s}" for s in sources)


def make_related(lesson, lessons_by_id):
    rel = lesson.get('related')
    if not rel:
        return None
    lines = ["## Related lessons", ""]
    for rid in rel:
        other = lessons_by_id.get(rid)
        if other:
            lines.append(f"- **Lesson {rid}** — {other['title']} (`{other['slug']}`)")
        else:
            lines.append(f"- **Lesson {rid}**")
    return '\n'.join(lines)


def make_article(lesson, lessons_by_id):
    module = modules.get(lesson['moduleId'], {})
    module_title = module.get('title', 'Unknown module')
    prompt = lesson['diagramPrompt'] + ' ' + COMPOSITIONS.get(lesson['id'], '')
    labels = extract_labels(prompt)
    color_phrases = extract_color_phrases(prompt)

    parts = [
        f"# Diagram {lesson['id']} — {lesson['title']}",
        "",
        f"![{lesson['alt']}](../{lesson['diagram']})",
        "",
        f"**Module:** {module_title}",
        f"**Role in the course:** {lesson['outcome']}",
        f"**Layout:** {make_layout(lesson, labels, color_phrases)}",
        "",
        "---",
        "",
        "## At a glance",
        "",
        make_at_a_glance(lesson, labels, color_phrases),
        "",
        "---",
        "",
        "## What the diagram teaches",
        "",
        make_what_the_diagram_teaches(lesson, labels, color_phrases),
        "",
        "---",
        "",
        make_case_study(lesson),
        "",
        "---",
        "",
        "## Composition",
        "",
        COMPOSITIONS.get(lesson['id'], f"The picture shows the {lesson['title']} laid out on the course's dark midnight-navy background, with labeled cobalt platforms, cyan arrows, teal safe paths, coral danger paths, and white cards."),
        "",
        "## Element by element",
        "",
        make_element_by_element(lesson, labels, color_phrases, prompt),
        "",
        "---",
        "",
        "## Colour and flow semantics",
        "",
        make_color_semantics(lesson, labels, color_phrases, prompt),
        "",
        "---",
        "",
        "## How to present it",
        "",
        make_how_to_present(lesson, labels, color_phrases),
        "",
        "---",
        "",
        "## Lab and checkpoint",
        "",
        f"**Lab:** {lesson['lab']}",
        "",
        f"**Checkpoint:** {lesson['checkpoint']}",
        "",
        f"**Answer:** {lesson['answer']}",
        "",
        "---",
        "",
        "## Glossary",
        "",
        make_glossary(lesson.get('glossary', [])),
        "",
        "---",
        "",
        "## Sources",
        "",
        make_sources(lesson.get('sources', [])),
    ]

    related = make_related(lesson, lessons_by_id)
    if related:
        parts.extend(["", "---", "", related])

    article = '\n'.join(parts)

    # ensure minimum word count with a concise, non-repetitive build contract
    if word_count(article) < 2500:
        trace_list = '; '.join(lesson.get('trace', []))
        extra = [
            "",
            "---",
            "",
            "### Why this diagram must precede the build",
            "",
            f"The team should not begin with code, prompts, or models for {lesson['title']} until the diagram is legible to every reviewer. {lesson['outcome']} The trace moves through {len(lesson.get('trace', []))} decisions: {trace_list}. Each decision maps to a labeled element in the picture, and each label must have an owner, a contract, and an acceptance test before the corresponding code is written.",
            "",
            f"The case study—{lesson['caseStudy']['situation']}—shows that {lesson['caseStudy']['takeaway']} If the team skips this, {lesson['caseStudy']['danger']} The diagram is the contract the two projects share. Until the team can trace the problem through the labels, assign owners to each card, and write the corresponding test, the build will drift from the architecture.",
            "",
            f"Before writing the first route, prompt, or adapter, the team should be able to answer: what is the user outcome this diagram protects, which card owns each decision, what evidence moves across each arrow, where the coral anti-patterns first appear, what test or gate proves the real system matches the picture, and which fixture will catch the next regression. When those answers are visible and reviewable, the build becomes a direct translation of the architecture rather than a guess about it. The diagram is the earliest acceptance test the project can write. Keeping it current is cheaper than debugging the drift it prevents. A reviewer who cannot read the diagram will not be able to read the build. Start every build review by pointing at the diagram, not the code.",
        ]
        article += '\n'.join(extra)

    return article


def main():
    lessons_by_id = {l['id']: l for l in lessons}
    counts = {}
    for lesson in lessons:
        if not (221 <= lesson['id'] <= 244):
            continue
        article = make_article(lesson, lessons_by_id)
        path = OUT / f"{lesson['id']:03d}-{lesson['slug']}.md"
        path.write_text(article, encoding='utf-8')
        counts[lesson['id']] = word_count(article)
        print(f"Wrote {path.name} ({counts[lesson['id']]} words)")
    print("Done.")


if __name__ == '__main__':
    main()
