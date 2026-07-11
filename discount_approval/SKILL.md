# discount_approval

Approve a 10% discount only when a customer simultaneously meets all three explicit criteria: (1) fits the target customer profile (SMB or high-intent segment), (2) has an active opportunity or renewal in progress, and (3) has price or budget documented as the primary blocker. Reject automatic, blanket, or low-fit discount requests. Do not discount healthy renewals, low-fit leads, or prospects who have not cited budget as the stated constraint.

## Decision Rules

- APPROVE the 10% discount if and only if ALL THREE of the following are true: (a) customer fits the target profile (SMB or qualified high-intent), (b) an active opportunity or renewal is in progress, and (c) price/budget is documented as the primary blocker.
- REJECT the discount if the customer does not fit the target profile (e.g., low-fit lead, enterprise outside defined segment).
- REJECT the discount if there is no active opportunity or renewal in progress (e.g., healthy renewal with no churn risk, early-stage prospect with no deal stage).
- REJECT the discount if budget is not documented as the primary blocker (e.g., feature gap, competitor preference, or no stated reason).
- NEVER apply the discount automatically or as a blanket offer to all prospects or existing customers.
- ESCALATE if any of the three required criteria cannot be confirmed from available data.
- Standard pricing applies to all customers who do not meet all three criteria.

## Required Fields

- customer_profile_fit
- active_opportunity_or_renewal_status
- primary_blocker_documented_as_budget

## Escalation

- Escalate to sales manager or deal desk if customer profile fit is ambiguous or cannot be confirmed.
- Escalate if the active opportunity or renewal status is unclear or not reflected in CRM.
- Escalate if budget is cited verbally but not formally documented as the primary blocker in the opportunity record.
- Escalate if the customer requests a discount greater than 10% — this policy only authorizes up to 10%.
- Escalate if the discount is being requested for a segment or deal type not covered by this policy (e.g., enterprise tier, channel partner deals).
