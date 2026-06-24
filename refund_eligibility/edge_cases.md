# Edge Cases

- Customer reports unauthorized charge but the transaction IP matches their usual location (e.g., compromised device at home location) — IP mismatch trigger is absent; escalate rather than auto-lockdown.
- Customer is a gift recipient attempting to report fraud on behalf of the original purchaser — identity and account ownership must be verified before lockdown can be initiated.
- Transaction amount is $0 or negligible — confirm whether the charge is a legitimate authorization hold versus a true unauthorized transaction before initiating fraud protocol.
- Customer reports the unauthorized charge days or weeks after it occurred — assess whether delayed reporting affects card issuer dispute eligibility and flag accordingly in the fraud claim.
- Account lockdown fails due to a system error — agent must immediately escalate to a human security agent and not inform the customer that the account is locked until lockdown is confirmed.
- Customer insists on a refund timeline faster than 3–5 business days — agent must hold the stated timeline and not over-promise; escalate if customer requests expedited processing.
- IP mismatch is detected but customer claims they were traveling and made the purchase themselves — treat as potential false positive; do not auto-lock; request additional verification before proceeding.

- `Confirmed IP Mismatch Unauthorized Charge — Standard Fraud Lockdown` -> `eligible`
- `Unauthorized Charge Reported But No IP Mismatch Detectable` -> `needs_escalation`
- `Forgotten Annual Subscription Renewal — No Fraud Signal` -> `ineligible`
- `Customer Cannot Confirm Account Email After Lockdown Triggered` -> `needs_escalation`
- `Trial Period Overage Charge — No Unauthorized Access Claim` -> `ineligible`
- `Gift Recipient Reporting Health Safety Concern — No Fraud Signal` -> `ineligible`
- `Multiple Unauthorized Charges Across Different Orders With IP Mismatch` -> `needs_escalation`
