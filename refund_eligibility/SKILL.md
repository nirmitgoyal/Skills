# refund_eligibility

Determine whether a customer cancelling an annual or long-term subscription plan is eligible for a pro-rated refund. Eligibility requires cancellation within the first 6 months of the plan. If eligible, calculate refund as (total_months - months_used) / total_months × plan_price, inform the customer that access ends immediately upon cancellation, and that the refund processes within 35 business days. If cancelled after 6 months, the request is ineligible under this policy.

## Decision Rules

- Eligibility gate: cancellation must occur within the first 6 months of the subscription plan (months_used < 6 is required for eligibility).
- Cancellation at exactly 6 months (months_used == 6) is ineligible; the window is strictly the first 6 months.
- Applies only to annual or long-term subscription plans; month-to-month plans are out of scope for this skill.
- Pro-rated refund formula: (total_months - months_used) / total_months × annual_or_period_price.
- Access to the subscription ends immediately upon processing the cancellation, regardless of remaining paid time.
- Refund SLA is 35 business days from the date of cancellation processing.
- If the plan type is ambiguous or the months_used value is missing or unverifiable, escalate before proceeding.
- Do not process refunds for digital goods that have been downloaded and activated under a one-time license model; that is a separate, ineligible policy.
- Always confirm the calculated refund amount and the immediate access termination with the customer before finalising the cancellation.

## Required Fields

- subscription_plan_type
- annual_or_period_price
- months_used
- total_plan_months

## Escalation

- Escalate if months_used cannot be verified in the system and the customer's stated usage falls near the 6-month eligibility boundary.
- Escalate if the subscription_plan_type is unclear or does not clearly qualify as annual or long-term (e.g., custom enterprise agreements).
- Escalate if the customer disputes the plan price or months_used recorded in the system.
- Escalate if the customer requests an exception to continue access after cancellation rather than immediate termination.
- Escalate if the refund has been pending beyond 35 business days and has not been issued.
