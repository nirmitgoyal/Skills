# Deterministic If Days Since Purchase 30 And Condition Unopened Or Condition Unused Then Eligible If Usage Count 0 Then Ineligible Runtime Profile

## Guidance

Always collect purchase_date, days_since_purchase, item_condition, and usage_count before rendering any eligibility decision.

Do not accept customer's self-reported condition at face value if order history, account logs, or prior interactions contradict the claim.

When issuing a courtesy refund for a trial billing edge case, explicitly log it as a one-time exception and verify no prior courtesy refund exists on the account.

Never offer a refund workaround for final-sale items; redirect customer to sizing or product guidance only.

For subscription renewal cases, present the two-option structure (50% autonomous vs. full refund via manager) only when zero-usage evidence is confirmed in account logs.

Confirm refund timeline with customer: standard refunds appear in 3–5 business days; manager-approved refunds may take up to 24 hours for approval before processing.

Do not make eligibility determinations based on subjective dissatisfaction alone (taste, preference, fit) when usage has occurred.

## Install Instructions

Deploy under the refund_eligibility skill. Attach to any conversation flow triggered by return or refund intent keywords. Requires read access to: order management system (purchase_date, promotional_flag, order_id), account usage logs (login_history, usage_count), and customer history (prior courtesy refund flags). Manager escalation routing must be configured with a ~24-hour SLA queue. Ensure final-sale promotional flags are populated at order ingestion time to support real-time lookup.

## Test Instructions

Before go-live, run all seven deterministic tests in test harness mode with mocked order and account data matching each test scenario. Verify: (1) test_001 returns eligible with full-refund confirmation message, (2) test_002 returns ineligible with usage-based denial message and no refund offer, (3) test_003 returns ineligible with final-sale policy citation, (4) test_004 triggers escalation flow with two-option prompt and manager routing, (5) test_005 triggers escalation without denial, (6) test_006 returns eligible with courtesy-refund message and exception logging, (7) test_007 returns ineligible with dual-rule failure noted. Confirm no test produces a refund offer when ineligible, and no test produces a hard denial when escalation is required.
