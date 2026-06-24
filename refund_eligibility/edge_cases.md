# Edge Cases

- Customer cancels at exactly month 6 — ineligible; the policy window is strictly fewer than 6 months used.
- Customer has a promotional or discounted price — use actual amount paid, not the standard list price, in the refund calculation.
- Customer requests partial cancellation (e.g., reducing seats) rather than full cancellation — out of scope for this skill; escalate.
- Refund would result in $0.00 due to rounding or a fully used period — confirm with customer before closing the case.
- Customer cancels and then requests to reverse the cancellation — access ends immediately upon processing; reversal is not covered by this skill and requires escalation.
- Plan price was charged in a foreign currency — confirm currency of refund and note potential FX timing differences; escalate if unclear.
- months_used is a fractional value (e.g., cancelled mid-month) — use the policy-defined whole-month rounding convention or escalate if convention is unspecified.

- `Standard annual plan cancelled at 3 months` -> `eligible`
- `Annual plan cancelled after 7 months` -> `ineligible`
- `Annual plan cancelled at exactly 6 months boundary` -> `ineligible`
- `Months used cannot be verified and customer claims usage near boundary` -> `needs_escalation`
- `24-month plan cancelled at 4 months` -> `eligible`
- `Annual plan cancelled after 1 month` -> `eligible`
- `Customer provides ambiguous plan type (custom enterprise agreement)` -> `needs_escalation`
