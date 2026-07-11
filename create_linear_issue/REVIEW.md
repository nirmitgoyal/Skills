# Trust Packet Review

## Summary

Draft review packet for `create_linear_issue`.

## Source Inventory

Approved source bundle hash: `sha256:c112b225f2ad213fbd68e2f1a62396c72fcae7ae31c09faad52f34cbd80b4141`

## Policy Claims

- claim_1_test_001: Eligible when User posts 'Need sentry integration @Linear create task' in the bugs channel. The bot should create a Linear issue titled 'Add support for sentry integration' (or similar derivation) and reply with a URL such as https://linear.app/.../SEM-92, with no assignee set. Evidence: src_slack_c0akplfbepl_1774894444782179.
- claim_2_test_002: Eligible when User posts '@Linear create bug issues from these and assign to @Nirmit Goyal' with 'linear integration is failing' as the bug description. The bot should create a Linear issue (e.g., SEM-120) assigned to Nirmit Goyal and reply with the issue URL. Evidence: src_slack_c0akplfbepl_1775264807261759.
- claim_3_test_003: Ineligible when A user in a different Slack workspace attempts to invoke the @Linear bot that is registered to the Semantic Search workspace. The bot must refuse with 'Sorry, you can’t message this instance of @Linear as it belongs to the Semantic Search workspace.' and must NOT create any Linear issue. Evidence: src_slack_c0akplfbepl_1775264807261759.
- claim_4_test_004: Ineligible when User posts '@Linear create task' with no preceding or following bug description text. Because the required 'bug_description' field is absent, the bot must not create an issue and should prompt the user to provide a description. No evidence of successful creation without description text in the source data.
- claim_5_test_005: Escalate when User posts 'Search is broken @Linear create task assign to @UnknownUser'. The bot can parse the create command and bug description, but cannot resolve '@UnknownUser' to a Linear team member. The bot should escalate back to the requester asking for a valid Linear assignee before or after creating the issue unassigned.
- claim_6_test_006: Escalate when The same bug description (e.g., 'Slack not integrated') is submitted twice in quick succession via '@Linear create task'. The first invocation creates SEM-93. The second invocation should be flagged as a potential duplicate and escalated for human triage rather than creating a second identical issue. Evidence pattern: src_slack_c0akplfbepl_1774894458850489 shows double invocation in the thread.
- claim_7_test_007: Eligible when User posts 'taking too much time to search across all connectors @Linear create task'. The bot should create a Linear issue with a title derived from the description (e.g., 'Search across all connectors is too slow', matching SEM-94) and reply with the issue URL. Evidence: src_slack_c0akplfbepl_1774894474554329.

## Required Fields

- bug_description
- assignee_mention

## Edge Cases

- Command typed twice in the same message (e.g., '@Linear create task @Linear create task') should result in only one issue being created, not two.
- Bug description that is purely a URL or contains no human-readable text may produce a poor issue title; the bot should use the raw text as the title fallback.
- If the assignee is mentioned before the create command rather than after, the bot should still parse and assign correctly.
- Slack message edits after issue creation should not trigger a second issue creation.
- If the Linear API is unavailable, the bot must not silently fail; it must surface an error to the user and flag for escalation.
- Messages in threads vs. top-level channel posts should both be supported as valid invocation surfaces.
- Issue titles auto-derived from very long descriptions should be truncated to Linear's title character limit without losing the core bug signal.
- test_001: Standard create task with description only -> pass
- test_002: Create bug with explicit assignee mention -> pass
- test_003: Cross-workspace bot invocation -> pass
- test_004: Missing bug description after create command -> pass
- test_005: Assignee mention resolves to unknown Linear user -> pass
- test_006: Rapid duplicate submission of same bug description -> pass
- test_007: Multi-word performance bug creates correctly titled issue -> pass

## Test Results

Generated deterministic pilot tests are included under `tests/`.

## Deterministic Calls Linear Api From Slack Bot Integration Install/Test Instructions

Runtime profile: `runtimes/deterministic_calls_linear_api_from_slack_bot_integration.md`

Owner: `[redacted-email]`

Install Instructions

1. Install the Linear Slack app in the target Slack workspace and authorize it with a Linear API key scoped to the relevant team. 2. Invite @Linear to the #bugs channel. 3. Configure the Slack bot to listen for messages matching the pattern '@Linear create (task|bug)' in #bugs. 4. Store the Linear team ID and default project ID as environment variables for the bot runtime. 5. Ensure the bot's OAuth token has permission to resolve Slack @mentions to Linear user accounts via the Linear user list API. 6. Deploy the bot runtime with the idempotency check (60-second deduplication window) enabled. 7. Set up an error alerting webhook to notify the workspace admin on Linear API failures.

Test Instructions

1. In the #bugs channel, post 'Test connectivity issue @Linear create task' and verify a new Linear issue is created with a derived title and a confirmation URL is returned in the thread. 2. Post '@Linear create task assign to @[valid Linear user]' and verify the created issue has the correct assignee in Linear. 3. Attempt to invoke the bot from a different Slack workspace and confirm the cross-workspace refusal message appears and no issue is created. 4. Post the same bug description twice within 30 seconds and confirm only one issue is created (idempotency test). 5. Post '@Linear create task' with no description text and confirm no issue is created and the bot prompts for a description. 6. Simulate a Linear API 500 error and confirm the bot surfaces an error message to the user rather than silently failing. 7. Check the Linear issue list to confirm all test issues carry the 'slack-bug-report' label and the correct source metadata.

## Runtime Lock

Do not install or activate the skill; runtime use remains locked pending reviewed/import verification.

## Merge Risks

This is a draft and must not be treated as ready until GitHub validation and reviewed/import verification land in later phases.

## Reviewer Checklist

- Confirm approved sources.
- Confirm decision rules, required fields, and deterministic tests.
- Confirm runtime lock and reviewer-safe output.

## Next Reviewer Action

Verify the approved sources, decision rules, required fields, runtime lock, and reviewer-safe output.
