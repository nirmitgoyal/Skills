# Edge Cases

- Customer submits a screenshot but it is cropped or low-resolution — request a clearer image before proceeding; do not deny outright.
- The checkout archive itself is ambiguous (e.g., A/B test variant shown to some customers) — escalate for product team to confirm which variant was served to this customer's session.
- Customer was charged duties by their national customs authority rather than by the merchant — clarify that a refund covers only merchant-controlled duties fees; third-party government fees may not be refundable and require escalation.
- Multiple orders with duties charges from the same customer in a short period — flag for pattern review to trust-and-safety before approving any individual refund.
- Customer already received a partial refund for the same duties charge from a previous interaction — deduct prior refunded amount from the approved refund to avoid double-payment.
- Destination country charges are split between duties and VAT/GST — only the duties portion covered by 'duties included' promise is refundable; tax components are handled separately.

- `Matching screenshot and archive — full refund approved` -> `eligible`
- `No screenshot and no archive record — ineligible` -> `ineligible`
- `Screenshot provided but archive record cannot be located — escalation required` -> `needs_escalation`
- `Chargeback threat with pending duties dispute — immediate escalation` -> `needs_escalation`
- `Screenshot shows generic free shipping, not duties coverage — ineligible` -> `ineligible`
- `Archive confirms duties promise; listing was corrected before order date — ineligible` -> `ineligible`
- `Screenshot matches archive, duties amount over $200 — escalation for manager approval` -> `needs_escalation`
