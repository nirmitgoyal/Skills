# Deterministic Check Ip Mismatch Customer Escalation Flag Security Team Escalation Fraud Claim Initiation Runtime Profile

## Guidance

Always lock the account before any other action when a fraud flag is confirmed.

Always confirm the customer's account email before sending the security alert.

Always communicate the 35-business-day refund SLA explicitly; do not imply a faster timeline.

Always instruct the customer to contact their card issuer independently to dispute the charge.

Never process a standard refund for a fraud case; route exclusively through the fraud claim and security escalation workflow.

Always send fraud claim confirmation to the customer within 15 minutes of the fraud flag being raised.

If both IP mismatch and customer escalation flag are present, treat as confirmed fraud and proceed without waiting for additional verification.

If only one fraud signal is present, do not self-resolve; escalate to security team for manual review.

Do not deny a fraud claim solely because the order_id cannot be found; escalate to security team instead.

Maintain a professional, urgent, and empathetic tone — unauthorized charges are high-stress events for customers and the agent must communicate top-priority handling immediately.

## Install Instructions

Deploy this skill under the 'refund_eligibility' skill slug. Attach to triggers: (1) customer message containing keywords indicating unauthorized charge, account compromise, or fraudulent transaction; (2) system event for IP mismatch detection on login. Ensure the runtime has read access to order management system for order_id lookup, IP log data for mismatch comparison, and write access to account lockdown controls and fraud claim filing API. Security team escalation webhook must be configured and tested before go-live. Fraud claim confirmation email template must be pre-loaded with a 15-minute SLA dispatch requirement. Set refund SLA parameter to 35 business days in the refund processing module. Manager approval workflow must be accessible for escalated high-value cases.

## Test Instructions

1. Simulate a customer message reporting an unauthorized charge with a valid order_id and confirm the agent locks the account, escalates to the security team, requests account email, and communicates the 35-business-day SLA. 2. Inject a system IP mismatch event without a customer fraud report and confirm the agent escalates rather than self-resolving. 3. Provide a fraud report with an unrecognized order_id and confirm the agent escalates rather than denying. 4. Provide a fraud report but withhold the customer email and confirm the agent requests it before dispatching the security alert. 5. Simulate a dispute with no IP mismatch and no escalation flag and confirm the agent routes to standard refund flow rather than fraud workflow. 6. Verify fraud claim confirmation is triggered within the 15-minute window in the staging environment. 7. Confirm account lockdown API call is the first outbound action in all confirmed fraud scenarios.
