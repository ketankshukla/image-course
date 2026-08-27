# Workbook 2 — Build the MCP Operations Gateway

## P1: turn business functions into controlled tools

**Outcome:** an MCP client can discover tools, read an authorized account snapshot, and request an approved simulated credit. Repeating a completed command returns its original receipt. A model is not needed to prove any of this.

Prerequisite: the foundations workbook. During this workbook, a trusted test fixture supplies execution grants. P4 later replaces that fixture with the real approval workflow. Never expose the fixture grant-creation helper as a public endpoint.

## 1. At a glance

![An MCP adapter receives a command, enforces authority, and calls a transactional domain service. A receipt confirms the committed result; repeated matching requests recover that receipt.](../architecture-assets/02-mcp-safe-write.png)

MCP is the protocol wrapper around a capability. The domain function is the rule behind that capability. We write the rule first so changing the protocol SDK does not change the meaning of a credit.

The diagram's authorization stage is not the only check. Any facts that could change concurrently—grant consumption, remaining balance, business uniqueness—must be checked again inside the database transaction.

## 2. Create files in this order

All Python module paths below start at `backend/src/acme`. Tests live under `backend/tests`.

| Order | File | Public functions/types | Responsibility |
|---|---|---|---|
| 1 | `contracts/credit.py` | `CreditCommand`, `CreditReceipt` | Strict command and response shapes |
| 2 | `domain/canonical.py` | `canonical_credit_payload(command)` | Stable comparison of the approved action |
| 3 | `domain/credit_rules.py` | `validate_credit(command, account, grant, now)` | All non-I/O business checks |
| 4 | `domain/credit_repository.py` | `find_operation`, `lock_account`, `lock_grant`, `insert_credit` | Parameterized SQL only |
| 5 | `domain/credit_service.py` | `issue_credit(command, actor, connection)` | One transaction, one outcome |
| 6 | `mcp_gateway/tools.py` | `lookup_account_tool`, `issue_credit_tool`, `get_receipt_tool` | Translate protocol inputs/results |
| 7 | `mcp_gateway/server.py` | `create_server(settings, dependencies)` | SDK registration, transport, verified identity |
| 8 | `lab/mcp_client.py` | `run_gateway_scenario(client)` | Discover and invoke real tools |

Create package `__init__.py` files as you add directories. Keep SQL out of `tools.py` and SDK types out of `credit_rules.py`.

## 3. Define the command before the tool

A `CreditCommand` needs tenant, case, account, proposal revision, amount in minor units, currency, operation key, and grant identifier. Reject unknown fields and invalid ranges. The trusted actor comes from authentication context, not from a user-writable field in this command.

`canonical_credit_payload` selects the action-defining fields in a documented order and serializes them consistently. Exclude trace IDs and changing transport timestamps. Include tenant, account, action, amount, currency, and proposal/evidence bindings. Use the same canonicalization contract in both languages; test it with golden JSON examples.

Hashing is useful for comparing payloads, but a hash does not authorize anything. The server loads the recorded grant and independently verifies the binding.

### Small typeable rule exercise

Create `domain/credit_rules.py` with this first pure function:

```python
def validate_credit_amount(amount_minor: int, available_minor: int) -> None:
    if type(amount_minor) is not int or type(available_minor) is not int:
        raise TypeError("Expected integer minor units")
    if available_minor < 0:
        raise ValueError("Invalid available balance")
    if amount_minor <= 0:
        raise ValueError("Credit must be positive")
    if amount_minor > available_minor:
        raise ValueError("Credit exceeds available amount")
```

This function returns nothing on success. Its output is either “checks passed” or an exception. It neither saves a credit nor consumes an approval. Test 7500 against 12000, zero, negative input, an excessive amount, and a Boolean before adding identity or persistence.

## 4. Write the schema with constraints

Add a migration for accounts, execution grants, operations, credits, receipts, and an operations outbox. Every business row carries a tenant identifier.

| Table | Critical fields and constraints |
|---|---|
| Accounts | Tenant/account key; current charge or eligible balance; revision |
| Grants | Grant ID; exact payload digest; expiry; consumption reference |
| Operations | Tenant + operation key unique; canonical payload; receipt reference |
| Credits | Positive amount; currency; business adjustment identity unique |
| Receipts | Receipt ID unique; credit ID unique; immutable recorded amount |
| Outbox | Event ID unique; aggregate ID; payload; delivery state |

The business adjustment identity should represent the approved adjustment itself, such as tenant, case, proposal revision, and action. Do not use amount alone: two legitimate credits can have the same amount.

Make immutable fields immutable through service permissions and update rules. A receipt is not a row that every worker can rewrite after the fact. Cross-tenant foreign keys must not permit a grant from one tenant to reference another tenant's credit.

## 5. Implement the transaction, step by step

Write `issue_credit` as an application algorithm in this order:

