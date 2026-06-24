# This Is A Merchant Error Case Both Refund And Exchange Should Be Offered Cover Return Shipping Automatically Runtime Profile

## Guidance

Always retrieve and confirm order_id, item_ordered, and item_received before making any eligibility determination.

Classify the case as merchant error if item_received differs materially from item_ordered; do not require the customer to prove fault.

Present both refund and exchange as equally valid options in the same message; never suggest one is preferred or easier.

State the exact refund dollar amount and the exact replacement item (name, variant, SKU if available) when presenting options.

Confirm return shipping is covered by the merchant in every eligible wrong-item case — include this statement proactively, not only if asked.

Do not apply subscription-lapse, trial-expiry, or gift-return policy logic to wrong-item fulfillment cases.

If any required field (order_id, item_ordered, item_received) is missing, ask for it before proceeding — do not guess or assume.

If the exchange item is out of stock, do not substitute a different product; escalate immediately.

For safety-related wrong-item cases, escalate urgently and note the safety concern explicitly in the escalation record.

After the customer selects refund or exchange, confirm the chosen action, the next steps, and the expected timeline before closing the interaction.

## Install Instructions

Deploy this skill under the refund_eligibility skill namespace with trigger phrase matching on customer reports of receiving an incorrect item, wrong variant, wrong color, or wrong product relative to their order confirmation. Ensure the skill has read access to order management data to verify order_id, item_ordered, and item_received fields. Link escalation path to the human agent queue with priority flag for safety-related wrong-item cases. Do not chain this skill with subscription-refund or final-sale-return skills without an explicit escalation handoff node between them.

## Test Instructions

1. Submit a conversation where customer provides a valid order_id and clearly states item_received differs from item_ordered — verify agent responds with both refund amount and exchange option plus return shipping coverage statement. 2. Submit a conversation where item_received matches item_ordered per system records — verify agent does not grant wrong-item remedy and either declines or escalates. 3. Submit a conversation where order_id is not found in the system — verify agent requests clarification and does not issue any remedy. 4. Submit a conversation where the correct exchange item is out of stock — verify agent escalates rather than substituting or auto-refunding without offering exchange. 5. Submit a conversation where the customer asks for both refund and exchange simultaneously — verify agent explains only one remedy is available and re-presents the choice. 6. Submit a final-sale wrong-item case — verify agent does not auto-deny and instead escalates to manager queue.
