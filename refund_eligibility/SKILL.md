# refund_eligibility

When a customer reports an unauthorized charge or when the system detects a login from an IP address that does not match the customer's usual location, the agent must immediately lock the account, flag the transaction as fraudulent, escalate to the security team, issue a fraud claim confirmation within 15 minutes, and initiate a refund processed within 35 business days. The customer must also be advised to contact their card issuer independently. Account email must be confirmed before dispatching the security alert.

## Decision Rules

- IF customer explicitly reports an unauthorized charge AND order_id is present THEN lock account immediately, flag order as fraudulent, escalate to security team, and initiate fraud claim.
- IF system detects IP mismatch (reported_ip_location != usual_login_location) AND customer escalation flag is set THEN treat as confirmed fraud signal and trigger full fraud workflow.
- IF either condition (customer report OR IP mismatch) is present without the other THEN escalate to security team for manual review before proceeding with refund.
- Fraud claim confirmation must be sent to the customer within 15 minutes of fraud flag being raised.
- Refund SLA is 35 business days from the date the fraud claim is filed; communicate this timeline explicitly to the customer.
- Customer must be instructed to notify their card issuer to dispute the charge independently, regardless of internal refund status.
- Account email must be confirmed from the customer before sending the security alert.
- Do NOT process a standard refund flow for unauthorized charges; always route through the fraud claim and security escalation workflow.
- Account lockdown is mandatory and must precede all other steps to prevent further unauthorized activity.
- If order_id cannot be located or customer cannot confirm account email, escalate to security team and do not attempt self-service resolution.

## Required Fields

- order_id
- customer_email
- reported_ip_location
- usual_login_location

## Escalation

- Escalate to security team immediately when IP mismatch is confirmed alongside a customer fraud report.
- Escalate to security team for manual review when only one fraud signal is present (report without IP mismatch, or IP mismatch without customer report).
- If the account email cannot be confirmed by the customer, hold the security alert and escalate to the security team for identity verification before proceeding.
- If the order_id does not exist in the system or belongs to a different account, escalate to security team rather than denying the claim outright.
- Any refund amount above a threshold requiring manager approval (inferred from edge-case evidence showing manager approval for full subscription refunds) should also be flagged for security team sign-off in fraud cases.
