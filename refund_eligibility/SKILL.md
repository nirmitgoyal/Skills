# refund_eligibility

Issue a full refund of charged customs or international duties fees when the customer provides verifiable evidence that the checkout page explicitly stated 'duties included' or equivalent duty-free delivery promise at time of purchase. Screenshot must be cross-checked against the checkout archive. If the archived messaging matches, approve the full refund immediately and raise a listing-correction flag to the product team. If the screenshot is missing, hold the case open and prompt the customer to supply it. If the screenshot cannot be verified against the archive or the claim appears inconsistent, escalate to a senior agent for manual review.

## Decision Rules

- ELIGIBLE: Customer provides a screenshot of checkout messaging explicitly stating 'duties included', 'duty-free delivery', or equivalent language, AND the screenshot matches the archived checkout record for that SKU/region/date.
- ELIGIBLE: Order timestamp and destination country are consistent with a product listing that carried a 'duties included' label in the checkout archive at the time of purchase, even if screenshot quality is low, provided the archive alone confirms the promise.
- INELIGIBLE: No screenshot is provided AND the checkout archive contains no record of any 'duties included' messaging for the relevant SKU, destination country, or order date.
- INELIGIBLE: Screenshot is provided but the messaging shown does not explicitly promise duties coverage (e.g., generic 'free shipping' without duty reference).
- INELIGIBLE: Customer is disputing duties on an order where the product listing was already corrected before the order timestamp, meaning the promise was not active at purchase time.
- NEEDS_ESCALATION: Screenshot is provided but cannot be verified against the archive (archive gap, corrupted record, or timestamp mismatch) — escalate to senior agent within 4 business hours.
- NEEDS_ESCALATION: Customer has already initiated a chargeback or explicitly states they are filing one — escalate immediately to senior payments team.
- NEEDS_ESCALATION: Charged duties amount exceeds $200 or involves a commercial/bulk order — requires manager approval before refund is issued.
- NEEDS_ESCALATION: Discrepancy exists between the customer-submitted screenshot and the archived checkout record (possible manipulation) — escalate to trust-and-safety review.
- Always raise a listing-correction flag to the product team when a refund is approved, regardless of whether the listing has already been corrected.

## Required Fields

- order_id
- charged_amount
- customer_screenshot_of_checkout_messaging
- order_timestamp
- destination_country

## Escalation

- Escalate to senior payments team when the customer mentions chargeback intent; reference source evidence src_slack_c0ba1v2k269_1781262823049209 for handling urgency protocol.
- Escalate to trust-and-safety when a submitted screenshot does not match the checkout archive — potential fraud indicator.
- Escalate to manager for any single refund exceeding $200 in duties charges before approval.
- When escalating, always include: order_id, charged_amount, order_timestamp, destination country, and the screenshot file or link.
- Escalation SLA: senior agent must respond within 4 business hours for archive-gap cases; immediate response required for chargeback-threat cases.
