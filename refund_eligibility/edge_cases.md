# Edge Cases

- Customer reports fraud but the charge matches a recently placed order from the correct IP and the customer may have forgotten making the purchase — do not auto-escalate; verify with customer before flagging as fraud.
- Refund amount is large and may require additional security team sign-off beyond the standard fraud workflow — communicate potential delay transparently.
- Customer is unable to receive the fraud claim confirmation email because their account email has been compromised — escalate to security team with alternate contact verification.
- Customer contacts support after already disputing the charge with their card issuer — note the external dispute, proceed with internal fraud claim, and inform the customer that duplicate refunds may be clawed back.
- Fraud report is filed by someone other than the account holder (e.g., a family member) — require identity verification of the account holder before locking or refunding.
- Multiple fraudulent orders are detected on the same account in a short period — escalate all order IDs together as a single fraud case rather than processing separately.
- Customer disputes a gift order placed by another person as unauthorized — distinguish between gift recipient confusion and actual account compromise before triggering fraud workflow.

- `Confirmed IP Mismatch With Customer Fraud Report` -> `eligible`
- `Customer Reports Unauthorized Charge No IP Data Available` -> `needs_escalation`
- `IP Mismatch Detected But Customer Does Not Report Unauthorized Charge` -> `needs_escalation`
- `Customer Cannot Confirm Account Email During Fraud Report` -> `needs_escalation`
- `Unauthorized Charge Report With No Matching Order ID In System` -> `needs_escalation`
- `Legitimate Authorized Purchase Disputed as Unauthorized Without Supporting Signals` -> `ineligible`
