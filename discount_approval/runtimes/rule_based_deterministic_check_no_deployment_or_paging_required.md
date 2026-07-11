# Rule Based Deterministic Check No Deployment Or Paging Required Runtime Profile

## Guidance

Check all three required fields before rendering any decision; a partial match is not sufficient for approval.

If any required field is missing, null, or ambiguous, route to needs_escalation rather than making an approval or rejection guess.

Do not approve discounts based on customer sentiment or urgency alone — all three documented criteria must be present.

Return decision as one of: APPROVED (all three criteria confirmed), REJECTED (one or more criteria not met), or ESCALATE (one or more criteria unconfirmable).

Log the source evidence for each criterion checked so the decision is auditable.

Do not prompt the customer for additional information at runtime; route to a human if inputs are insufficient.

This skill authorizes a maximum of 10% discount only; do not extrapolate to other discount amounts or types.

## Install Instructions

No deployment, infrastructure changes, or on-call paging required. This skill is a rule-based deterministic check. Install by registering the skill slug 'discount_approval' in the skill registry and mapping the three required input fields (customer_profile_fit, active_opportunity_or_renewal_status, primary_blocker_documented_as_budget) to the corresponding CRM or deal record data source. Ensure the skill is triggered on discount request events or renewal-at-risk signals.

## Test Instructions

To validate correct behavior: (1) Submit a record with all three criteria set to confirmed/true and verify the skill returns APPROVED. (2) Submit a record with one criterion missing or false and verify the skill returns REJECTED. (3) Submit a record with one criterion set to ambiguous or null and verify the skill returns ESCALATE. (4) Submit a blanket discount request with no individual record context and verify the skill returns REJECTED. Review audit logs after each test to confirm criterion-level evidence is captured. Run all eight deterministic tests defined in this spec before promoting to production.
