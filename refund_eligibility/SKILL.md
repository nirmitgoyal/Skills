# refund_eligibility

When a customer paid for an expedited shipping tier (e.g., 2-day) and the package arrived materially late, the agent determines full refund eligibility. If the delay was significant and the customer states the item was rendered useless for its intended purpose, a full refund (item + shipping fee) is issued and the customer is allowed to keep the item. No return is required in such cases.

## Decision Rules

- Customer must have paid for an expedited shipping tier (e.g., 2-day shipping) on the order in question.
- The actual delivery date must be materially later than the promised delivery date (e.g., 8 days late on a 2-day promise qualifies as material).
- If the late delivery rendered the item useless for its customer-stated purpose (e.g., a gift for a passed event), issue a full refund covering both the item cost and the shipping fee.
- No return is required when the item is deemed useless due to late delivery; customer is explicitly permitted to keep the item.
- If the delay exists but the customer does not state the item was rendered useless, refund the shipping fee at minimum; evaluate item refund on a case-by-case basis.
- Orders flagged as final sale or under promotional non-refundable terms are not eligible under this skill; those cases follow the final sale policy.
- If the refund has already been issued but not yet reflected on the customer's payment method, escalate to the payments team rather than issuing a duplicate refund.
- If disputed charges (e.g., unexpected customs fees) are involved alongside a late delivery claim, handle each component separately and escalate the disputed charge portion as needed.

## Required Fields

- order_id
- paid_shipping_tier
- promised_delivery_date
- actual_delivery_date
- customer_stated_purpose

## Escalation

- Escalate to the payments team if a refund was previously confirmed but has not appeared on the customer's card after a reasonable processing window (typically flagged around 21 days).
- Escalate to a senior agent or compliance team if the customer claims the website displayed misleading shipping guarantees or promotional terms that conflict with the outcome.
- Escalate if the order cannot be verified in the system or if the paid shipping tier cannot be confirmed from order records.
- Escalate if the calculated refund amount is unusually large or if fraud indicators are present on the account.
- Escalate if the customer disputes the delivery date shown in tracking records and provides conflicting evidence.
