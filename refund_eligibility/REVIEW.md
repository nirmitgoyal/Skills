# Trust Packet Review

## Summary

Draft review packet for `refund_eligibility`.

## Source Inventory

Approved source bundle hash: `sha256:182250d5155b8e7b497fc79d839b9727f987d4d6be5ddc825c2fa870de483356`

## Policy Claims

- claim_1_dt_001: Eligible when Customer reports item arrived damaged (Order #ORD-28471), purchased 7 days ago, item is completely unused. All eligibility criteria met: within 30-day window, damage-on-arrival, unused. Grant full refund with no return required. Refund credited in 3–5 business days. Source: src_slack_c0ba1v2k269_1781262638614199.
- claim_2_dt_002: Eligible when Customer reports charger (Order #ORD-44209) stopped working after 5 days of normal use, purchased 3 weeks ago. Failure after extremely short normal use qualifies as manufacturing defect; order is within 30-day window. Grant full refund; optionally offer prepaid return label. Source: src_slack_c0ba1v2k269_1781262660706279.
- claim_3_dt_003: Ineligible when Customer cannot supply an order number or receipt. Without verifiable proof of purchase the transaction cannot be located and no refund can be processed. Request customer check email for order confirmation or bank/card statement before proceeding. Source: src_slack_c0ba1v2k269_1781262721847029.
- claim_4_dt_004: Ineligible when Customer purchased item during a Black Friday final-sale event (Order #ORD-67890) and wants to return due to fit. Final-sale promotional terms disclosed at checkout make the item non-refundable and non-returnable; no exception applies. Deny refund and offer sizing guidance for future purchases. Source: src_slack_c0ba1v2k269_1781262732047749.
- claim_5_dt_005: Ineligible when Customer downloaded and activated a software license (Order #ORD-78234) and now wants a refund due to change of mind. Activated digital goods are consumed products; digital goods policy prohibits refund post-activation. Deny refund, pivot to technical support offer if a functional issue exists. Source: src_slack_c0ba1v2k269_1781262743711859.
- claim_6_dt_006: Escalate when Customer claims item is defective but provides a vague failure description (e.g., 'it just stopped working') after several weeks of use, making it unclear whether the cause is a manufacturing defect or normal wear and tear. Agent cannot independently classify failure_type. Escalate to human agent for product-specific defect assessment before approving or denying refund.
- claim_7_dt_007: Escalate when Customer has a valid order_id, is within the 30-day window, and reports a defect, but the promotional terms attached to the order cannot be confirmed in the system (agent cannot verify whether it was a final-sale event). Escalate to human agent to confirm promotional classification before processing or denying refund.

## Required Fields

- order_id (or equivalent proof of purchase such as receipt or bank statement reference)
- days_since_purchase (derived from order timestamp vs. current date)
- item_condition (unused/unopened vs. in-use at time of damage/defect discovery)
- failure_type (arrived_damaged | manufacturing_defect | early_failure_normal_use | change_of_mind | other)
- usage_duration (how long item was in use before failure, if applicable)

## Edge Cases

- Item was purchased as a gift and recipient reports damage — original purchaser's order_id is required; if unavailable, request email confirmation or bank statement reference before escalating.
- Customer reports damage discovered after limited use (e.g., 2 days) but item_condition is listed as 'opened' — agent must assess whether 'opened' constitutes use that voids no-return-required status or merely unboxing.
- Customer is within the 30-day window but item is in a category (e.g., appliance, large electronics) that may have a separate manufacturer warranty process — agent should check category-specific policy before applying the standard 30-day defect rule.
- Customer provides only a bank/card statement reference with no order number — attempt system lookup by name + transaction amount + date before denying; escalate if lookup is inconclusive.
- Item arrived with minor cosmetic damage only (e.g., dented packaging, no functional damage) — clarify whether the item itself is functionally impaired; cosmetic-only damage with fully functional item may not qualify for full refund under the defect policy.
- Customer reports defect just outside the 30-day window (e.g., day 31–35) — categorically outside the standard window; do not approve; advise customer to contact manufacturer warranty support.
- Customer purchased an annual subscription plan and seeks pro-rated refund after partial use — this falls under subscription cancellation policy, not the damaged/defective item refund policy; route to appropriate skill (annual plan cancellation).
- dt_001: Damaged on arrival, unused, within 30 days -> pass
- dt_002: Manufacturing defect after 5 days of normal use, within 30 days -> pass
- dt_003: No proof of purchase provided -> pass
- dt_004: Final-sale promotional item, change of mind -> pass
- dt_005: Activated digital good, no defect reported -> pass
- dt_006: Defect claim with ambiguous failure description and unclear usage duration -> pass
- dt_007: Within 30 days, defect claim, final-sale status unverifiable -> pass

## Test Results

Generated deterministic pilot tests are included under `tests/`.

## Check Order Timestamp Against 30 Day Window Assess Defect Vs Normal Wear Install/Test Instructions

Runtime profile: `runtimes/check_order_timestamp_against_30_day_window_assess_defect_vs_normal_wear.md`

Owner: `[redacted-email]`

Install Instructions

Deploy as a sub-skill under the refund_eligibility skill group. Bind the order lookup tool to retrieve: order_id, purchase_timestamp, item_category, promotional_flags (final_sale, black_friday, etc.), item_type (physical/digital), and order_amount. Configure days_since_purchase to be computed automatically from purchase_timestamp vs. runtime date. Set a high-value refund escalation threshold (e.g., $500) in the skill config. Ensure the skill can call the refund initiation API and the prepaid-label generation API. Link the skill to the subscription cancellation skill so that pro-rated subscription refund requests are routed correctly. Load the digital goods policy and final-sale policy as grounding documents.

Test Instructions

1. Submit a test case with a valid order_id, days_since_purchase=7, item_condition=unused, failure_type=arrived_damaged — expect ELIGIBLE response with no-return-required language and 3–5 business day refund timeline. 2. Submit a test case with a valid order_id, days_since_purchase=21, failure_type=early_failure_normal_use, usage_duration=5_days — expect ELIGIBLE response with optional prepaid label offer. 3. Submit a test case with no order_id and no receipt — expect INELIGIBLE response requesting proof of purchase. 4. Submit a test case with a final_sale flag on the order — expect INELIGIBLE response citing promotional terms. 5. Submit a test case with item_type=digital and activation_status=activated — expect INELIGIBLE response with technical support pivot offer. 6. Submit a test case with days_since_purchase=25 and failure_type=ambiguous (description: 'just stopped working' after 20 days of use) — expect NEEDS_ESCALATION response routing to human agent. 7. Submit a test case with days_since_purchase=32 — expect INELIGIBLE response citing 30-day window expiration.

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
