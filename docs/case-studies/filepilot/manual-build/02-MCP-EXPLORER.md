# Build FilePilot — The Read-Only MCP Explorer

## At a glance

Create a useful explorer before creating a writer. It should inventory an approved sandbox, return bounded previews, and identify duplicate candidates without changing anything. Test the Python services directly, then expose the same behavior through MCP.

## What the diagram teaches

![The explorer supplies observations, while the operations engine is the only writer. Protocol access does not bypass the coordinator's contracts or root permissions.](../assets/architecture.svg)

Maya grants ROOT-DEMO. A tool call requests a scan of that identifier. The service looks up the real root internally, checks current authorization, and walks only supported entries. Returning a root ID from a UI does not establish that a caller is authorized to use it; the server must bind it to the caller's grant.

The tool returns a scan ID and summary. Large inventories should be paginated and cancellable. A skipped locked or inaccessible file appears as a skipped entry with a safe reason, not as proof that the folder was completely inspected.

## 1. Create the modules in this order

| File | Functions | Contract |
|---|---|---|
| `roots.py` | `authorize_root(principal, root_id)` | Return a current grant or deny |
| `adapters/filesystem_windows.py` | `inspect_entry`, `iter_entries` | Read-only observations; no recursive link following |
| `fingerprints.py` | `fingerprint(file_handle)` | Hash bounded file bytes and record identity metadata |
| `inventory.py` | `scan_root`, `list_scan_files` | Persist stable records and skipped-entry reasons |
| `adapters/mcp_server.py` | Tool wrappers | Validate protocol input and call these services |

Do not open a path first and authorize it afterward. Check the root and entry policy before reading content. Bound traversal depth, entry count, total bytes hashed, preview size, and elapsed time. Report when a limit is reached.

## 2. Define a narrow tool surface

Use application-specific tool names such as `scan_root`, `list_files`, `preview_text`, and `find_duplicate_candidates`. Their arguments reference granted roots, scan IDs, or file IDs. Do not provide `run_shell`, `read_any_path`, or `execute_python` as shortcuts.

The tool result should contain structured records and safe errors. A preview should include a source revision and truncation indicator. An error should not echo a full private path or document contents into an assistant transcript. Tool descriptions are useful guidance, but the service enforces the rules regardless of the caller's interpretation.

For an initial local integration, an MCP client can launch the server over stdio. Keep diagnostic logging off the protocol stream. Local subprocesses still have operating-system privileges; using MCP does not automatically sandbox them. Pin the SDK and use its matching examples instead of mixing APIs from unrelated versions. The [MCP security notes](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/SECURITY.md) explain this local execution boundary.

## 3. Detect duplicate candidates carefully

Group regular files by size, then compare content hashes for candidate matches. For an exact-duplicate claim, confirm matching bytes using bounded chunk comparisons on stable observations. Treat changing files as unstable and exclude them from the result.

An exact content match does not mean the files are interchangeable in their projects. A document may be intentionally duplicated or referenced by another file. The tool reports a group; the planner may propose a review-folder move; the user decides. No duplicate tool deletes anything.

Do not call similar documents duplicates. “Same filename,” “similar text,” “same hash,” and “same filesystem identity through a hard link” are different observations. Keep those categories separate in both data and explanation.

## 4. Test through the real adapter

Create protocol tests for unknown root IDs, another principal's scan ID, oversized previews, unsupported file types, and cancellation. Test a junction escape in a disposable fixture tree and verify that no outside bytes are returned. Where a runner cannot create a particular Windows fixture, record an explicit skipped test; do not report that boundary as passed.

Also test that read-only module imports do not expose mutation commands. A direct MCP call should fail exactly as a direct Python service call does. Test malformed input through the actual server rather than testing only the happy-path function.

## Acceptance gate and demonstration

Show inventory, one preview, one duplicate group, and one denial. Explain that the scan is an observation of a particular moment. You should be able to unplug the model entirely and still demonstrate all four behaviors.
