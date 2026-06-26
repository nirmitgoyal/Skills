# Trust Packet Review

## Summary

Draft review packet for `refund_eligibility`.

## Source Inventory

Approved source bundle hash: `sha256:bc5aafb9daa7d055260b1fd550d4a7471245431e6ef27b95840899e66c3b2fa7`

## Policy Claims

- claim_1_test_001: Eligible when Customer on Pro plan trial forgot to cancel; charge of $49.00 processed 1 day after the 7-day trial ended. System confirms trial_end_date and charge_date delta ≤ 24 hours, no prior courtesy refund on account. Agent issues full $49.00 refund, cancels subscription, reverts to free plan, and states refund appears in 3–5 business days. Directly supported by src_slack_c0ba1v2k269_1781262670462979.
- claim_2_test_002: Ineligible when Customer requests refund but system records show charge_date is 48 hours after trial_end_date. This exceeds the 24-hour post-trial window required for autonomous courtesy refund eligibility. Agent cannot issue refund unilaterally; must escalate to manager.
- claim_3_test_003: Escalate when Customer requests refund on a $99 annual renewal charge 2 days after renewal date; account shows zero logins in 11 months. This is not a trial-to-paid conversion and falls outside the trial courtesy refund policy. Per src_slack_c0ba1v2k269_1781262784193319, escalate for manager decision on partial or full refund options.
- claim_4_test_004: Ineligible when Charge is within 24 hours of trial end and customer qualifies on timing, but system records show a prior courtesy refund was already issued on this account under this same policy. The one-time-only nature of the courtesy refund disqualifies the request. Agent denies autonomous refund and escalates.
- claim_5_test_005: Escalate when Customer claims trial ended yesterday and requests refund for today's charge, but system records show no matching trial_end_date or the subscription record is ambiguous. Agent cannot confirm the 24-hour window without verified system data. Escalate for manual review before any refund action is taken.
- claim_6_test_006: Escalate when Trial ended and charge occurred within the 24-hour window, but the charge_amount provided by the customer ($79) does not match the subscription_plan_name pricing on record ($49). Discrepancy prevents confident full-refund issuance. Escalate to verify correct charge amount before processing.

## Required Fields

- trial_end_date
- charge_date
- charge_amount
- subscription_plan_name

## Edge Cases

- Annual or multi-year renewal charges are not covered by this trial courtesy refund policy even if the customer has been non-active; escalate per src_slack_c0ba1v2k269_1781262784193319.
- Charge that falls exactly at the 24-hour boundary (e.g., charge timestamp equals trial_end_date + 24:00:00) should be treated as eligible, but document precisely for audit trail.
- Customer who cancelled during the trial but was still charged due to a billing system error is a separate billing dispute, not a courtesy refund scenario; escalate to payments team.
- If the customer's account is already on the free plan (subscription already inactive) when they contact support, verify whether the refund was already processed before re-issuing.
- Customers with multiple trial subscriptions across different plans in the same billing cycle may have ambiguous trial_end_date records; escalate to avoid duplicate refunds.
- Delayed return refund issues (as in src_slack_c0ba1v2k269_1781262796239039) are entirely out of scope for this skill and should be routed to the payments team.
- test_001: Charge exactly 1 day (within 24 hours) after trial end — standard eligible case -> pass
- test_002: Charge 48 hours after trial end — outside 24-hour window -> pass
- test_003: Annual renewal charge with zero account usage — not a trial conversion -> pass
- test_004: Customer has already received a prior courtesy refund on same account -> pass
- test_005: Customer-stated trial end date conflicts with system records — unverifiable window -> pass
- test_006: Charge within 24 hours but charge_amount does not match plan pricing on record -> pass

## Test Results

Generated deterministic pilot tests are included under `tests/`.

## Verify Trial End Date In System Confirm Charge Occurred Within 24 Hours Post Trial Install/Test Instructions

Runtime profile: `runtimes/verify_trial_end_date_in_system_confirm_charge_occurred_within_24_hours_post_trial.md`

Owner: `[redacted-email]`

Install Instructions

Register this skill under the 'refund_eligibility' skill slug. Ensure the runtime has read access to subscription billing records including trial_end_date, charge_date, charge_amount, subscription_plan_name, and prior courtesy refund history. Grant write access to initiate refunds, cancel subscriptions, and update account plan status. Configure escalation routing to the billing manager queue for out-of-window or ambiguous cases. Set the one-time courtesy refund flag as a checkable account attribute to prevent duplicate issuance.

Test Instructions

To validate this skill in a staging environment: (1) Seed a test account with trial_end_date = T and charge_date = T+20 hours; invoke skill and assert full refund issued, subscription cancelled, free plan restored. (2) Seed a second account with charge_date = T+30 hours; invoke and assert escalation path triggered, no refund issued. (3) Seed a third account with a prior courtesy refund flag set and charge_date = T+10 hours; invoke and assert ineligible response with escalation. (4) Seed an annual renewal scenario (no trial record); invoke and assert needs_escalation output matching manager-approval flow. (5) Seed an account with missing trial_end_date in system; invoke and assert escalation triggered before any refund action. Confirm all refund amounts in passing tests equal the seeded charge_amount exactly.

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
