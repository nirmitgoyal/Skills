# refund_eligibility

A return or refund request cannot be processed unless the customer provides at least one valid proof of purchase (order number, receipt, email order confirmation, or bank/card statement transaction). If no proof is provided, the request must be blocked and the customer must be prompted to supply documentation before any processing can occur. Once valid proof is provided, eligibility evaluation proceeds normally against other applicable policies.

## Decision Rules

- IF order_number_provided == true OR receipt_provided == true OR bank_statement_transaction_provided == true OR purchase_email_confirmation_provided == true THEN proof_of_purchase gate is PASSED and return eligibility evaluation may continue.
- IF order_number_provided == false AND receipt_provided == false AND bank_statement_transaction_provided == false AND purchase_email_confirmation_provided == false THEN return_processing = BLOCKED; prompt customer to supply at least one proof document before proceeding.
- The proof-of-purchase gate is a prerequisite check; it does not itself determine final refund eligibility — other policies (e.g., final sale, return window, shipping fault) still apply after the gate is passed.
- When the gate is blocked, the agent must explicitly name acceptable substitute documents: order confirmation email, bank or card statement showing the transaction, or a printed or digital receipt.
- The agent must not make exceptions to the proof-of-purchase gate regardless of the customer's reason for lacking documentation.
- Once any single qualifying proof document is provided, the gate is cleared and the agent proceeds immediately to evaluate the specific refund or return scenario without requiring additional proof documents.

## Required Fields

- order_number_provided
- receipt_provided
- bank_statement_transaction_provided
- purchase_email_confirmation_provided

## Escalation

- If the customer insists they cannot locate any proof document and requests a supervisor or escalation, route to a human agent — do not attempt to process the return without documentation.
- If the customer provides documentation that appears inconsistent (e.g., an order number that cannot be located in the system), do not unilaterally deny; escalate to a human agent for manual verification.
- If the customer states they purchased in-store and has no digital record, escalate to a human agent who can perform in-store purchase lookup procedures outside the scope of this skill.
