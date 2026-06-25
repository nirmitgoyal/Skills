# refund_eligibility

Determine refund eligibility for item returns based on two primary factors: (1) days since purchase must be 30 or fewer, and (2) item must be unused and unopened. Used items are categorically ineligible regardless of days since purchase or reason for return. Final-sale promotional purchases are non-refundable per promotional terms. Edge cases involving clear non-usage history or renewal charges with zero account activity may qualify for partial refunds or escalated full-refund review.

## Decision Rules

- If days_since_purchase <= 30 AND item_condition is 'unopened' OR 'unused', then ELIGIBLE for full refund.
- If usage_count > 0 OR item_condition is 'used', then INELIGIBLE regardless of days since purchase or dissatisfaction reason.
- If the item was purchased under a final-sale or promotional event explicitly marked non-refundable at checkout, then INELIGIBLE regardless of condition or timeframe.
- If days_since_purchase > 30 AND item is unused, eligibility cannot be confirmed by policy; escalate for manager review.
- If a subscription renewal was charged within the last 30 days AND account shows zero usage, escalate: agent may offer 50% refund autonomously or route full-refund request to manager (~24hr approval).
- Do not accept subjective dissatisfaction (e.g., taste, preference, fit) as grounds for overriding a usage-based or final-sale ineligibility ruling.
- One-time courtesy refunds for missed trial cancellations charged within 1 day of trial expiry may be issued autonomously as a goodwill exception; document as courtesy action.

## Required Fields

- purchase_date
- days_since_purchase
- item_condition (unopened / unused / used)
- usage_count or usage_evidence
- order_id
- promotional_flag (was item purchased during a final-sale event?)

## Escalation

- Full refund on subscription renewal with zero-login history requires manager approval; estimated resolution ~24 hours.
- Any return request outside the 30-day window where item is genuinely unused should be escalated rather than auto-denied.
- Courtesy refunds issued for trial billing edge cases must be logged as one-time exceptions to avoid repeat exploitation.
- Final-sale policy exceptions are explicitly not permitted at the agent level; do not offer workarounds.
- If customer provides conflicting usage evidence (claims unused but order history suggests otherwise), escalate for manual review rather than making autonomous eligibility determination.
