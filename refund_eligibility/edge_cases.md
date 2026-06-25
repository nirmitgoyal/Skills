# Edge Cases

- Item purchased as a gift: purchase_date may differ from recipient's receipt date; clarify which date governs the 30-day window before ruling.
- Subscription renewals with partial usage (e.g., logged in once in 11 months): agent should not auto-approve full refund; escalate with usage evidence for manager discretion.
- Customer claims item is unused but order history or packaging indicates otherwise: do not make autonomous eligibility determination; escalate for manual review.
- Bundle purchases where one item is used and another is unopened: apply used-item rule to the bundle as a whole unless items can be individually returned and priced.
- Item returned without original packaging but genuinely unused: condition classification is ambiguous; escalate rather than auto-approve or auto-deny.
- Repeat courtesy refund requests: one-time courtesy exception must not be granted again to the same customer for a similar trial-billing scenario; check account history before issuing.
- Final-sale item with a defect (not merely preference-based): defect claims may override final-sale terms under consumer protection standards; escalate to manager for legal review.

- `Unopened item within 30-day window` -> `eligible`
- `Used item within 30-day window` -> `ineligible`
- `Final-sale promotional item, unused, within 30 days` -> `ineligible`
- `Subscription renewal with zero account usage, charged 2 days ago` -> `needs_escalation`
- `Unused item outside 30-day window` -> `needs_escalation`
- `Trial billing courtesy refund within 1 day of trial end` -> `eligible`
- `Used item outside 30-day window` -> `ineligible`
