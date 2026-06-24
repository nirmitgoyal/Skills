# Trust Packet Review

## Summary

Draft review packet for `refund_eligibility`.

## Source Inventory

Approved source bundle hash: `sha256:4d6f4414c65ea0706994de4183f2de88ec2ed50d1722ea98716f5d5e77f7b79f`

## Policy Claims

- claim_1_dt_001: Eligible when Customer requests a return and supplies a valid order number (e.g., ORD-31502). The proof-of-purchase gate is cleared because order_number_provided == true. Processing proceeds to evaluate the specific return scenario. Backed by src_slack_c0ba1v2k269_1781262649628429, where Order #ORD-31502 was accepted as sufficient proof to initiate refund or exchange processing.
- claim_2_dt_002: Ineligible when Customer requests a refund for a gift purchase but cannot provide an order number, receipt, bank statement, or email confirmation. All four proof fields are false. Return processing is blocked. Agent prompts the customer to check email for an order confirmation or locate the charge on a bank or card statement. Backed by src_slack_c0ba1v2k269_1781262721847029, where the agent explicitly declined to process without proof and listed acceptable substitute documents.
- claim_3_dt_003: Ineligible when Customer provides a valid order number (ORD-67890), so the proof-of-purchase gate is cleared. However, the order was placed during a final-sale promotional event, making the item non-refundable and non-returnable per the disclosed promotional terms. Eligibility is denied on policy grounds after the gate is passed, not because of missing proof. Backed by src_slack_c0ba1v2k269_1781262732047749.
- claim_4_dt_004: Eligible when Customer cannot locate their order number or receipt but provides a bank statement entry showing the transaction amount and merchant. bank_statement_transaction_provided == true satisfies the proof-of-purchase gate as an acceptable substitute document. Processing proceeds to evaluate the specific return scenario. Backed by the agent guidance in src_slack_c0ba1v2k269_1781262721847029, which explicitly cites 'the transaction on your bank/card statement' as a qualifying proof document.
- claim_5_dt_005: Eligible when Customer supplies Order #ORD-55120 and reports a package arrived 8 days after a promised 2-day delivery window, rendering the gift item unusable. order_number_provided == true clears the proof gate. Post-gate evaluation finds the late delivery constitutes carrier fault, qualifying the customer for a full refund including the shipping fee. Backed by src_slack_c0ba1v2k269_1781262686690199.
- claim_6_dt_006: Escalate when Customer cannot provide any form of proof of purchase and, after being prompted to retrieve documentation, insists they have none and demands to speak with a supervisor. The agent cannot process the return without documentation and must not fabricate an exception. The request must be escalated to a human agent for manual handling. Backed by the escalation rule derived from the gating policy established in src_slack_c0ba1v2k269_1781262721847029 and the runtime gating logic.

## Required Fields

- order_number_provided
- receipt_provided
- bank_statement_transaction_provided
- purchase_email_confirmation_provided

## Edge Cases

- Customer provides a partial order number or a typo — agent should attempt a lookup but if no match is found, treat proof as unconfirmed and prompt for correction or an alternative document rather than outright denying.
- Customer provides a screenshot of an email confirmation rather than forwarding it — this should be treated as purchase_email_confirmation_provided == true provided the screenshot contains a visible order number or transaction detail.
- Gift recipient attempts a return without any documentation and the original purchaser is unavailable — no exceptions to the proof gate; escalate if the customer cannot retrieve any document.
- Customer has both an order number AND a bank statement but the order number resolves to a different amount than the bank statement — escalate rather than processing, as the discrepancy requires human verification.
- Customer is a repeat buyer and asks the agent to 'look up their account' as a substitute for proof — account lookup alone does not satisfy the proof-of-purchase gate unless a matching order number or transaction is confirmed from the lookup result.
- Customer provides proof of purchase from a third-party retailer (not a direct company order) — escalate to a human agent, as third-party purchase verification is outside this skill's scope.
- dt_001: Return request with valid order number provided -> pass
- dt_002: Return request with no proof of purchase of any kind -> pass
- dt_003: Proof gate passed but return blocked by final-sale policy -> pass
- dt_004: Return request supported only by bank statement transaction -> pass
- dt_005: Late delivery refund request with order number confirmed -> pass
- dt_006: Refund request with no proof and customer insists on escalation -> pass

## Test Results

Generated deterministic pilot tests are included under `tests/`.

## Gating Rule If Proof Of Purchase Null Or Proof Of Purchase False Then Return Processing Blocked Until One Of Proof Documents Provided Install/Test Instructions

Runtime profile: `runtimes/gating_rule_if_proof_of_purchase_null_or_proof_of_purchase_false_then_return_processing_blocked_until_one_of_proof_documents_provided.md`

Owner: `[redacted-email]`

Install Instructions

Deploy this skill under the 'refund_eligibility' skill slug. Ensure the four boolean input fields (order_number_provided, receipt_provided, bank_statement_transaction_provided, purchase_email_confirmation_provided) are surfaced in the conversation context before the skill evaluates any return or refund scenario. The gating check must execute as the first step in the skill's decision tree, prior to any policy-specific evaluation (e.g., return window, final sale, shipping fault). Wire the escalation path so that a human agent queue is reachable when the customer confirms they cannot provide any proof document. No fallback processing of returns without proof is permitted at the automated layer.

Test Instructions

1. Simulate a return request with order_number_provided=true; verify the agent proceeds past the gate to policy evaluation without re-requesting proof. 2. Simulate a return request with all four proof fields set to false; verify the agent blocks processing and enumerates all four acceptable document types in the response. 3. Simulate the gate-blocked scenario followed by the customer supplying a bank statement entry; set bank_statement_transaction_provided=true in the second turn and verify the gate clears immediately. 4. Simulate a return where order_number_provided=true but the order is tagged as a final-sale event; verify the denial message references final-sale policy, not missing proof. 5. Simulate a customer with no proof who explicitly requests escalation; verify the skill routes to the human agent queue without processing the return. 6. Confirm no test case allows a return to be processed when all four proof fields remain false, regardless of other eligibility signals.

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
