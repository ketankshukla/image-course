# Agent Architecture — Narration Script

Course 1 · Lesson 1. Review draft: slides and spoken script only; no audio or presenter has been generated.

15 slides · 1795 spoken words · approximately 13–15 minutes at 120–140 words per minute, plus learner pauses.

Pronunciation: MCP = “em see pee”; A2A = “ay two ay”; RAG = “rag”; idempotency = “eye-dem-POH-ten-see.” Read shipment 4471 as “four four seven one.” The Northwind Freight case and all amounts are fictional.

## Slide 01 — An agent needs more than a model

### Narration

Imagine an assistant that sounds helpful, understands your question, and confidently says it has solved your problem. There is still something important you do not know. Did it use the right information? Was it allowed to make the change? And can you see evidence that the change actually happened? This lesson is about the system around the model. We will follow one request from a person, through an application agent, into tools and a specialist, and finally to the rules that protect a real business system. You do not need to know the protocols yet. By the end, you should be able to explain what each part does, where a request can be refused, and why the answer needs a receipt.

### Visual cue — not spoken

Hold the opening title. Let the three short lines establish the lesson's promise.

## Slide 02 — Follow the arrows, not just the boxes

### Narration

Here is our map. On the left is the person who wants something done. The application agent is the software they talk to. MCP capabilities are the tools and information interfaces that the application can use. An A2A specialist represents work delegated to another agent. Domain and policy mean the actual business system and the rules governing it. Now look underneath the boxes. That dashed line brings evidence back to the person. If you removed it, work might still happen, but the person could not reliably tell what happened. One warning before we go further: this row is a teaching map, not a mandatory sequence. An application does not have to call an MCP tool before it can contact another agent. We will revisit that shortly.

### Visual cue — not spoken

Show the original diagram in full. Trace left to right, then point out the dashed return path.

## Slide 03 — One request hides several decisions

### Narration

Meet Priya, an operations coordinator at our fictional company, Northwind Freight. A customer wants a credit because a shipment arrived late. Priya asks one simple question, but that question contains several jobs. Someone must investigate the delay, read the contract, look at previous credits, and decide what response is appropriate. There is also a hidden permission question: what is Priya allowed to approve? All names, shipment details and dollar amounts in this example are invented for teaching. We are not describing a measured customer deployment. Keep that distinction in mind as we walk through the system. The point is to make the architecture concrete, not to claim that a real company achieved these results.

### Visual cue — not spoken

Read the request naturally. Emphasize the difference between finding facts and authorizing money.

## Slide 04 — The application agent organizes the work

### Narration

The application agent is the coordinator, not the owner of every decision. It turns Priya's request into a plan. First, establish the facts. Next, ask the appropriate specialist to assess credit eligibility. Finally, return a recommendation with evidence. Notice what is missing from this plan: automatically issuing money. Understanding a request does not create authority to act on it. A good plan also recognizes uncertainty. If the shipment number is ambiguous, ask for clarification. If the contract is unavailable, say what is missing. Planning is where a vague sentence becomes a set of checkable tasks. It is also where the application decides that a finance decision belongs with finance, rather than quietly guessing the rules itself.

### Visual cue — not spoken

Reveal the three responsibilities in order. Pause on 'no automatic payment'.

## Slide 05 — Tools retrieve facts within a boundary

### Narration

MCP stands for Model Context Protocol. For this lesson, think of it as a standard way for an application to discover and use capabilities exposed by a server. Our example exposes four reading tools. Each one has a defined input and returns a specific kind of information. The application should validate the arguments and the user's access before retrieving the records. We deliberately do not expose an issue-credit tool at this stage. That is our application design, not an automatic property of MCP. MCP tools can perform writes, take time, or invoke complex services. And read-only access is not harmless: reading the wrong customer's private data is still a serious failure. The useful boundary is a narrow, authorized interface whose behavior we can inspect.

### Visual cue — not spoken

Point to each tool name and translate it into its plain-English question.

## Slide 06 — A specialist receives a bounded task

### Narration

Now the application asks a finance specialist to assess eligibility. A2A means Agent-to-Agent. It supports cooperation between agents that may be operated by different teams or systems. In our example, the application sends a bounded task: assess this shipment using these evidence items, then return a recommendation and explanation. It does not send Priya's credentials or her entire conversation. The specialist may return an answer, request more information, or report that it cannot complete the task. If there is a task identifier, use it to check that task's status instead of blindly creating another copy. The key distinction here is responsibility: the specialist owns its assessment, but the business system still owns permission to issue the credit.

### Visual cue — not spoken

Contrast the narrow retrieval request with the delegated outcome. Do not imply every tool is simple or every A2A request is long-running.

## Slide 07 — Approval and authorization are different

### Narration

Suppose the specialist recommends a three-hundred-and-forty-dollar credit. In our fictional policy, Priya may approve credits up to five hundred dollars. Two different checks are needed. Confirmation asks whether Priya actually wants this particular action. Authorization asks whether the rules allow her to perform it. Clicking Approve does not override the rules. If the recommendation were nine hundred dollars, the backend would refuse Priya's approval and route the request to an authorized supervisor. These checks belong in ordinary application code at the protected operation, not only in the model's instructions. We also check permissions earlier, when data is read or a task is delegated. The final write boundary is especially important, but it is not the only place where security belongs.

### Visual cue — not spoken

Read the two amounts, then introduce the $900 counterexample. State that these are fictional policy values.

## Slide 08 — A safe change leaves a receipt

### Narration

The next diagram makes a safe change explicit. First, confirm the exact action with the person. Second, authorize that action against current rules. Third, attach an idempotency key. That long word means we can recognize the same intended operation when it is retried. Fourth, commit the change and record its result. The key is not magic. The receiving service must actually enforce deduplication, and the application must use the same key for a retry of the same operation. Approval should be tied to the exact amount and version being reviewed. If those details change, ask for approval again. Together, these controls turn a plausible recommendation into a governed action that can later be explained.

