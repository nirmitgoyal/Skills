# Check Order Timestamp Against 30 Day Window Assess Defect Vs Normal Wear Runtime Profile

## Guidance

Step 1: Verify proof of purchase — confirm order_id exists in the system before any eligibility assessment. If not found, request email confirmation or bank statement reference.

Step 2: Calculate days_since_purchase from order timestamp to today. If > 30 days, deny immediately and inform customer they are outside the refund window.

Step 3: Confirm failure_type by asking the customer to describe what happened. Classify as arrived_damaged, manufacturing_defect, early_failure_normal_use, or other.

Step 4: If failure_type is change_of_mind, wrong_size, or buyer_remorse with no defect, deny refund (not within scope of this skill).

Step 5: Check whether the order is flagged as a final-sale or promotional purchase. If yes, deny refund regardless of defect claim.

Step 6: Check whether the item is a digital good that has been activated. If yes, deny refund and offer technical support pivot.

Step 7: If all eligibility criteria are met, confirm refund amount from order record and initiate refund to original payment method. State 3–5 business day timeline.

Step 8: If item arrived damaged and item_condition is unused/unopened, explicitly waive the return requirement and communicate this to the customer.

Step 9: For defective items (not arrived-damaged), optionally offer a prepaid return label even if return is not required.

Step 10: If failure_type is ambiguous or promotional terms cannot be confirmed, escalate to a human agent rather than approving or denying.

## Install Instructions

Deploy as a sub-skill under the refund_eligibility skill group. Bind the order lookup tool to retrieve: order_id, purchase_timestamp, item_category, promotional_flags (final_sale, black_friday, etc.), item_type (physical/digital), and order_amount. Configure days_since_purchase to be computed automatically from purchase_timestamp vs. runtime date. Set a high-value refund escalation threshold (e.g., $500) in the skill config. Ensure the skill can call the refund initiation API and the prepaid-label generation API. Link the skill to the subscription cancellation skill so that pro-rated subscription refund requests are routed correctly. Load the digital goods policy and final-sale policy as grounding documents.

## Test Instructions

1. Submit a test case with a valid order_id, days_since_purchase=7, item_condition=unused, failure_type=arrived_damaged — expect ELIGIBLE response with no-return-required language and 3–5 business day refund timeline. 2. Submit a test case with a valid order_id, days_since_purchase=21, failure_type=early_failure_normal_use, usage_duration=5_days — expect ELIGIBLE response with optional prepaid label offer. 3. Submit a test case with no order_id and no receipt — expect INELIGIBLE response requesting proof of purchase. 4. Submit a test case with a final_sale flag on the order — expect INELIGIBLE response citing promotional terms. 5. Submit a test case with item_type=digital and activation_status=activated — expect INELIGIBLE response with technical support pivot offer. 6. Submit a test case with days_since_purchase=25 and failure_type=ambiguous (description: 'just stopped working' after 20 days of use) — expect NEEDS_ESCALATION response routing to human agent. 7. Submit a test case with days_since_purchase=32 — expect INELIGIBLE response citing 30-day window expiration.
