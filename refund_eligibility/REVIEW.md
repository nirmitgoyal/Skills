# Trust Packet Review

## Summary

Draft review packet for `refund_eligibility`.

## Source Inventory

Approved source bundle hash: `sha256:16ed34af79426b31b05001fdea61357cdd32ac59a3b71bbb4aea0168ddf49e6b`

## Policy Claims

- claim_1_test_001: Eligible when Customer reports a $230 unauthorized charge on Order #ORD-77654. Transaction IP does not match customer's usual location. Agent must immediately lock the account, flag IP mismatch to the security team, confirm fraud claim within 15 minutes, state the $230 refund will process in 3–5 business days, and instruct the customer to notify their card issuer. Agent must also request account email confirmation for the security alert. No human approval required for lockdown; human confirmation required only for fraud claim initiation. Backed by src_slack_c0ba1v2k269_1781262857848579.
- claim_2_test_002: Escalate when Customer reports an unauthorized charge but the system cannot retrieve or compare the transaction IP address against the customer's usual location. Because the IP mismatch signal—the primary deterministic trigger—cannot be confirmed, the agent must not auto-lock or auto-initiate the fraud claim. Instead, the case must be escalated to the security team for manual review before any further action is taken.
- claim_3_test_003: Ineligible when Customer reports a $99 annual renewal charge they forgot about after 11 months of non-usage. There is no IP mismatch and no claim of unauthorized access. This case does not qualify for the Fraudulent Account Security Lockdown Protocol. It must be routed to the standard refund eligibility flow (partial refund or full refund with manager approval), not the fraud lockdown path. Backed by src_slack_c0ba1v2k269_1781262784193319.
- claim_4_test_004: Escalate when Customer reports an unauthorized charge with a confirmed IP mismatch. Account lockdown is executed immediately. However, when the agent requests the customer's account email for the security alert, the customer is unable to provide it or provides one that does not match any record. The agent must pause fraud claim submission and escalate to a human security agent before proceeding, as email confirmation is a required field for security alert delivery.
- claim_5_test_005: Ineligible when Customer reports being charged $49 one day after their 7-day trial ended because they forgot to cancel. There is no report of unauthorized access, no IP mismatch, and no fraud indicators. This case does not meet the trigger conditions for the Fraudulent Account Security Lockdown Protocol and must be handled under the standard trial refund courtesy policy. Backed by src_slack_c0ba1v2k269_1781262670462979.
- claim_6_test_006: Ineligible when A gift recipient reports an allergic reaction to a skincare product and requests store credit. The original purchaser is not involved. There is no unauthorized transaction, no IP mismatch, and no fraud indicators. This case does not qualify for the Fraudulent Account Security Lockdown Protocol. It must be routed to the gift return and health safety exception flow. Backed by src_slack_c0ba1v2k269_1781262772545439.
- claim_7_test_007: Escalate when Customer reports multiple unauthorized charges across several order IDs, all showing IP mismatches from unfamiliar geographies. While the standard protocol covers a single fraud claim, multiple simultaneous unauthorized transactions indicate a broader account compromise. The agent must execute immediate account lockdown per protocol but then escalate to a dedicated fraud investigation team rather than processing multiple individual fraud claims autonomously.

## Required Fields

- customer_email
- order_id
- transaction_amount
- transaction_ip_address
- customer_usual_location

## Edge Cases

- Customer reports unauthorized charge but the transaction IP matches their usual location (e.g., compromised device at home location) — IP mismatch trigger is absent; escalate rather than auto-lockdown.
- Customer is a gift recipient attempting to report fraud on behalf of the original purchaser — identity and account ownership must be verified before lockdown can be initiated.
- Transaction amount is $0 or negligible — confirm whether the charge is a legitimate authorization hold versus a true unauthorized transaction before initiating fraud protocol.
- Customer reports the unauthorized charge days or weeks after it occurred — assess whether delayed reporting affects card issuer dispute eligibility and flag accordingly in the fraud claim.
- Account lockdown fails due to a system error — agent must immediately escalate to a human security agent and not inform the customer that the account is locked until lockdown is confirmed.
- Customer insists on a refund timeline faster than 3–5 business days — agent must hold the stated timeline and not over-promise; escalate if customer requests expedited processing.
- IP mismatch is detected but customer claims they were traveling and made the purchase themselves — treat as potential false positive; do not auto-lock; request additional verification before proceeding.
- test_001: Confirmed IP Mismatch Unauthorized Charge — Standard Fraud Lockdown -> pass
- test_002: Unauthorized Charge Reported But No IP Mismatch Detectable -> pass
- test_003: Forgotten Annual Subscription Renewal — No Fraud Signal -> pass
- test_004: Customer Cannot Confirm Account Email After Lockdown Triggered -> pass
- test_005: Trial Period Overage Charge — No Unauthorized Access Claim -> pass
- test_006: Gift Recipient Reporting Health Safety Concern — No Fraud Signal -> pass
- test_007: Multiple Unauthorized Charges Across Different Orders With IP Mismatch -> pass

## Test Results

Generated deterministic pilot tests are included under `tests/`.

## Deterministic Security Event Requires Human Confirmation Only For Fraud Claim Initiation Install/Test Instructions

Runtime profile: `runtimes/deterministic_security_event_requires_human_confirmation_only_for_fraud_claim_initiation.md`

Owner: `[redacted-email]`

Install Instructions

Deploy this skill under the refund_eligibility skill slug with a dedicated intent classifier trigger keyed on: (1) customer self-report of unauthorized charge, AND (2) system-detected IP address mismatch against customer_usual_location. Ensure the account lockdown API call is the first action executed upon trigger confirmation, before any outbound message is composed. Wire the fraud claim initiation step to a human-in-the-loop confirmation checkpoint. Confirm that the security team alert webhook is active and that the 15-minute SLA for fraud claim confirmation is monitored. All five required input fields (transaction_amount, order_id, customer_email, transaction_ip_address, customer_usual_location) must be validated as present before the skill resolves autonomously; missing fields must trigger an input-collection loop. Ensure fallback routing to the standard refund_eligibility flow for cases that do not meet both trigger conditions.

Test Instructions

To validate this skill in staging: (1) Submit a synthetic fraud report with a confirmed IP mismatch and all five required fields populated — verify account lockdown fires first, security flag is sent, fraud claim confirmation is scheduled within 15 minutes, refund amount is stated correctly, and customer is advised to contact their card issuer. (2) Submit a fraud report with transaction_ip_address missing — verify the skill enters input-collection mode rather than proceeding. (3) Submit a non-fraud refund scenario (e.g., forgotten renewal) and verify the skill does not trigger lockdown and routes to standard refund flow. (4) Simulate a lockdown API failure and verify immediate human escalation is triggered. (5) Submit a fraud report where the customer cannot confirm their account email and verify that fraud claim initiation is paused and escalated to a human agent. Review all responses for compliance with the 3–5 business day refund timeline and presence of card issuer advisory language.

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
