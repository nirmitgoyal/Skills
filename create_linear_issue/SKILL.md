# create_linear_issue

When a user posts a bug description in Slack and invokes '@Linear create task' or '@Linear create bug', the bot automatically opens a new Linear issue, derives the issue title from the bug description text, optionally assigns it to a mentioned user, and replies with a hyperlinked issue identifier (e.g., SEM-92). The bot operates deterministically: every valid invocation produces exactly one new issue and one confirmation reply containing the Linear URL. The bot is scoped to its home workspace and will refuse cross-workspace invocations.

## Decision Rules

- IF message contains '@Linear create task' OR '@Linear create bug' AND a non-empty bug description is present, THEN create a Linear issue and reply with the issue URL.
- IF an '@mention' of a user follows the create command (e.g., 'assign to @User'), THEN set that user as the assignee on the created issue.
- IF the @Linear bot instance does not belong to the invoking Slack workspace, THEN refuse with the message 'Sorry, you can’t message this instance of @Linear as it belongs to the [workspace] workspace.' and do NOT create an issue.
- IF the bug description is empty or missing after the create command, THEN do not create an issue and prompt the user to supply a description.
- IF the command is a valid cross-workspace attempt to create an issue that has already been deduplicated (same description in same channel within a short window), THEN escalate for human review rather than creating a duplicate.
- Issue title is derived automatically from the bug description text; the user does not need to supply a separate title.
- The confirmation reply MUST include the full Linear hyperlink and the issue identifier slug (e.g., SEM-NNN).

## Required Fields

- bug_description
- assignee_mention

## Escalation

- If the @Linear bot returns an error other than the cross-workspace refusal (e.g., API timeout, 5xx from Linear), escalate to the workspace administrator.
- If an assignee mention cannot be resolved to a Linear team member, escalate to the requester to confirm the correct Linear username.
- If a cross-workspace invocation is attempted, surface the error message to the user and flag for admin review.
- Duplicate issue suspicion (same description posted multiple times in rapid succession) should be flagged for human triage before a second issue is created.
