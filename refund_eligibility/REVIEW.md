# Trust Packet Review

## Summary

Draft review packet for `refund_eligibility`.

## Source Inventory

Approved source bundle hash: `sha256:0abe1e5fa8b36514262a07d83900063071c3db22baf19a8d080e43870bbd1b0a`

## Policy Claims

- claim_1_test_001: Eligible when Customer ordered blue wireless headphones (Order #ORD-31502) but received red ones. Agent must confirm merchant error, offer full refund ($79.00) OR free exchange for blue headphones, and automatically cover return shipping. Based directly on src_slack_c0ba1v2k269_1781262649628429.
- claim_2_test_002: Eligible when Customer ordered size Medium black jacket (Order #ORD-55201) but received size Large. Customer wants the correct size, not a refund. Agent must offer free exchange for size Medium black jacket with return shipping covered, confirming the correct item details before finalizing.
- claim_3_test_003: Ineligible when Customer received exactly the item ordered but it does not fit well. No fulfillment error exists. Wrong-item policy does not apply. Agent must decline and may direct to standard return or sizing guidance. Analogous to src_slack_c0ba1v2k269_1781262732047749 (buyer dissatisfaction, not merchant error).
- claim_4_test_004: Escalate when Customer claims wrong item received but the provided order_id does not match any record in the system, so item_ordered cannot be confirmed. Agent cannot verify discrepancy and must escalate to a human agent rather than issuing a refund or exchange on unverified claim alone.
- claim_5_test_005: Escalate when Customer received wrong color variant and wants an exchange for the correct item. The correct variant is confirmed out of stock. Agent cannot auto-substitute and must escalate to a human agent to resolve the exchange or offer an alternative resolution such as a refund, with manager involvement.
- claim_6_test_006: Escalate when Customer purchased during a final-sale promotion and received the wrong item due to fulfillment error. The final-sale ineligibility rule conflicts with the merchant-error entitlement. Agent must not unilaterally deny or approve and must escalate to manager for confirmation before proceeding.
- claim_7_test_007: Ineligible when Customer demands a full refund AND a free exchange (both) for a wrong-item shipment. Policy allows only one remedy at the customer's choice. Agent must clarify that only one option may be selected and re-present the two choices. Request as stated is ineligible as submitted.

## Required Fields

- order_id
- item_ordered
- item_received

## Edge Cases

- Customer received wrong item on a final-sale order — merchant error may override final-sale policy but requires manager confirmation before any remedy is issued.
- Customer has already used or disposed of the wrong item and cannot return it — no-return refund or exchange may require manager approval; do not auto-deny.
- Wrong item received as a gift where the recipient (not the purchaser) contacts support — may require gifter's order details to verify; consider gift-return accommodation logic from src_slack_c0ba1v2k269_1781262772545439 as a reference for locating orders via gifter name/email.
- Wrong item involves a safety concern (allergen, medication, hazardous material) — must be escalated urgently and flagged to product/safety team regardless of refund/exchange outcome.
- Replacement item for exchange is a different price than item ordered — agent must not charge or credit a price difference without manager approval; flag and escalate.
- Customer reports wrong item but item_received field matches item_ordered in system records — possible labeling error or system mismatch; escalate rather than deny.
- Customer contacts support long after delivery (e.g., 60+ days) about a wrong item — standard wrong-item policy timeline may apply; confirm whether a return window cutoff exists before proceeding.
- test_001: Classic wrong color variant — eligible for refund or exchange -> pass
- test_002: Wrong variant with exchange preference -> pass
- test_003: Correct item received but poor fit — not a fulfillment error -> pass
- test_004: Wrong item shipped but order record unverifiable -> pass
- test_005: Wrong item shipped — replacement SKU out of stock -> pass
- test_006: Wrong item shipped on a final-sale order -> pass
- test_007: Wrong item shipped — customer requests both refund and exchange simultaneously -> pass

## Test Results

Generated deterministic pilot tests are included under `tests/`.

## This Is A Merchant Error Case Both Refund And Exchange Should Be Offered Cover Return Shipping Automatically Install/Test Instructions

Runtime profile: `runtimes/this_is_a_merchant_error_case_both_refund_and_exchange_should_be_offered_cover_return_shipping_automatically.md`

Owner: `[redacted-email]`

Install Instructions

Deploy this skill under the refund_eligibility skill namespace with trigger phrase matching on customer reports of receiving an incorrect item, wrong variant, wrong color, or wrong product relative to their order confirmation. Ensure the skill has read access to order management data to verify order_id, item_ordered, and item_received fields. Link escalation path to the human agent queue with priority flag for safety-related wrong-item cases. Do not chain this skill with subscription-refund or final-sale-return skills without an explicit escalation handoff node between them.

Test Instructions

1. Submit a conversation where customer provides a valid order_id and clearly states item_received differs from item_ordered — verify agent responds with both refund amount and exchange option plus return shipping coverage statement. 2. Submit a conversation where item_received matches item_ordered per system records — verify agent does not grant wrong-item remedy and either declines or escalates. 3. Submit a conversation where order_id is not found in the system — verify agent requests clarification and does not issue any remedy. 4. Submit a conversation where the correct exchange item is out of stock — verify agent escalates rather than substituting or auto-refunding without offering exchange. 5. Submit a conversation where the customer asks for both refund and exchange simultaneously — verify agent explains only one remedy is available and re-presents the choice. 6. Submit a final-sale wrong-item case — verify agent does not auto-deny and instead escalates to manager queue.

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
