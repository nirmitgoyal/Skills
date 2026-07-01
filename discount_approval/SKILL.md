# discount_approval

Evaluate a 10% discount request by checking three deterministic criteria derived from internal policy discussion: (1) the customer fits the target profile, (2) an active opportunity or renewal is in progress, and (3) price or budget is documented as the primary blocker. Approve only when all three criteria are simultaneously met. Deny when any criterion is missing. Escalate when evidence is ambiguous or conflicting.

## Decision Rules

- APPROVE the 10% discount if and only if ALL three criteria are met: customer fits target profile AND active opportunity or renewal is in progress AND price/budget is documented as the primary blocker.
- DENY the discount if the customer does not fit the target profile, regardless of other criteria.
- DENY the discount if there is no active opportunity or renewal in progress, regardless of other criteria.
- DENY the discount if price/budget is not documented as the primary blocker, regardless of other criteria.
- Do NOT apply an automatic discount to all prospects; targeted application is required.
- Do NOT apply the discount to existing healthy renewals where budget is not a documented blocker.
- Do NOT apply the discount to low-fit leads even if they cite budget concerns.
- Customers outside the qualifying segment must remain on standard pricing.

## Required Fields

- customer_profile_classification: confirmed fit or non-fit against the target segment (e.g., qualified SMB prospect or renewal-risk account)
- active_opportunity_or_renewal_status: active or inactive, with CRM reference or date
- primary_blocker_documentation: written evidence (e.g., call notes, email, CRM field) confirming price or budget is the primary blocker

## Escalation

- Escalate if customer profile classification is ambiguous and cannot be confirmed as fit or non-fit against the target segment.
- Escalate if the opportunity or renewal status is unclear, stale, or disputed in the CRM.
- Escalate if the budget blocker claim is verbal or informal and lacks documented evidence.
- Escalate if a customer requests more than 10% discount, as the policy only authorizes a 10% ceiling.
- Escalate if multiple overlapping discount requests exist for the same account to prevent stacking.
