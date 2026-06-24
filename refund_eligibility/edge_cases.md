# Edge Cases

- Customer paid for expedited shipping and the delay was borderline (e.g., 1 day late on a 2-day promise): apply materiality judgment; minor delays alone without stated purpose impact do not automatically qualify for a full item refund.
- Item was time-sensitive but the delay was caused by a carrier-side force majeure event (e.g., severe weather, natural disaster): eligibility may still apply for the shipping fee refund, but the full item refund with keep-the-item policy should be reviewed against internal exception guidelines.
- Customer states a time-sensitive purpose after the fact that cannot be verified: agent should use reasonable judgment and may apply the benefit of the doubt for low-value orders, but escalate for high-value refunds.
- Order involved a promotional or discounted shipping rate rather than a full paid expedited tier: confirm whether the expedited SLA guarantee applies to discounted shipping tiers before approving.
- Refund was already partially issued (e.g., shipping fee only) and customer is now requesting the full item refund: verify prior refund records to avoid duplication and apply remaining eligible refund amount.
- Customer paid expedited shipping but the item was a digital or virtual good: shipping SLA refund logic does not apply; route to the appropriate digital fulfillment skill.
- Late delivery claim is submitted months after the delivery date: apply any applicable claim window policy; very stale claims may require escalation rather than automatic approval.

- `2-day shipping arrived 8 days late, item useless for passed event` -> `eligible`
- `Expedited shipping arrived 1 day late, customer states no time-sensitive purpose` -> `ineligible`
- `Refund previously issued for late delivery but not yet visible on credit card` -> `needs_escalation`
- `2-day shipping arrived 5 days late, customer states item was time-sensitive for a medical appointment` -> `eligible`
- `Late delivery on a Black Friday final sale order` -> `ineligible`
- `Customer claims late delivery but paid_shipping_tier was standard free shipping` -> `ineligible`
- `Expedited shipping late delivery with unverifiable actual delivery date` -> `needs_escalation`
