# Edge Cases

- Customer received wrong item on a final-sale order — merchant error may override final-sale policy but requires manager confirmation before any remedy is issued.
- Customer has already used or disposed of the wrong item and cannot return it — no-return refund or exchange may require manager approval; do not auto-deny.
- Wrong item received as a gift where the recipient (not the purchaser) contacts support — may require gifter's order details to verify; consider gift-return accommodation logic from src_slack_c0ba1v2k269_1781262772545439 as a reference for locating orders via gifter name/email.
- Wrong item involves a safety concern (allergen, medication, hazardous material) — must be escalated urgently and flagged to product/safety team regardless of refund/exchange outcome.
- Replacement item for exchange is a different price than item ordered — agent must not charge or credit a price difference without manager approval; flag and escalate.
- Customer reports wrong item but item_received field matches item_ordered in system records — possible labeling error or system mismatch; escalate rather than deny.
- Customer contacts support long after delivery (e.g., 60+ days) about a wrong item — standard wrong-item policy timeline may apply; confirm whether a return window cutoff exists before proceeding.

- `Classic wrong color variant — eligible for refund or exchange` -> `eligible`
- `Wrong variant with exchange preference` -> `eligible`
- `Correct item received but poor fit — not a fulfillment error` -> `ineligible`
- `Wrong item shipped but order record unverifiable` -> `needs_escalation`
- `Wrong item shipped — replacement SKU out of stock` -> `needs_escalation`
- `Wrong item shipped on a final-sale order` -> `needs_escalation`
- `Wrong item shipped — customer requests both refund and exchange simultaneously` -> `ineligible`
