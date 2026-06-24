# Deterministic Security Event Requires Human Confirmation Only For Fraud Claim Initiation Runtime Profile

## Guidance

Always lock the account before any other communication when IP mismatch and unauthorized charge are both confirmed — do not delay lockdown pending customer response.

Always state the exact dollar amount of the refund in the response to avoid ambiguity.

Always instruct the customer to contact their card issuer to dispute the charge independently, in addition to the internal refund process.

Always request and confirm the customer's account email before sending the security alert — this is a required field.

Never promise a refund timeline shorter than 3–5 business days for fraud claims.

Never skip the security team flag step even if the refund amount is small — IP mismatch fraud protocol is mandatory regardless of transaction value.

Always generate and communicate that the fraud claim confirmation will be delivered within 15 minutes.

Do not auto-initiate the fraud claim without human confirmation at that specific step, even though all other lockdown actions are deterministic.

If any required input field (transaction_ip_address, customer_usual_location, order_id, transaction_amount, customer_email) is missing, request it before proceeding with the protocol.

Route all non-fraud refund scenarios (forgotten renewals, trial expirations, gift returns) to their respective standard flows — do not apply this protocol to non-fraud cases.

## Install Instructions

Deploy this skill under the refund_eligibility skill slug with a dedicated intent classifier trigger keyed on: (1) customer self-report of unauthorized charge, AND (2) system-detected IP address mismatch against customer_usual_location. Ensure the account lockdown API call is the first action executed upon trigger confirmation, before any outbound message is composed. Wire the fraud claim initiation step to a human-in-the-loop confirmation checkpoint. Confirm that the security team alert webhook is active and that the 15-minute SLA for fraud claim confirmation is monitored. All five required input fields (transaction_amount, order_id, customer_email, transaction_ip_address, customer_usual_location) must be validated as present before the skill resolves autonomously; missing fields must trigger an input-collection loop. Ensure fallback routing to the standard refund_eligibility flow for cases that do not meet both trigger conditions.

## Test Instructions

To validate this skill in staging: (1) Submit a synthetic fraud report with a confirmed IP mismatch and all five required fields populated — verify account lockdown fires first, security flag is sent, fraud claim confirmation is scheduled within 15 minutes, refund amount is stated correctly, and customer is advised to contact their card issuer. (2) Submit a fraud report with transaction_ip_address missing — verify the skill enters input-collection mode rather than proceeding. (3) Submit a non-fraud refund scenario (e.g., forgotten renewal) and verify the skill does not trigger lockdown and routes to standard refund flow. (4) Simulate a lockdown API failure and verify immediate human escalation is triggered. (5) Submit a fraud report where the customer cannot confirm their account email and verify that fraud claim initiation is paused and escalated to a human agent. Review all responses for compliance with the 3–5 business day refund timeline and presence of card issuer advisory language.
