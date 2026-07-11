# Edge Cases

- Customer requests more than 10% discount — this policy only authorizes exactly 10%; any request above that must be escalated.
- Renewal is flagged as healthy but the customer unexpectedly cites budget concerns mid-cycle — requires documentation of budget as primary blocker before the discount can be considered.
- Customer fits profile and has active opportunity but blocker is documented as 'competitor pricing' rather than 'budget' — this does not satisfy criterion (c); standard pricing applies unless re-documented.
- Channel partner or reseller requests discount on behalf of end customer — this policy does not explicitly cover indirect deals; escalate to deal desk.
- Customer previously received a discount and is requesting it again at renewal — each request must independently satisfy all three criteria; prior discount does not create entitlement.
- Multiple blockers listed in CRM (e.g., budget AND feature gap) — budget must be the PRIMARY blocker, not one of several; if unclear, escalate for clarification.
- Enterprise customer outside SMB segment cites budget constraints — does not fit target profile as defined; reject or escalate depending on deal size and strategic importance.

- `All three criteria met — SMB renewal at risk` -> `eligible`
- `All three criteria met — high-intent new opportunity` -> `eligible`
- `Healthy renewal with no budget blocker` -> `ineligible`
- `Low-fit lead citing budget concerns` -> `ineligible`
- `Blanket discount request for all prospects` -> `ineligible`
- `Budget verbally cited but not documented in CRM` -> `needs_escalation`
- `Customer profile fit is ambiguous` -> `needs_escalation`
- `No active opportunity or renewal in CRM` -> `ineligible`
