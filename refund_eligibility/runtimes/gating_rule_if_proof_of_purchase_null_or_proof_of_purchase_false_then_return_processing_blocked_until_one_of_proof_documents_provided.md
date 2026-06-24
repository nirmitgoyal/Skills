# Gating Rule If Proof Of Purchase Null Or Proof Of Purchase False Then Return Processing Blocked Until One Of Proof Documents Provided Runtime Profile

## Guidance

At the start of every return or refund conversation, evaluate all four proof fields before taking any other action: order_number_provided, receipt_provided, bank_statement_transaction_provided, purchase_email_confirmation_provided.

If all four fields are false or null, immediately block processing and respond with a message that names all four acceptable document types so the customer knows their options.

Do not apologize in a way that implies the agent will make an exception to the proof requirement — empathy is appropriate, but the gate must remain firm.

Once any single proof field flips to true, do not re-challenge the customer for additional proof; proceed directly to the next eligibility evaluation step.

When prompting for proof, suggest the most commonly accessible document first: 'Please check your email for an order confirmation, or find the charge on your bank or card statement.'

Never guess or infer an order number from context clues in the conversation; only mark order_number_provided == true if the customer explicitly supplies a verifiable identifier.

If the proof gate is cleared but the order is flagged as final sale, communicate the denial clearly and do not suggest that providing more documentation would change the outcome.

Log which proof document type was used to clear the gate for audit and compliance purposes.

## Install Instructions

Deploy this skill under the 'refund_eligibility' skill slug. Ensure the four boolean input fields (order_number_provided, receipt_provided, bank_statement_transaction_provided, purchase_email_confirmation_provided) are surfaced in the conversation context before the skill evaluates any return or refund scenario. The gating check must execute as the first step in the skill's decision tree, prior to any policy-specific evaluation (e.g., return window, final sale, shipping fault). Wire the escalation path so that a human agent queue is reachable when the customer confirms they cannot provide any proof document. No fallback processing of returns without proof is permitted at the automated layer.

## Test Instructions

1. Simulate a return request with order_number_provided=true; verify the agent proceeds past the gate to policy evaluation without re-requesting proof. 2. Simulate a return request with all four proof fields set to false; verify the agent blocks processing and enumerates all four acceptable document types in the response. 3. Simulate the gate-blocked scenario followed by the customer supplying a bank statement entry; set bank_statement_transaction_provided=true in the second turn and verify the gate clears immediately. 4. Simulate a return where order_number_provided=true but the order is tagged as a final-sale event; verify the denial message references final-sale policy, not missing proof. 5. Simulate a customer with no proof who explicitly requests escalation; verify the skill routes to the human agent queue without processing the return. 6. Confirm no test case allows a return to be processed when all four proof fields remain false, regardless of other eligibility signals.
