# Trust Packet Review

## Summary

Draft review packet for `discount_approval`.

## Source Inventory

Approved source bundle hash: `sha256:eec9827cb271f035310bb849d924f8c75b8bf1b7d7fb0c13678857e7b4a92ef6`

## Policy Claims

- claim_1_test_001: Eligible when Customer is a qualified SMB prospect (fits target profile), has an active opportunity in the CRM, and sales notes document budget as the primary reason for delay. All three criteria are satisfied; approve the 10% discount.
- claim_2_test_002: Eligible when Account is flagged as renewal-risk (fits target profile), renewal is actively in progress, and a documented email from the customer cites price as the primary blocker. All three criteria are met; approve the 10% discount.
- claim_3_test_003: Ineligible when Customer does not fit the target profile (classified as low-fit lead). Although an active opportunity exists and budget is cited as a blocker, the profile criterion fails. Deny the discount and keep on standard pricing.
- claim_4_test_004: Ineligible when Customer fits the target profile and has an active renewal, but the account is classified as a healthy renewal with no documented price or budget objection. The third criterion is not met. Deny the discount per policy against discounting healthy demand.
- claim_5_test_005: Ineligible when Customer fits the target profile and has documented budget concerns, but there is no active opportunity or renewal found in the CRM. The second criterion fails. Deny the discount; no blanket discounts for all prospects.
- claim_6_test_006: Escalate when The submitting rep cannot confirm whether the customer fits the target profile. Active opportunity exists and budget is documented as a blocker, but profile fit is unverified. Escalate for human review before any discount is issued.
- claim_7_test_007: Escalate when Customer fits the target profile and has an active opportunity, but the only evidence of a budget blocker is a verbal statement with no written record in CRM, email, or call notes. Escalate to confirm documentation before approving.

## Required Fields

- customer_profile_classification: confirmed fit or non-fit against the target segment (e.g., qualified SMB prospect or renewal-risk account)
- active_opportunity_or_renewal_status: active or inactive, with CRM reference or date
- primary_blocker_documentation: written evidence (e.g., call notes, email, CRM field) confirming price or budget is the primary blocker

## Edge Cases

- Customer fits profile and has a budget blocker documented, but the opportunity was closed-lost last quarter and has not been reopened — treat as no active opportunity; deny.
- Customer requests a 15% discount citing the same budget blocker — policy caps at 10%; deny the excess and escalate if negotiation continues.
- Two separate reps submit discount requests for the same account simultaneously — escalate to prevent duplicate or stacked discounts.
- A healthy renewal account later reports a mid-cycle budget reduction — re-evaluate as a potential renewal-risk account; require updated profile classification before approving.
- Customer fits profile and has an active opportunity but the budget blocker is documented as secondary (primary blocker is a feature gap) — third criterion not met; deny.
- Prospect is an enterprise account, not an SMB — evaluate whether it still fits the defined target profile before applying the rule; escalate if classification is unclear.
- test_001: All three criteria met — qualified SMB with active opportunity and documented budget blocker -> pass
- test_002: Renewal-risk account with documented budget blocker and active renewal -> pass
- test_003: Low-fit lead citing budget concerns with active opportunity -> pass
- test_004: Healthy renewal account — no budget blocker documented -> pass
- test_005: Qualified prospect with budget blocker but no active opportunity or renewal on record -> pass
- test_006: Ambiguous profile classification — rep unsure if customer fits target segment -> pass
- test_007: Verbal budget blocker claim only — no written documentation provided -> pass

## Test Results

Generated deterministic pilot tests are included under `tests/`.

## Rule Based Check Approve If All Three Criteria Met Deny Otherwise No Automatic Discounts For All Prospects Healthy Renewals Or Low Fit Leads Install/Test Instructions

Runtime profile: `runtimes/rule_based_check_approve_if_all_three_criteria_met_deny_otherwise_no_automatic_discounts_for_all_prospects_healthy_renewals_or_low_fit_leads.md`

Owner: `[redacted-email]`

Install Instructions

Deploy this skill as a rule-based evaluation node triggered when a discount request or price-match inquiry is submitted. Attach required input fields (customer_profile_classification, active_opportunity_or_renewal_status, primary_blocker_documentation) to the intake form or CRM workflow. The skill must receive all three fields as structured inputs before evaluation begins. Connect ELIGIBLE output to discount approval workflow, INELIGIBLE output to standard pricing confirmation message, and NEEDS_ESCALATION output to a human review queue. Do not enable auto-approval modes. Ensure audit logging captures the values of all three criteria for each decision.

Test Instructions

To verify correct behavior after deployment: (1) Submit test_001 inputs and confirm ELIGIBLE response with 10% discount approval. (2) Submit test_003 inputs and confirm INELIGIBLE response with standard pricing message. (3) Submit test_006 inputs and confirm NEEDS_ESCALATION response with 'customer_profile_classification unverified' noted. (4) Submit a request with all fields empty and confirm the system requests required inputs rather than defaulting to any outcome. (5) Submit a request with a 15% discount ask matching otherwise eligible criteria and confirm escalation is triggered. Review audit logs after each test to confirm all three criterion values are recorded.

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
