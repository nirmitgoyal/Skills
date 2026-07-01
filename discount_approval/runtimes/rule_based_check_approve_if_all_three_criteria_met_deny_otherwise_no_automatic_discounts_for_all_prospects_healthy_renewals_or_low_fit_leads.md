# Rule Based Check Approve If All Three Criteria Met Deny Otherwise No Automatic Discounts For All Prospects Healthy Renewals Or Low Fit Leads Runtime Profile

## Guidance

Step 1: Confirm customer_profile_classification. If not confirmed as fitting the target segment, output INELIGIBLE immediately without checking further criteria.

Step 2: Confirm active_opportunity_or_renewal_status. If no active opportunity or renewal is on record, output INELIGIBLE without checking the third criterion.

Step 3: Confirm primary_blocker_documentation. If price or budget is not the documented primary blocker, output INELIGIBLE.

Step 4: If all three criteria are confirmed, output ELIGIBLE for a 10% discount.

Step 5: If any field is missing, ambiguous, or unverifiable, output NEEDS_ESCALATION with the specific unresolved field noted.

Never approve a discount automatically for all prospects or all renewals; each request requires individual three-criterion evaluation.

The maximum authorized discount under this policy is 10%; any request exceeding this must be escalated.

Do not infer or assume any criterion is met from partial information; require explicit evidence for each.

## Install Instructions

Deploy this skill as a rule-based evaluation node triggered when a discount request or price-match inquiry is submitted. Attach required input fields (customer_profile_classification, active_opportunity_or_renewal_status, primary_blocker_documentation) to the intake form or CRM workflow. The skill must receive all three fields as structured inputs before evaluation begins. Connect ELIGIBLE output to discount approval workflow, INELIGIBLE output to standard pricing confirmation message, and NEEDS_ESCALATION output to a human review queue. Do not enable auto-approval modes. Ensure audit logging captures the values of all three criteria for each decision.

## Test Instructions

To verify correct behavior after deployment: (1) Submit test_001 inputs and confirm ELIGIBLE response with 10% discount approval. (2) Submit test_003 inputs and confirm INELIGIBLE response with standard pricing message. (3) Submit test_006 inputs and confirm NEEDS_ESCALATION response with 'customer_profile_classification unverified' noted. (4) Submit a request with all fields empty and confirm the system requests required inputs rather than defaulting to any outcome. (5) Submit a request with a 15% discount ask matching otherwise eligible criteria and confirm escalation is triggered. Review audit logs after each test to confirm all three criterion values are recorded.
