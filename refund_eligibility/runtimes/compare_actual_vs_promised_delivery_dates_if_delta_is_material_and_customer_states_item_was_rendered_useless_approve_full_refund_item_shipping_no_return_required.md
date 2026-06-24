# Compare Actual Vs Promised Delivery Dates If Delta Is Material And Customer States Item Was Rendered Useless Approve Full Refund Item Shipping No Return Required Runtime Profile

## Guidance

Pull order_id from the customer and verify paid_shipping_tier, promised_delivery_date, and actual_delivery_date from order records before making any eligibility determination.

Calculate the delta between promised_delivery_date and actual_delivery_date; a delta of 2 or more days on a 2-day shipping promise is considered material.

Explicitly ask the customer for their customer_stated_purpose if not already provided, as it is required to determine whether the item was rendered useless.

If the item was rendered useless for its stated purpose due to the late delivery, approve a full refund (item cost + shipping fee) and explicitly inform the customer they may keep the item.

Do not require a return when issuing a full refund under the late delivery + useless item condition.

Communicate the refund amount clearly, specifying both the item cost and shipping fee components in your response.

If the order falls under a final sale promotion, do not apply this skill for the item refund component; shipping fee refund may still be evaluated separately.

If a prior refund was issued and the customer reports non-receipt, escalate to the payments team immediately rather than issuing a duplicate refund.

Always close the interaction by asking if there is anything else you can do to help the customer.

## Install Instructions

Deploy this skill under the refund_eligibility skill slug. Ensure the agent has read access to order management systems to verify: paid_shipping_tier, promised_delivery_date, actual_delivery_date, item cost, and prior refund history. The agent must also have write access to initiate full refunds to the original payment method. Link this skill to the carrier tracking API so delivery dates can be independently verified against customer claims. Configure escalation routing to the payments team for unresolved refund visibility issues and to senior agents for high-value or disputed-evidence cases. Final sale order flags must be readable by the agent to prevent incorrect full item refund approvals on promotional orders.

## Test Instructions

To validate this skill in a staging environment: (1) Submit a test case with order_id=ORD-55120, paid_shipping_tier=2-day, promised_delivery_date=D, actual_delivery_date=D+8, customer_stated_purpose='gift for event that has passed' and confirm the agent returns an eligible decision with full refund of item + shipping and a keep-the-item statement. (2) Submit a test case with standard free shipping selected and confirm the agent returns ineligible. (3) Submit a test case where refund was previously issued 21 days ago and confirm the agent escalates to the payments team without issuing a duplicate refund. (4) Submit a test case with a Black Friday final sale order and confirm the agent blocks the item refund while citing the promotional terms. (5) Submit a test case with a 1-day delay and no stated time-sensitive purpose and confirm the agent does not approve a full item refund. (6) Verify that in all eligible full-refund cases, the response explicitly states the customer may keep the item and no return is required.
