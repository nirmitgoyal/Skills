# discount_approval

Approve a 10% discount only when all three criteria are simultaneously met: (1) the customer fits the target profile (qualified SMB prospect or renewal-risk account with high intent), (2) an active opportunity or renewal is currently in progress, and (3) price or budget is explicitly documented as the primary blocker. Deny the discount for all-prospects blanket requests, healthy renewals without budget friction, and low-fit or unqualified leads.

## Decision Rules

- ELIGIBLE if customer_profile_segment is 'qualified_smb_prospect' OR 'renewal_risk_account' AND opportunity_or_renewal_status is 'active' AND budget_constraint_documented is true.
- INELIGIBLE if customer_profile_segment is 'low_fit_lead' regardless of other criteria.
- INELIGIBLE if opportunity_or_renewal_status is 'healthy_renewal' and budget_constraint_documented is false.
- INELIGIBLE if opportunity_or_renewal_status is 'none' or 'closed_won' or 'closed_lost'.
- INELIGIBLE if budget_constraint_documented is false, even if fit and opportunity criteria are met.
- ELIGIBLE discount amount is fixed at exactly 10%; no other discount amount is authorized under this skill.
- Do not apply this discount as a blanket offer to all prospects; it must be individually qualified per the three criteria.
- If any one of the three required criteria is missing, ambiguous, or undocumented, do not approve the discount.

## Required Fields

- customer_profile_segment
- opportunity_or_renewal_status
- budget_constraint_documented

## Escalation

- Escalate to a human manager if the customer_profile_segment is unclassified or disputed and cannot be resolved from available data.
- Escalate if the requested discount amount exceeds 10%, as this skill only authorizes up to 10%.
- Escalate if budget documentation is anecdotal or verbal-only without a written record, as 'documented' requires a traceable artifact.
- Escalate if the account has multiple overlapping opportunity statuses that make active vs. healthy determination ambiguous.
- Escalate if there is a policy exception request citing special circumstances not covered by the three-criteria rule.
