# Trust Packet Review

## Summary

Draft review packet for `refund_eligibility`.

## Source Inventory

Approved source bundle hash: `sha256:7fee610f08e303c23307fd60a80d46400c3da05616bde5d9deca3f0eaed8c441`

## Policy Claims

- claim_1_test_001: Eligible when Customer cancels a $120/year annual plan after 3 months. months_used=3, total_months=12. Refund = (12-3)/12 × $120 = $90.00. Access ends immediately; refund in 35 business days. Directly backed by src_slack_c0ba1v2k269_1781262754545559.
- claim_2_test_002: Ineligible when Customer cancels a $240/year annual plan after 7 months. months_used=7 exceeds the 6-month eligibility window, so no pro-rated refund is available under this policy.
- claim_3_test_003: Ineligible when Customer cancels a $120/year plan at exactly 6 months used. Policy requires cancellation within the first 6 months (months_used < 6); at months_used=6 the customer is outside the eligibility window and no refund applies.
- claim_4_test_004: Escalate when Customer claims they have used only 5 months of their 18-month plan ($360), but the system shows no reliable record. Stated usage places them at the eligibility boundary. Escalate for manual verification before calculating or denying a refund.
- claim_5_test_005: Eligible when Customer cancels a $480 24-month plan after 4 months. months_used=4 < 6, so eligible. Refund = (24-4)/24 × $480 = $400.00. Access ends immediately; refund within 35 business days.
- claim_6_test_006: Eligible when Customer cancels a $360/year annual plan after 1 month. months_used=1 < 6. Refund = (12-1)/12 × $360 = $330.00. Access ends immediately; refund within 35 business days.
- claim_7_test_007: Escalate when Customer references a multi-seat enterprise agreement with a non-standard billing structure. Plan type does not clearly qualify as a standard annual or long-term subscription; escalate to determine whether this policy applies before proceeding.

## Required Fields

- subscription_plan_type
- annual_or_period_price
- months_used
- total_plan_months

## Edge Cases

- Customer cancels at exactly month 6 — ineligible; the policy window is strictly fewer than 6 months used.
- Customer has a promotional or discounted price — use actual amount paid, not the standard list price, in the refund calculation.
- Customer requests partial cancellation (e.g., reducing seats) rather than full cancellation — out of scope for this skill; escalate.
- Refund would result in $0.00 due to rounding or a fully used period — confirm with customer before closing the case.
- Customer cancels and then requests to reverse the cancellation — access ends immediately upon processing; reversal is not covered by this skill and requires escalation.
- Plan price was charged in a foreign currency — confirm currency of refund and note potential FX timing differences; escalate if unclear.
- months_used is a fractional value (e.g., cancelled mid-month) — use the policy-defined whole-month rounding convention or escalate if convention is unspecified.
- test_001: Standard annual plan cancelled at 3 months -> pass
- test_002: Annual plan cancelled after 7 months -> pass
- test_003: Annual plan cancelled at exactly 6 months boundary -> pass
- test_004: Months used cannot be verified and customer claims usage near boundary -> pass
- test_005: 24-month plan cancelled at 4 months -> pass
- test_006: Annual plan cancelled after 1 month -> pass
- test_007: Customer provides ambiguous plan type (custom enterprise agreement) -> pass

## Test Results

Generated deterministic pilot tests are included under `tests/`.

## Eligibility Deterministic Calculation Total Months Months Used Total Months Price Refund Sla 35 Business Days Install/Test Instructions

Runtime profile: `runtimes/eligibility_deterministic_calculation_total_months_months_used_total_months_price_refund_sla_35_business_days.md`

Owner: `[redacted-email]`

Install Instructions

Deploy under skill slug 'refund_eligibility'. Attach to cancellation intents for annual and long-term subscription plan types. Ensure the runtime has read access to the customer's subscription record (plan type, start date, price paid, total term months) to auto-populate months_used and plan_price where possible, reducing manual entry errors. Gate this skill so it does not fire for month-to-month plans or one-time digital license purchases.

Test Instructions

Run all seven deterministic tests in the test suite before promoting to production. Verify that: (1) the eligibility gate correctly blocks months_used >= 6 as ineligible; (2) the refund formula produces the correct two-decimal-place value for each eligible test; (3) needs_escalation paths halt calculation and surface an escalation prompt; (4) the 35-business-day SLA and immediate access termination disclosures appear in every eligible response; (5) no refund figure is presented to the customer before explicit confirmation is solicited.

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