### Visual cue — not spoken

Walk through the four panels. Explain the technical term before using it again.

## Slide 09 — A retry must not become a second credit

### Narration

Here is the failure that makes this important. Imagine the billing service commits the credit, but its response never reaches the assistant. From the assistant's point of view, the request timed out. That does not prove the credit failed. If the assistant sends a new operation, it could issue a second credit. Instead, it retries with the same operation key, and the receiving service returns the original result under its deduplication rules. In a real system, you also need to understand the key's scope, retention period and behavior when the parameters differ. This is a hypothetical failure exercise, not an incident report. The lesson is simple: reliable retry behavior is something engineers implement and test. It does not come automatically from using an agent.

### Visual cue — not spoken

Follow the simple three-part sequence. Emphasize that the response can fail after the action succeeds.

## Slide 10 — The human needs evidence, not “Done”

### Narration

Now we can explain the dashed return line in practical terms. Priya should see what happened, which shipment it affected, who approved it, and where to find the supporting record. The system should distinguish a recommendation, a pending action, a confirmed success and a failure. A generic Done message hides those differences. The receipt also helps someone investigate the decision later without reconstructing a conversation from memory. Do not expose private evidence to everyone just because it appears in an audit record; receipts and logs need access controls too. The return path is not decoration. It makes the result understandable to the person who asked, and it gives the organization a way to inspect what the application actually did.

### Visual cue — not spoken

Show the receipt fields as the practical meaning of the dashed line from the opening diagram.

## Slide 11 — Real requests can take different routes

### Narration

Let us correct the straight-line impression from the first diagram. Here the application has several routes. It can retrieve relevant knowledge, call a capability, or delegate work to another agent. Retrieval-augmented generation, often shortened to RAG, means finding relevant material to help ground an answer. These routes are not necessarily exclusive. The application might retrieve a contract and then ask a specialist to interpret the case. Or it may answer a simple status question without delegation or a write. MCP and A2A are useful interfaces, not compulsory ingredients for every application. The architecture you choose should match the task. What remains essential is that data access and consequential actions stay within their permission boundaries, and the user receives an honest account of the result.

### Visual cue — not spoken

Show the three parallel lanes. Explain that they are choices and may be combined.

## Slide 12 — Planning and verification need owners

### Narration

This companion picture describes the work as verbs: ask, plan, retrieve, act, delegate and verify. Treat these as responsibilities, not as a rigid execution order. You may delegate before acting, and many requests should never perform a write at all. Two responsibilities deserve special attention: planning and verification. They do not need their own service box, but they do need an owner. Planning decides which steps are justified. Verification checks whether the intended outcome is supported by actual results. A model saying the job succeeded is not enough. Check the authoritative record, the returned artifact and the operation status. If the result is uncertain, report uncertainty rather than converting it into a confident success message.

### Visual cue — not spoken

Emphasize PLAN and VERIFY. Explain that the pictured order is illustrative, not mandatory.

## Slide 13 — Ask three questions at every boundary

### Narration

You can now review an agent design without memorizing every acronym. At each boundary, ask three questions. What crosses it? What can be refused there? And what evidence does the crossing produce? If you remove permission checks, the wrong user may reach the data. If you remove the approval boundary, a recommendation can turn into an unauthorized action. If you remove retry protection, one action can become two. If you remove the return path, a failure may remain invisible. One important nuance: removing MCP itself does not automatically remove safety. Ordinary APIs can enforce the same controls. The protocol standardizes an interface; the control is the rule your system actually enforces. Evaluate both rather than confusing one with the other.

### Visual cue — not spoken

Use the three questions as a reusable architecture-review checklist.

## Slide 14 — What should the assistant do next?

### Narration

Let us test the architecture with two short questions. First, the specialist recommends a nine-hundred-dollar credit. Priya clicks Approve, but her limit is five hundred dollars. Should the backend issue the credit because both the specialist and Priya agree? Second, imagine a different credit that is properly authorized. Its write request times out, and the application does not know whether it succeeded. Should it create a new operation key and try again? Pause here and explain your answers in your own words. You are not being tested on vocabulary. You are checking whether you can separate a recommendation from authority, and a missing response from a failed action.

### Visual cue — not spoken

Pause for the learner to answer both questions before moving to the final slide.

## Slide 15 — Useful work. Controlled actions. Evidence.

### Narration

The nine-hundred-dollar credit must not be issued under Priya's authority. The backend should reject that action and direct it to someone who can approve it. For the uncertain retry, preserve the identity of the original operation and use the receiving system's supported recovery and deduplication behavior. Do not invent a fresh identity just because the response was lost. That brings us back to the opening question. A capable model is only one part of a trustworthy application. People express intent. Applications organize work. Tools provide capabilities. Specialists contribute assessments. Business rules govern consequential changes. Evidence closes the loop. Take one system you know and label its boundaries: what crosses, what can be refused, and what gets recorded. If you can answer those three questions clearly, you are already reasoning like a system designer.

### Visual cue — not spoken

Resolve both questions, then invite the learner to apply the boundary checklist to a project they understand.

## Source and adaptation notes

Adapted from the supplied Course 1, Lesson 1 document and its original diagrams. Unverified deployment anecdotes were replaced with explicitly fictional examples. The presentation distinguishes protocols from application-enforced security, and treats depicted orders as illustrative.

- [MCP architecture](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture)
- [A2A overview](https://a2a-protocol.org/latest/topics/what-is-a2a/)

Official references checked 28 August 2026. Sources are also included in the PowerPoint speaker notes.