1. Authenticate upstream and require execution scope for the target tenant.
2. Begin a database transaction.
3. Serialize contenders for this tenant/operation key, using a transaction-scoped lock or an insert/unique-conflict design with a documented retry path.
4. Look up the operation. If completed with the same canonical payload, return its original receipt to the authorized caller. If the payload differs, reject the conflict.
5. For a new operation, lock the account and grant in a consistent order.
6. Verify tenant, account, action binding, revision, expiry, unused grant, and remaining permitted amount.
7. Enforce business uniqueness independently of the operation key.
8. Insert operation, credit, and receipt; consume the grant; update the account if required; insert the outbox event.
9. Commit. Return the receipt only after successful commit.

Do not keep a database transaction open while waiting for a model or a human. Every external decision has already been recorded before this short transaction starts.

For two simultaneous identical requests, the losing request must recover the committed operation, not return an unexplained database exception. If you use a unique constraint to detect the race, roll back the failed transaction before re-reading. Test the behavior with two independent database connections.

## 6. Separate lookup from mutation

`lookup_account_tool` accepts an account ID, derives the tenant from verified context, authorizes access, and returns only safe fields. Its database role must not write the ledger.

`get_receipt_tool` checks caller access to the tenant and case before revealing a receipt. Guessing an operation key is not permission to read another customer's result.

`issue_credit_tool` validates the protocol input and delegates to `issue_credit`. It translates expected domain exceptions into stable tool errors. It must not catch every exception and return “success” with an error hidden inside a string.

Choose explicit error categories: invalid input, forbidden, stale proposal, expired grant, key conflict, insufficient balance, and temporarily unavailable. Only the last category is automatically retryable, and an uncertain response must preserve the same operation key.

## 7. Add the actual MCP server and client

Install a pinned official MCP Python SDK release in the new application's dependency file. Its high-level server APIs can expose tools over supported transports, including Streamable HTTP. Use the installed release's examples because names and configuration can change. Do not mix a separate similarly named package with the official SDK unintentionally. [Official MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk), [HTTP integration](https://py.sdk.modelcontextprotocol.io/run/asgi/).

Implement `create_server`: construct dependencies once, register the three tools, configure the HTTP transport, and connect verified request identity to each invocation. Start on loopback during development. A session ID is not a user identity, and a tool description is not an authorization policy.

In `lab/mcp_client.py`, connect through the SDK client, initialize the session when required, list tools, validate their advertised schemas, call lookup, and inspect the structured result. Then invoke the approved-credit scenario. A direct call to the Python function is a unit test, not a protocol test.

Before public hosting, implement and test the selected MCP authentication requirements, token validation, audience/scope checks, origin/host protections, and connection cleanup. Bind no unauthenticated write-capable demonstration to a public address.

## 8. Your test ladder

| Test file | Scenario | Required assertion |
|---|---|---|
| `test_credit_rules.py` | Invalid and valid amounts | Invalid inputs cannot pass |
| `test_credit_service.py` | Valid fixture grant | One credit, one receipt, grant consumed |
| `test_credit_idempotency.py` | Same key and same payload | Same receipt identifier |
| `test_credit_conflict.py` | Same key, changed amount | Conflict and unchanged ledger |
| `test_credit_concurrency.py` | Two connections race | One business adjustment |
| `test_credit_rollback.py` | Fail before commit | No partial credit or consumed grant |
| `test_mcp_protocol.py` | Real client/server exchange | Tool schema and result match contract |
| `test_mcp_security.py` | Wrong tenant or Finance identity writes | Denied before mutation |

Use `python -m pytest -q` from the configured backend environment. For integration tests, start an isolated database and server using the entry point you implemented; record that command in the project's README rather than guessing a framework CLI.

## 9. Failure lab: lose the response

Add a test-only fault hook immediately after commit but before returning the receipt. Trigger it for one synthetic operation. Restart the client and retry the same payload and key. Inspect the database: credit count is one and the receipt ID is unchanged.

Disable the hook outside the local/test configuration. Do not create a public “crash server” endpoint. The exercise teaches that a timeout is an unknown outcome, not proof that nothing happened.

## 10. TypeScript implementation path

Create `packages/contracts/src/credit.ts`, `packages/operations-domain/src/credit-rules.ts`, `credit-repository.ts`, `issue-credit.ts`, and `apps/mcp-service/src/tools.ts` in that order. Functions become `validateCreditAmount`, `canonicalCreditPayload`, and `issueCredit`.

Use safe-integer validation, parameterized SQL, and an explicit transaction connection. Do not launch transaction queries on different pooled connections. Use the official TypeScript MCP server adapter for the pinned release and preserve the same tool contracts. The repository function may be async, but the validation function should remain synchronous and pure.

Run the same concurrency and response-loss tests. Shared types do not prove the protocol or transaction works; only the real client/server and database tests do.

## 11. Completion and presentation

P1 is complete when the three tools work through a real MCP client, forbidden writes fail, concurrent retries produce one adjustment, and a response-loss retry recovers the receipt. The service must have a health check, restricted credentials, configurable timeouts, and no public fixture-grant shortcut before deployment.

Explain it aloud: **“The protocol exposes the tool, but the database transaction enforces the action. The receipt—not the model's answer—is proof.”**
