# refund_eligibility

When a customer receives an item materially different from what was ordered (wrong color, wrong variant, wrong product) due to a fulfillment error, the agent must offer both a full refund and a free exchange as co-equal options, letting the customer choose. Return shipping must be covered by the merchant automatically without the customer needing to request it. This is a merchant-error case and no fault or policy exception language should be applied. The agent should confirm the specific dollar amount of the refund and the exact correct item for the exchange before finalizing.

## Decision Rules

- ELIGIBLE if the item received is materially different from the item on the order confirmation (e.g., wrong color, wrong variant, wrong SKU) and the discrepancy is attributable to a fulfillment error.
- Both a full refund AND a free exchange must be offered simultaneously; the customer selects one — never pre-select or favor one option over the other.
- Return shipping must be covered by the merchant in all eligible wrong-item cases; this is automatic and must not be contingent on customer request.
- The agent must confirm the exact refund amount and the exact correct replacement item details before asking the customer to decide.
- INELIGIBLE if the customer received the correct item but dislikes it (e.g., fit, preference, buyer's remorse) — wrong-item policy does not apply in those cases.
- INELIGIBLE if the item was purchased under a final-sale or non-returnable promotion, unless the error is a merchant fulfillment mistake — in that case, escalate rather than deny.
- NEEDS_ESCALATION if the order cannot be located, if the item_received versus item_ordered discrepancy cannot be verified from order records, or if the exchange replacement item is out of stock.
- NEEDS_ESCALATION if the customer requests compensation beyond refund or exchange (e.g., additional store credit, monetary damages) for a wrong-item shipment.
- Do not apply subscription, trial, or gift-return logic to wrong-item fulfillment error cases — those are governed by separate policies.

## Required Fields

- order_id
- item_ordered
- item_received

## Escalation

- Escalate to a human agent if the replacement item for exchange is out of stock and the customer still wants an exchange — do not auto-substitute a different item.
- Escalate if the order record cannot confirm a discrepancy between item_ordered and item_received — do not issue a refund or exchange on the customer's unverified word alone without order data.
- Escalate if the wrong-item case intersects with a final-sale order — the final-sale ineligibility rule may be overridden by merchant error but requires manager confirmation.
- Escalate if the customer reports a safety concern (e.g., wrong medication, allergen-containing product shipped) — treat as urgent and flag to the product and safety team immediately.
- Escalate if the customer has already disposed of or used the wrong item and return shipping is impossible — a no-return refund or exchange may require manager approval.
