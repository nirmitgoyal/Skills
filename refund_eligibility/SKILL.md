# refund_eligibility

Determine whether a customer is eligible for a full refund on an item that arrived damaged or failed due to a manufacturing defect. Eligibility requires: (1) the order falls within the 30-day purchase window, (2) the failure is attributable to damage-on-arrival or a manufacturing defect rather than normal wear, misuse, or change-of-mind, and (3) the item is unused/unopened at time of damage discovery for no-return-required refunds. Defective items that failed after a short period of normal use may still qualify within the 30-day window. Proof of purchase (order number or receipt) is mandatory. Final-sale or promotional items and activated digital goods are categorically excluded. Eligible refunds are processed back to the original payment method within 3–5 business days; no return is required for damaged/defective items unless the agent optionally offers a prepaid label.

## Decision Rules

- ELIGIBLE if: order_id or proof of purchase is present AND days_since_purchase <= 30 AND failure_type is one of [arrived_damaged, manufacturing_defect, early_failure_normal_use] AND item is not a final-sale/promotional item AND item is not an activated digital good.
- ELIGIBLE (no return required) if: item arrived damaged AND item_condition is unused/unopened at time of damage discovery — waive return requirement and process full refund.
- ELIGIBLE (defect after brief normal use) if: usage_duration is short relative to expected product lifespan AND failure is consistent with manufacturing defect AND days_since_purchase <= 30.
- INELIGIBLE if: proof of purchase (order_id or receipt or bank statement reference) cannot be located — request proof before proceeding.
- INELIGIBLE if: days_since_purchase > 30 — outside the 30-day refund window.
- INELIGIBLE if: item was purchased under a final-sale or promotional event explicitly marked non-refundable at checkout.
- INELIGIBLE if: item is a digital good (software license, subscription activation) that has already been downloaded and activated — no refund for consumed digital products; pivot to technical support offer.
- INELIGIBLE if: failure_type is change_of_mind, wrong_size, or buyer_remorse without any defect claim.
- NEEDS_ESCALATION if: customer claims defect but usage_duration and failure description are ambiguous between normal wear and manufacturing defect.
- NEEDS_ESCALATION if: order exists and is within 30 days but item category or promotional terms are unclear and agent cannot confirm final-sale status.
- NEEDS_ESCALATION if: customer provides partial proof of purchase (e.g., bank statement only, no order number) and purchase cannot be confirmed in the system.
- Always confirm order_id lookup before quoting any refund amount.
- Optionally offer a prepaid return label for defective items even when return is not required.

## Required Fields

- order_id (or equivalent proof of purchase such as receipt or bank statement reference)
- days_since_purchase (derived from order timestamp vs. current date)
- item_condition (unused/unopened vs. in-use at time of damage/defect discovery)
- failure_type (arrived_damaged | manufacturing_defect | early_failure_normal_use | change_of_mind | other)
- usage_duration (how long item was in use before failure, if applicable)

## Escalation

- Escalate when failure_type is ambiguous and cannot be clearly classified as manufacturing defect vs. normal wear — do not deny or approve without human review.
- Escalate when the item category has a separate or specialty return policy (e.g., appliances, electronics with extended warranty programs) that the agent cannot independently verify.
- Escalate when customer provides only a bank/card statement reference but no order number and the system cannot locate the transaction — do not flatly deny; route to human agent to attempt manual lookup.
- Escalate when refund amount exceeds a high-value threshold (threshold to be configured at runtime) to require supervisor approval.
- Escalate when customer disputes a final-sale classification, claiming they were not informed at checkout.
