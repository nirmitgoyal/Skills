# Edge Cases

- Command typed twice in the same message (e.g., '@Linear create task @Linear create task') should result in only one issue being created, not two.
- Bug description that is purely a URL or contains no human-readable text may produce a poor issue title; the bot should use the raw text as the title fallback.
- If the assignee is mentioned before the create command rather than after, the bot should still parse and assign correctly.
- Slack message edits after issue creation should not trigger a second issue creation.
- If the Linear API is unavailable, the bot must not silently fail; it must surface an error to the user and flag for escalation.
- Messages in threads vs. top-level channel posts should both be supported as valid invocation surfaces.
- Issue titles auto-derived from very long descriptions should be truncated to Linear's title character limit without losing the core bug signal.

- `Standard create task with description only` -> `eligible`
- `Create bug with explicit assignee mention` -> `eligible`
- `Cross-workspace bot invocation` -> `ineligible`
- `Missing bug description after create command` -> `ineligible`
- `Assignee mention resolves to unknown Linear user` -> `needs_escalation`
- `Rapid duplicate submission of same bug description` -> `needs_escalation`
- `Multi-word performance bug creates correctly titled issue` -> `eligible`
