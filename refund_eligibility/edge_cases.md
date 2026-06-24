# Edge Cases

- Item was purchased as a gift and recipient reports damage — original purchaser's order_id is required; if unavailable, request email confirmation or bank statement reference before escalating.
- Customer reports damage discovered after limited use (e.g., 2 days) but item_condition is listed as 'opened' — agent must assess whether 'opened' constitutes use that voids no-return-required status or merely unboxing.
- Customer is within the 30-day window but item is in a category (e.g., appliance, large electronics) that may have a separate manufacturer warranty process — agent should check category-specific policy before applying the standard 30-day defect rule.
- Customer provides only a bank/card statement reference with no order number — attempt system lookup by name + transaction amount + date before denying; escalate if lookup is inconclusive.
- Item arrived with minor cosmetic damage only (e.g., dented packaging, no functional damage) — clarify whether the item itself is functionally impaired; cosmetic-only damage with fully functional item may not qualify for full refund under the defect policy.
- Customer reports defect just outside the 30-day window (e.g., day 31–35) — categorically outside the standard window; do not approve; advise customer to contact manufacturer warranty support.
- Customer purchased an annual subscription plan and seeks pro-rated refund after partial use — this falls under subscription cancellation policy, not the damaged/defective item refund policy; route to appropriate skill (annual plan cancellation).

- `Damaged on arrival, unused, within 30 days` -> `eligible`
- `Manufacturing defect after 5 days of normal use, within 30 days` -> `eligible`
- `No proof of purchase provided` -> `ineligible`
- `Final-sale promotional item, change of mind` -> `ineligible`
- `Activated digital good, no defect reported` -> `ineligible`
- `Defect claim with ambiguous failure description and unclear usage duration` -> `needs_escalation`
- `Within 30 days, defect claim, final-sale status unverifiable` -> `needs_escalation`
