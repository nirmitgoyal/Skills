# Trust Packet Review

## Summary

Draft review packet for `discount_approval`.

## Structure Reference

Use `marketing_10pct_discount_policy` as review-only folder-structure guidance.

## Source Inventory

Approved source bundle hash: `sha256:61bd40af1a09a31136348d3ffedece2db8a2d23ebb1ece1425e2e89e5ec1d9ba`

## Policy Claims

- claim_1_test_001: Eligible when customer_profile_segment='qualified_smb_prospect', opportunity_or_renewal_status='active', budget_constraint_documented=true. All three criteria met; 10% discount should be approved.
- claim_2_test_002: Eligible when customer_profile_segment='renewal_risk_account', opportunity_or_renewal_status='active_renewal', budget_constraint_documented=true. All three criteria met; 10% discount should be approved.
- claim_3_test_003: Ineligible when customer_profile_segment='low_fit_lead', opportunity_or_renewal_status='active', budget_constraint_documented=true. Fails criterion 1; discount must be denied per explicit policy exclusion of low-fit leads.
- claim_4_test_004: Ineligible when customer_profile_segment='qualified_smb_prospect', opportunity_or_renewal_status='healthy_renewal', budget_constraint_documented=false. Fails criteria 2 and 3; discount denied to avoid broadly discounting healthy demand.
- claim_5_test_005: Ineligible when customer_profile_segment='qualified_smb_prospect', opportunity_or_renewal_status='active', budget_constraint_documented=false. Fails criterion 3; verbal mention of budget concern without documentation is insufficient for approval.
- claim_6_test_006: Escalate when customer_profile_segment='unknown', opportunity_or_renewal_status='active', budget_constraint_documented=true. Criterion 1 cannot be deterministically evaluated; escalate to human manager for segment classification before proceeding.
- claim_7_test_007: Escalate when customer_profile_segment='qualified_smb_prospect', opportunity_or_renewal_status='active', budget_constraint_documented=true, requested_discount=20%. Fit criteria met but requested amount exceeds the 10% authorized ceiling; escalate to manager for non-standard discount approval.
- claim_8_test_008: Ineligible when customer_profile_segment='qualified_smb_prospect', opportunity_or_renewal_status='none', budget_constraint_documented=true. Fails criterion 2; no active opportunity or renewal in progress means discount cannot be applied.

## Required Fields

- customer_profile_segment
- opportunity_or_renewal_status
- budget_constraint_documented

## Edge Cases

- Budget documented as a secondary blocker rather than the primary blocker — treat as criteria 3 NOT met; deny discount.
- Customer is both a renewal-risk account and has a new upsell opportunity active simultaneously — evaluate each opportunity line independently against all three criteria.
- Budget constraint documented only as a verbal note in CRM without a formal written record — treat as undocumented; escalate for verification.
- Prospect upgrades from low-fit to qualified mid-conversation — require re-evaluation of criteria 1 with updated classification before approving.
- Healthy renewal account that suddenly reports a budget constraint during the renewal cycle — opportunity_or_renewal_status must be reclassified to 'renewal_risk' before criteria can be re-evaluated; escalate for reclassification.
- Customer requests discount stacking on top of an existing promotional rate — this skill only governs the 10% discount layer; escalate if combined discount logic is required.
- criteria fields are present but contain null or empty string values — treat as missing and deny or escalate accordingly.
- test_001: Qualified SMB prospect with active opportunity and documented budget blocker -> pass
- test_002: Renewal-risk account with active renewal and documented budget blocker -> pass
- test_003: Low-fit lead with active opportunity and documented budget blocker -> pass
- test_004: Healthy renewal with no documented budget constraint -> pass
- test_005: Qualified SMB prospect with active opportunity but budget not documented -> pass
- test_006: Unclassified customer segment with active opportunity and documented budget blocker -> pass
- test_007: Qualified SMB prospect requesting 20% discount with active opportunity and documented budget blocker -> pass
- test_008: Qualified SMB prospect with no active opportunity and documented budget blocker -> pass

## Test Results

Generated deterministic pilot tests are included under `tests/`.

## Deterministic Rule Based Check No External Api Calls Required Install/Test Instructions

Runtime profile: `runtimes/deterministic_rule_based_check_no_external_api_calls_required.md`

Owner: `[redacted-email]`

Install Instructions

Deploy as a deterministic rule-based skill with no external API dependencies. Ingest the three required fields (customer_profile_segment, opportunity_or_renewal_status, budget_constraint_documented) from the CRM or deal management system via structured input. Validate that all three fields are present and non-null before executing the decision logic. Wire escalation outputs to the human manager review queue. Ensure the skill returns one of three outcomes: eligible (approve 10% discount), ineligible (deny, log failing criterion), or needs_escalation (route to manager with reason code). No machine learning inference or probabilistic scoring should be used; logic must be fully deterministic and auditable.

Test Instructions

Before production deployment, execute all eight deterministic tests defined in this spec using synthetic fixture data. Confirm that test_001 and test_002 return eligible with discount_amount=10. Confirm that test_003, test_004, test_005, and test_008 return ineligible with the correct failing criterion logged. Confirm that test_006 and test_007 return needs_escalation with a descriptive reason code. Additionally, run a null-field test where all three required fields are missing and verify the skill returns needs_escalation rather than throwing an unhandled error. Regression-test after any change to decision logic or field mappings.

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
