# Trust Packet Review

## Summary

Draft review packet for `refund_eligibility`.

## Source Inventory

Approved source bundle hash: `sha256:750de57f788932a82623c3cbc9d10282ce98fb07e6524aea6a24e5063b0d4edb`

## Policy Claims

- claim_1_test_001: Eligible when Customer purchased an item 14 days ago. Item is unopened and unused. days_since_purchase=14, item_condition='unopened', usage_count=0. Should return full refund eligible per core policy rule.
- claim_2_test_002: Ineligible when Customer purchased a coffee maker 10 days ago and has used it approximately 20 times but dislikes the output. days_since_purchase=10, item_condition='used', usage_count=20. Usage disqualifies refund regardless of recency or subjective dissatisfaction, matching src_slack_c0ba1v2k269_1781262709512969.
- claim_3_test_003: Ineligible when Customer purchased a dress during a Black Friday final-sale event 5 days ago. Item is unworn but promotional terms at checkout marked all items non-refundable. promotional_flag=true, days_since_purchase=5, item_condition='unused'. Final-sale override applies, matching src_slack_c0ba1v2k269_1781262732047749.
- claim_4_test_004: Escalate when Customer was charged $99 for an annual renewal 2 days ago. Account shows zero logins in 11 months. Policy does not guarantee renewal refunds; agent may offer 50% autonomously but full refund requires manager approval (~24hrs). Matches src_slack_c0ba1v2k269_1781262784193319.
- claim_5_test_005: Escalate when Customer purchased an item 45 days ago and claims it is still completely unopened and unused. days_since_purchase=45, item_condition='unopened', usage_count=0. Outside the standard 30-day window; agent cannot auto-approve or auto-deny. Must escalate to manager for discretionary review.
- claim_6_test_006: Eligible when Customer forgot to cancel a 7-day trial and was charged $49 exactly 1 day after trial expiry. Account shows no substantive usage during trial. Agent may issue one-time courtesy full refund and cancel subscription autonomously. Matches src_slack_c0ba1v2k269_1781262670462979.
- claim_7_test_007: Ineligible when Customer purchased a blender 60 days ago and has used it regularly but now wants a refund due to performance issues. days_since_purchase=60, item_condition='used', usage_count=15. Fails both the 30-day rule and the unused-condition rule; categorically ineligible with no escalation path.

## Required Fields

- purchase_date
- days_since_purchase
- item_condition (unopened / unused / used)
- usage_count or usage_evidence
- order_id
- promotional_flag (was item purchased during a final-sale event?)

## Edge Cases

- Item purchased as a gift: purchase_date may differ from recipient's receipt date; clarify which date governs the 30-day window before ruling.
- Subscription renewals with partial usage (e.g., logged in once in 11 months): agent should not auto-approve full refund; escalate with usage evidence for manager discretion.
- Customer claims item is unused but order history or packaging indicates otherwise: do not make autonomous eligibility determination; escalate for manual review.
- Bundle purchases where one item is used and another is unopened: apply used-item rule to the bundle as a whole unless items can be individually returned and priced.
- Item returned without original packaging but genuinely unused: condition classification is ambiguous; escalate rather than auto-approve or auto-deny.
- Repeat courtesy refund requests: one-time courtesy exception must not be granted again to the same customer for a similar trial-billing scenario; check account history before issuing.
- Final-sale item with a defect (not merely preference-based): defect claims may override final-sale terms under consumer protection standards; escalate to manager for legal review.
- test_001: Unopened item within 30-day window -> pass
- test_002: Used item within 30-day window -> pass
- test_003: Final-sale promotional item, unused, within 30 days -> pass
- test_004: Subscription renewal with zero account usage, charged 2 days ago -> pass
- test_005: Unused item outside 30-day window -> pass
- test_006: Trial billing courtesy refund within 1 day of trial end -> pass
- test_007: Used item outside 30-day window -> pass

## Test Results

Generated deterministic pilot tests are included under `tests/`.

## Deterministic If Days Since Purchase 30 And Condition Unopened Or Condition Unused Then Eligible If Usage Count 0 Then Ineligible Install/Test Instructions

Runtime profile: `runtimes/deterministic_if_days_since_purchase_30_and_condition_unopened_or_condition_unused_then_eligible_if_usage_count_0_then_ineligible.md`

Owner: `[redacted-email]`

Install Instructions

Deploy under the refund_eligibility skill. Attach to any conversation flow triggered by return or refund intent keywords. Requires read access to: order management system (purchase_date, promotional_flag, order_id), account usage logs (login_history, usage_count), and customer history (prior courtesy refund flags). Manager escalation routing must be configured with a ~24-hour SLA queue. Ensure final-sale promotional flags are populated at order ingestion time to support real-time lookup.

Test Instructions

Before go-live, run all seven deterministic tests in test harness mode with mocked order and account data matching each test scenario. Verify: (1) test_001 returns eligible with full-refund confirmation message, (2) test_002 returns ineligible with usage-based denial message and no refund offer, (3) test_003 returns ineligible with final-sale policy citation, (4) test_004 triggers escalation flow with two-option prompt and manager routing, (5) test_005 triggers escalation without denial, (6) test_006 returns eligible with courtesy-refund message and exception logging, (7) test_007 returns ineligible with dual-rule failure noted. Confirm no test produces a refund offer when ineligible, and no test produces a hard denial when escalation is required.

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
