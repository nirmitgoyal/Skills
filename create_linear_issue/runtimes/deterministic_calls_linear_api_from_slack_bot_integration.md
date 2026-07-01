# Deterministic Calls Linear Api From Slack Bot Integration Runtime Profile

## Guidance

Parse the Slack message to extract the bug_description as all text preceding the '@Linear create' invocation token.

Parse the Slack message for an 'assign to @User' or 'assign @User' pattern after the create command to populate the assignee field.

Call the Linear API createIssue mutation with: title (derived from bug_description), description (full raw message text), and assignee (resolved Linear user ID if present).

On successful issue creation, reply in the same Slack thread with the formatted message: 'Created issue <Linear URL|ISSUE-ID>'.

On cross-workspace refusal from the Linear bot, surface the exact error message to the user and log the attempt.

On assignee resolution failure, either create the issue unassigned and notify the requester, or hold creation and escalate — do not silently drop the assignee.

Idempotency check: before calling createIssue, query for an existing open issue with an identical title in the same team created within the last 60 seconds; if found, skip creation and return the existing URL.

All created issues should be tagged with the source label 'slack-bug-report' for traceability.

Log the source Slack message timestamp and channel ID alongside the created Linear issue ID for audit purposes.

## Install Instructions

1. Install the Linear Slack app in the target Slack workspace and authorize it with a Linear API key scoped to the relevant team. 2. Invite @Linear to the #bugs channel. 3. Configure the Slack bot to listen for messages matching the pattern '@Linear create (task|bug)' in #bugs. 4. Store the Linear team ID and default project ID as environment variables for the bot runtime. 5. Ensure the bot's OAuth token has permission to resolve Slack @mentions to Linear user accounts via the Linear user list API. 6. Deploy the bot runtime with the idempotency check (60-second deduplication window) enabled. 7. Set up an error alerting webhook to notify the workspace admin on Linear API failures.

## Test Instructions

1. In the #bugs channel, post 'Test connectivity issue @Linear create task' and verify a new Linear issue is created with a derived title and a confirmation URL is returned in the thread. 2. Post '@Linear create task assign to @[valid Linear user]' and verify the created issue has the correct assignee in Linear. 3. Attempt to invoke the bot from a different Slack workspace and confirm the cross-workspace refusal message appears and no issue is created. 4. Post the same bug description twice within 30 seconds and confirm only one issue is created (idempotency test). 5. Post '@Linear create task' with no description text and confirm no issue is created and the bot prompts for a description. 6. Simulate a Linear API 500 error and confirm the bot surfaces an error message to the user rather than silently failing. 7. Check the Linear issue list to confirm all test issues carry the 'slack-bug-report' label and the correct source metadata.
