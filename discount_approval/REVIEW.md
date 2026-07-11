# Trust Packet Review

## Summary

Draft review packet for `discount_approval`.

## Source Inventory

Approved source bundle hash: `sha256:c0cbc9373e67a270b224543cdc33d1020459d10bd58f90e338896ecf8f37a86c`

## Policy Claims

- claim_1_test_001: Eligible when Customer is a qualified SMB (fits target profile), has an active renewal in progress flagged as renewal-risk, and the CRM opportunity record documents budget/price as the primary blocker. All three criteria are satisfied → approve 10% discount.
- claim_2_test_002: Eligible when Customer is a high-intent qualified prospect in the SMB segment, has an active new-business opportunity in progress, and has explicitly cited budget constraints as the reason they cannot proceed. All three criteria are satisfied → approve 10% discount.
- claim_3_test_003: Ineligible when Customer fits target profile and has an active renewal, but the renewal is healthy with no churn risk and budget has not been cited as a blocker. Criterion (c) is not met → reject discount, apply standard pricing.
- claim_4_test_004: Ineligible when Customer cites budget as a blocker and has an active opportunity, but does not fit the target customer profile (low-fit lead). Criterion (a) is not met → reject discount, apply standard pricing.
- claim_5_test_005: Ineligible when Sales team requests automatic 10% discount to be applied to all prospects in a campaign. No individual qualification criteria are evaluated. Policy explicitly prohibits blanket or automatic discounts → reject.
- claim_6_test_006: Escalate when Customer fits target profile, has an active opportunity in progress, and the sales rep verbally reports that budget is the blocker, but the primary blocker field is not formally documented in the CRM opportunity record. Criterion (c) cannot be confirmed → escalate to deal desk for documentation before approval.
- claim_7_test_007: Escalate when Customer has an active renewal at risk and budget is documented as the primary blocker, but account segmentation data is missing or contradictory, making it unclear whether the customer fits the SMB/high-intent target profile. Criterion (a) cannot be confirmed → escalate to sales manager to verify profile fit.
- claim_8_test_008: Ineligible when Customer fits the target profile and has cited budget as a concern, but no active opportunity or renewal record exists in the CRM. Criterion (b) is not met → reject discount, apply standard pricing.

## Required Fields

- customer_profile_fit
- active_opportunity_or_renewal_status
- primary_blocker_documented_as_budget

## Edge Cases

- Customer requests more than 10% discount — this policy only authorizes exactly 10%; any request above that must be escalated.
- Renewal is flagged as healthy but the customer unexpectedly cites budget concerns mid-cycle — requires documentation of budget as primary blocker before the discount can be considered.
- Customer fits profile and has active opportunity but blocker is documented as 'competitor pricing' rather than 'budget' — this does not satisfy criterion (c); standard pricing applies unless re-documented.
- Channel partner or reseller requests discount on behalf of end customer — this policy does not explicitly cover indirect deals; escalate to deal desk.
- Customer previously received a discount and is requesting it again at renewal — each request must independently satisfy all three criteria; prior discount does not create entitlement.
- Multiple blockers listed in CRM (e.g., budget AND feature gap) — budget must be the PRIMARY blocker, not one of several; if unclear, escalate for clarification.
- Enterprise customer outside SMB segment cites budget constraints — does not fit target profile as defined; reject or escalate depending on deal size and strategic importance.
- test_001: All three criteria met — SMB renewal at risk -> pass
- test_002: All three criteria met — high-intent new opportunity -> pass
- test_003: Healthy renewal with no budget blocker -> pass
- test_004: Low-fit lead citing budget concerns -> pass
- test_005: Blanket discount request for all prospects -> pass
- test_006: Budget verbally cited but not documented in CRM -> pass
- test_007: Customer profile fit is ambiguous -> pass
- test_008: No active opportunity or renewal in CRM -> pass

## Test Results

Generated deterministic pilot tests are included under `tests/`.

## Rule Based Deterministic Check No Deployment Or Paging Required Install/Test Instructions

Runtime profile: `runtimes/rule_based_deterministic_check_no_deployment_or_paging_required.md`

Owner: `[redacted-email]`

Install Instructions

No deployment, infrastructure changes, or on-call paging required. This skill is a rule-based deterministic check. Install by registering the skill slug 'discount_approval' in the skill registry and mapping the three required input fields (customer_profile_fit, active_opportunity_or_renewal_status, primary_blocker_documented_as_budget) to the corresponding CRM or deal record data source. Ensure the skill is triggered on discount request events or renewal-at-risk signals.

Test Instructions

To validate correct behavior: (1) Submit a record with all three criteria set to confirmed/true and verify the skill returns APPROVED. (2) Submit a record with one criterion missing or false and verify the skill returns REJECTED. (3) Submit a record with one criterion set to ambiguous or null and verify the skill returns ESCALATE. (4) Submit a blanket discount request with no individual record context and verify the skill returns REJECTED. Review audit logs after each test to confirm criterion-level evidence is captured. Run all eight deterministic tests defined in this spec before promoting to production.

## Runtime Lock

Do not install or activate the skill; runtime use remains locked pending reviewed/import verification.

## Merge Risks

This is a draft and must not be treated as ready until GitHub validation and reviewed/import verification land in later phases.

## Reviewer Checklist

- Confirm approved sources.
- Confirm decision rules, required fields, and deterministic tests.
- Confirm runtime lock and reviewer-safe output.

## Next Reviewer Action

Verify the approved sources, decision rules, required fields, runtime lock, and reviewer-safe output.
