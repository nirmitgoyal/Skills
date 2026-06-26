# refund_eligibility

Issue a full one-time courtesy refund when a subscription charge occurs within 24 hours after the customer's trial period ends, indicating a missed cancellation deadline. Cancel the subscription immediately and revert the account to the free plan. Refund is strictly one-time; renewals, charges beyond the 24-hour window, or prior courtesy refunds on the same account do not qualify under this policy and require escalation.

## Decision Rules

- Confirm the trial end date from system records before accepting any customer-stated date.
- Calculate the exact elapsed time between trial_end_date and charge_date; the charge must have occurred within 24 hours (≤24 hours) post-trial to be eligible.
- Verify this is the customer's first courtesy refund on the account; deny if a prior courtesy refund has already been issued under this policy.
- The refund must equal the full charge_amount—no partial refunds under this policy.
- Cancel the subscription immediately upon issuing the refund and revert the account to the free plan.
- Inform the customer that the refund will appear in 3–5 business days.
- If the charge is for an annual renewal (not a trial-to-paid conversion), do not apply this policy; treat as an edge case requiring escalation.
- If the charge occurred more than 24 hours after trial end, escalate to a manager rather than issuing an autonomous refund.
- Do not use customer-provided dates as the sole verification source; always cross-reference system records.

## Required Fields

- trial_end_date
- charge_date
- charge_amount
- subscription_plan_name

## Escalation

- Escalate to manager if charge occurred more than 24 hours after trial end date; autonomous refund authority does not extend beyond the 24-hour window.
- Escalate if the customer has already received a prior courtesy refund under this policy on the same account.
- Escalate annual or multi-month renewal charges that are not trial-to-paid conversions; those require separate manager-approved handling (up to full refund with account termination per evidence).
- Escalate if system records cannot confirm trial end date or charge date, preventing reliable window calculation.
- Escalate if the charge amount does not match the stated subscription plan pricing on record.
