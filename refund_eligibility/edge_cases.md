# Edge Cases

- Customer reports allergic reaction but item was a final-sale purchase — policy conflict requires human escalation, not auto-approval or auto-denial.
- Customer provides gifter name but the name returns multiple orders — agent must request additional detail (e.g., approximate purchase date or item name) before issuing store credit.
- Customer describes a severe medical reaction (anaphylaxis, hospitalization) — standard refund approval should still proceed, but a safety incident report must be opened in parallel.
- Gifter is willing to process the return themselves — agent should offer both paths (gifter-initiated return or health/safety exception) and let the customer choose.
- Customer cannot identify the specific allergen but describes a clear reaction — still eligible; capture symptoms and flag to product team even without a named ingredient.
- Item is a perishable or consumable that has been fully used — health/safety exception still applies; do not apply the 'used item' ineligibility rule from standard policy when a health concern is documented.
- Customer is also the original purchaser AND experienced an allergic reaction — no alternative verification needed; process as a standard health/safety return without invoking the gift-receipt pathway.

- `Gift recipient with allergic reaction and gift receipt provided` -> `eligible`
- `Gift recipient with allergic reaction and gifter email provided` -> `eligible`
- `Non-original purchaser with no health concern — preference return` -> `ineligible`
- `Gift recipient with allergic reaction but zero alternative verification available` -> `needs_escalation`
- `Allergic reaction on final-sale item with gift receipt provided` -> `needs_escalation`
- `Original purchaser outside 30-day window with no health concern` -> `ineligible`
- `Gift recipient with ingredient sensitivity (non-allergic) and gifter name provided` -> `eligible`
