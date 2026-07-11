# Edge Cases

- Budget documented as a secondary blocker rather than the primary blocker — treat as criteria 3 NOT met; deny discount.
- Customer is both a renewal-risk account and has a new upsell opportunity active simultaneously — evaluate each opportunity line independently against all three criteria.
- Budget constraint documented only as a verbal note in CRM without a formal written record — treat as undocumented; escalate for verification.
- Prospect upgrades from low-fit to qualified mid-conversation — require re-evaluation of criteria 1 with updated classification before approving.
- Healthy renewal account that suddenly reports a budget constraint during the renewal cycle — opportunity_or_renewal_status must be reclassified to 'renewal_risk' before criteria can be re-evaluated; escalate for reclassification.
- Customer requests discount stacking on top of an existing promotional rate — this skill only governs the 10% discount layer; escalate if combined discount logic is required.
- criteria fields are present but contain null or empty string values — treat as missing and deny or escalate accordingly.

- `Qualified SMB prospect with active opportunity and documented budget blocker` -> `eligible`
- `Renewal-risk account with active renewal and documented budget blocker` -> `eligible`
- `Low-fit lead with active opportunity and documented budget blocker` -> `ineligible`
- `Healthy renewal with no documented budget constraint` -> `ineligible`
- `Qualified SMB prospect with active opportunity but budget not documented` -> `ineligible`
- `Unclassified customer segment with active opportunity and documented budget blocker` -> `needs_escalation`
- `Qualified SMB prospect requesting 20% discount with active opportunity and documented budget blocker` -> `needs_escalation`
- `Qualified SMB prospect with no active opportunity and documented budget blocker` -> `ineligible`
