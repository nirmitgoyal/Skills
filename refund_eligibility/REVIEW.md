# Trust Packet Review

## Summary

Draft review packet for `refund_eligibility`.

## Source Inventory

Approved source bundle hash: `sha256:377c8d49b8079ead4570697a43c6111b324b182b193a54b0f79a70041aa73c0d`

## Policy Claims

- claim_1_test_001: Eligible when Customer reports an unauthorized charge on Order #ORD-77654 for $230. System confirms the order was placed from an IP that does not match the customer's usual login location. Agent must lock the account immediately, flag the transaction as fraudulent, escalate to the security team, send fraud claim confirmation within 15 minutes, communicate a 35-business-day refund timeline, advise the customer to contact their card issuer, and confirm the customer's account email before dispatching the security alert. Refund is eligible for full amount.
- claim_2_test_002: Escalate when Customer reports an unauthorized charge but the system cannot retrieve reported_ip_location or usual_login_location data. Only one fraud signal (customer report) is present without IP corroboration. Agent must lock the account as a precaution, escalate to the security team for manual review, and must not process the refund autonomously until the security team confirms fraud. Do not deny the claim; hold pending escalation.
- claim_3_test_003: Escalate when System detects a login from an IP address that does not match the customer's usual location, but the customer has not reported an unauthorized charge or account compromise. Only one fraud signal is present. Agent must escalate to the security team for review, alert the customer to the suspicious login, and must not initiate a refund without a confirmed fraud claim. Escalation is required before any further action.
- claim_4_test_004: Escalate when Customer reports an unauthorized charge and IP mismatch is confirmed, but the customer is unable to confirm the account email associated with the order when prompted. Agent must not dispatch the security alert without email confirmation per the workflow rule. Agent must escalate to the security team for identity verification before proceeding. Account should still be locked as a precautionary measure.
- claim_5_test_005: Escalate when Customer reports an unauthorized charge referencing an order_id that cannot be located in the system or is associated with a different account. Agent must not deny the claim outright and must not attempt self-service resolution. The case must be escalated to the security team for manual investigation. The agent should advise the customer to also contact their card issuer while the internal investigation proceeds.
- claim_6_test_006: Ineligible when Customer claims a charge is unauthorized, but the system shows the order was placed from the customer's usual IP location with no IP mismatch flag, no customer escalation flag, and the customer's account shows recent normal login activity. No fraud signals are present. The transaction does not meet the criteria for the fraud workflow. Agent must not lock the account or file a fraud claim and should inform the customer that no fraud indicators were detected, directing them to the standard return/refund process if applicable.

## Required Fields

- order_id
- customer_email
- reported_ip_location
- usual_login_location

## Edge Cases

- Customer reports fraud but the charge matches a recently placed order from the correct IP and the customer may have forgotten making the purchase — do not auto-escalate; verify with customer before flagging as fraud.
- Refund amount is large and may require additional security team sign-off beyond the standard fraud workflow — communicate potential delay transparently.
- Customer is unable to receive the fraud claim confirmation email because their account email has been compromised — escalate to security team with alternate contact verification.
- Customer contacts support after already disputing the charge with their card issuer — note the external dispute, proceed with internal fraud claim, and inform the customer that duplicate refunds may be clawed back.
- Fraud report is filed by someone other than the account holder (e.g., a family member) — require identity verification of the account holder before locking or refunding.
- Multiple fraudulent orders are detected on the same account in a short period — escalate all order IDs together as a single fraud case rather than processing separately.
- Customer disputes a gift order placed by another person as unauthorized — distinguish between gift recipient confusion and actual account compromise before triggering fraud workflow.
- test_001: Confirmed IP Mismatch With Customer Fraud Report -> pass
- test_002: Customer Reports Unauthorized Charge No IP Data Available -> pass
- test_003: IP Mismatch Detected But Customer Does Not Report Unauthorized Charge -> pass
- test_004: Customer Cannot Confirm Account Email During Fraud Report -> pass
- test_005: Unauthorized Charge Report With No Matching Order ID In System -> pass
- test_006: Legitimate Authorized Purchase Disputed as Unauthorized Without Supporting Signals -> pass

## Test Results

Generated deterministic pilot tests are included under `tests/`.

## Deterministic Check Ip Mismatch Customer Escalation Flag Security Team Escalation Fraud Claim Initiation Install/Test Instructions

Runtime profile: `runtimes/deterministic_check_ip_mismatch_customer_escalation_flag_security_team_escalation_fraud_claim_initiation.md`

Owner: `[redacted-email]`

Install Instructions

Deploy this skill under the 'refund_eligibility' skill slug. Attach to triggers: (1) customer message containing keywords indicating unauthorized charge, account compromise, or fraudulent transaction; (2) system event for IP mismatch detection on login. Ensure the runtime has read access to order management system for order_id lookup, IP log data for mismatch comparison, and write access to account lockdown controls and fraud claim filing API. Security team escalation webhook must be configured and tested before go-live. Fraud claim confirmation email template must be pre-loaded with a 15-minute SLA dispatch requirement. Set refund SLA parameter to 35 business days in the refund processing module. Manager approval workflow must be accessible for escalated high-value cases.

Test Instructions

1. Simulate a customer message reporting an unauthorized charge with a valid order_id and confirm the agent locks the account, escalates to the security team, requests account email, and communicates the 35-business-day SLA. 2. Inject a system IP mismatch event without a customer fraud report and confirm the agent escalates rather than self-resolving. 3. Provide a fraud report with an unrecognized order_id and confirm the agent escalates rather than denying. 4. Provide a fraud report but withhold the customer email and confirm the agent requests it before dispatching the security alert. 5. Simulate a dispute with no IP mismatch and no escalation flag and confirm the agent routes to standard refund flow rather than fraud workflow. 6. Verify fraud claim confirmation is triggered within the 15-minute window in the staging environment. 7. Confirm account lockdown API call is the first outbound action in all confirmed fraud scenarios.

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
