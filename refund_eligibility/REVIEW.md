# Trust Packet Review

## Summary

Draft review packet for `refund_eligibility`.

## Source Inventory

Approved source bundle hash: `sha256:25d600baa62af8b122f8ef3d74f287faaa85f4b11df78d14adbd35f49f658f2d`

## Policy Claims

- claim_1_test_001: Eligible when Customer paid for 2-day shipping on Order #ORD-55120. Package arrived 8 days late. Customer states the item was a gift for an event that has already passed, rendering the item useless. Agent should issue a full refund including the shipping fee and inform the customer they may keep the item. No return required. Supported directly by src_slack_c0ba1v2k269_1781262686690199.
- claim_2_test_002: Ineligible when Customer paid for 2-day shipping and package arrived 1 day late. Customer does not state the item was rendered useless and has no time-sensitive purpose. A single-day minor delay without stated impact does not meet the materiality threshold or the uselessness criterion for a full item refund. At most, a partial shipping fee credit may be warranted, but full refund eligibility is not established under this skill's rules.
- claim_3_test_003: Escalate when Customer reports that a refund for a prior late-delivery case was confirmed but has not appeared on their credit card after 21 days. Agent must not issue a duplicate refund. This should be escalated to the payments team to trace the transaction, with a 48-hour resolution target and direct follow-up to the customer. Supported by src_slack_c0ba1v2k269_1781262796239039.
- claim_4_test_004: Eligible when Customer paid for 2-day shipping. Package arrived 5 days late. Customer states the item (e.g., a medical device or test kit) was needed before a specific appointment that has now passed, rendering it useless for its intended purpose. The material delay combined with the customer's stated purpose qualifies for a full refund of item and shipping fee, with no return required. Consistent with the decision rules derived from src_slack_c0ba1v2k269_1781262686690199.
- claim_5_test_005: Ineligible when Customer paid for expedited shipping on a Black Friday final sale order. Even if the package arrived late, the final sale promotional terms disclosed at checkout render the item non-refundable and non-returnable. The shipping fee refund may still be evaluated, but a full item refund is ineligible under the final sale policy. Supported by src_slack_c0ba1v2k269_1781262732047749.
- claim_6_test_006: Ineligible when Customer reports a delayed package but order records show the customer selected standard free shipping, not an expedited paid tier. Because no expedited shipping fee was paid, the core eligibility criterion for this skill is not met. The agent should acknowledge the delay, communicate any applicable standard SLA information, but decline a shipping fee refund under this skill.
- claim_7_test_007: Escalate when Customer paid for 2-day shipping and claims the package arrived significantly late. However, the tracking system shows a delivery date that conflicts with the customer's stated actual delivery date. The agent cannot deterministically confirm the delay without resolving the discrepancy. This case must be escalated to verify delivery records before a refund decision is made.

## Required Fields

- order_id
- paid_shipping_tier
- promised_delivery_date
- actual_delivery_date
- customer_stated_purpose

## Edge Cases

- Customer paid for expedited shipping and the delay was borderline (e.g., 1 day late on a 2-day promise): apply materiality judgment; minor delays alone without stated purpose impact do not automatically qualify for a full item refund.
- Item was time-sensitive but the delay was caused by a carrier-side force majeure event (e.g., severe weather, natural disaster): eligibility may still apply for the shipping fee refund, but the full item refund with keep-the-item policy should be reviewed against internal exception guidelines.
- Customer states a time-sensitive purpose after the fact that cannot be verified: agent should use reasonable judgment and may apply the benefit of the doubt for low-value orders, but escalate for high-value refunds.
- Order involved a promotional or discounted shipping rate rather than a full paid expedited tier: confirm whether the expedited SLA guarantee applies to discounted shipping tiers before approving.
- Refund was already partially issued (e.g., shipping fee only) and customer is now requesting the full item refund: verify prior refund records to avoid duplication and apply remaining eligible refund amount.
- Customer paid expedited shipping but the item was a digital or virtual good: shipping SLA refund logic does not apply; route to the appropriate digital fulfillment skill.
- Late delivery claim is submitted months after the delivery date: apply any applicable claim window policy; very stale claims may require escalation rather than automatic approval.
- test_001: 2-day shipping arrived 8 days late, item useless for passed event -> pass
- test_002: Expedited shipping arrived 1 day late, customer states no time-sensitive purpose -> pass
- test_003: Refund previously issued for late delivery but not yet visible on credit card -> pass
- test_004: 2-day shipping arrived 5 days late, customer states item was time-sensitive for a medical appointment -> pass
- test_005: Late delivery on a Black Friday final sale order -> pass
- test_006: Customer claims late delivery but paid_shipping_tier was standard free shipping -> pass
- test_007: Expedited shipping late delivery with unverifiable actual delivery date -> pass

## Test Results

Generated deterministic pilot tests are included under `tests/`.

## Compare Actual Vs Promised Delivery Dates If Delta Is Material And Customer States Item Was Rendered Useless Approve Full Refund Item Shipping No Return Required Install/Test Instructions

Runtime profile: `runtimes/compare_actual_vs_promised_delivery_dates_if_delta_is_material_and_customer_states_item_was_rendered_useless_approve_full_refund_item_shipping_no_return_required.md`

Owner: `[redacted-email]`

Install Instructions

Deploy this skill under the refund_eligibility skill slug. Ensure the agent has read access to order management systems to verify: paid_shipping_tier, promised_delivery_date, actual_delivery_date, item cost, and prior refund history. The agent must also have write access to initiate full refunds to the original payment method. Link this skill to the carrier tracking API so delivery dates can be independently verified against customer claims. Configure escalation routing to the payments team for unresolved refund visibility issues and to senior agents for high-value or disputed-evidence cases. Final sale order flags must be readable by the agent to prevent incorrect full item refund approvals on promotional orders.

Test Instructions

To validate this skill in a staging environment: (1) Submit a test case with order_id=ORD-55120, paid_shipping_tier=2-day, promised_delivery_date=D, actual_delivery_date=D+8, customer_stated_purpose='gift for event that has passed' and confirm the agent returns an eligible decision with full refund of item + shipping and a keep-the-item statement. (2) Submit a test case with standard free shipping selected and confirm the agent returns ineligible. (3) Submit a test case where refund was previously issued 21 days ago and confirm the agent escalates to the payments team without issuing a duplicate refund. (4) Submit a test case with a Black Friday final sale order and confirm the agent blocks the item refund while citing the promotional terms. (5) Submit a test case with a 1-day delay and no stated time-sensitive purpose and confirm the agent does not approve a full item refund. (6) Verify that in all eligible full-refund cases, the response explicitly states the customer may keep the item and no return is required.

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
