# Edge Cases

- Customer fits profile and has a budget blocker documented, but the opportunity was closed-lost last quarter and has not been reopened — treat as no active opportunity; deny.
- Customer requests a 15% discount citing the same budget blocker — policy caps at 10%; deny the excess and escalate if negotiation continues.
- Two separate reps submit discount requests for the same account simultaneously — escalate to prevent duplicate or stacked discounts.
- A healthy renewal account later reports a mid-cycle budget reduction — re-evaluate as a potential renewal-risk account; require updated profile classification before approving.
- Customer fits profile and has an active opportunity but the budget blocker is documented as secondary (primary blocker is a feature gap) — third criterion not met; deny.
- Prospect is an enterprise account, not an SMB — evaluate whether it still fits the defined target profile before applying the rule; escalate if classification is unclear.

- `All three criteria met — qualified SMB with active opportunity and documented budget blocker` -> `eligible`
- `Renewal-risk account with documented budget blocker and active renewal` -> `eligible`
- `Low-fit lead citing budget concerns with active opportunity` -> `ineligible`
- `Healthy renewal account — no budget blocker documented` -> `ineligible`
- `Qualified prospect with budget blocker but no active opportunity or renewal on record` -> `ineligible`
- `Ambiguous profile classification — rep unsure if customer fits target segment` -> `needs_escalation`
- `Verbal budget blocker claim only — no written documentation provided` -> `needs_escalation`
