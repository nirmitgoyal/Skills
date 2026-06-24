# refund_eligibility

When a customer reports an unauthorized charge and the transaction IP does not match their usual location, the agent must immediately lock the account, flag the IP mismatch to the security team, generate a fraud claim confirmation within 15 minutes, and initiate the standard refund timeline of 3–5 business days. The agent must also instruct the customer to notify their card issuer. Human confirmation is required only at the fraud claim initiation step. All other lockdown actions are deterministic and must execute without delay.

## Decision Rules

- IF customer reports an unauthorized charge AND transaction IP does not match customer's usual location THEN lock account immediately, flag IP mismatch to security team, generate fraud claim confirmation within 15 minutes, and initiate refund.
- IF customer reports an unauthorized charge BUT IP mismatch cannot be confirmed THEN escalate to security team for manual review before taking further action.
- IF account lockdown is triggered THEN agent must collect and confirm customer account email before sending security alert.
- IF fraud claim is initiated THEN inform customer that refund will be processed within 3–5 business days and advise them to dispute the charge with their card issuer.
- IF transaction amount is present in the report THEN explicitly state the exact refund amount in the response.
- IF IP mismatch is detected THEN do not wait for customer confirmation before locking the account; lockdown is immediate and automatic.
- IF customer cannot provide account email confirmation THEN escalate to human security agent before proceeding with fraud claim submission.
- NEVER promise a refund timeline shorter than 3–5 business days for fraud-related claims based on source evidence.

## Required Fields

- customer_email
- order_id
- transaction_amount
- transaction_ip_address
- customer_usual_location

## Escalation

- Escalate to the security team immediately upon detecting an IP location mismatch flagged as a fraudulent transaction; this is non-negotiable and must not be deferred.
- If the customer cannot confirm their account email for the security alert, pause automated processing and route to a human security agent.
- If the transaction IP cannot be retrieved or compared against the customer's usual location, escalate to the security team for manual adjudication rather than auto-resolving.
- If the transaction amount exceeds a high-value threshold not explicitly defined in policy (e.g., significantly above $230), flag for senior security review in addition to standard protocol.
- If the customer reports multiple unauthorized charges across different orders, escalate beyond standard fraud claim protocol to a dedicated fraud investigation team.
