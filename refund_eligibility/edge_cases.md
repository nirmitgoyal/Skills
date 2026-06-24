# Edge Cases

- Customer provides a partial order number or a typo — agent should attempt a lookup but if no match is found, treat proof as unconfirmed and prompt for correction or an alternative document rather than outright denying.
- Customer provides a screenshot of an email confirmation rather than forwarding it — this should be treated as purchase_email_confirmation_provided == true provided the screenshot contains a visible order number or transaction detail.
- Gift recipient attempts a return without any documentation and the original purchaser is unavailable — no exceptions to the proof gate; escalate if the customer cannot retrieve any document.
- Customer has both an order number AND a bank statement but the order number resolves to a different amount than the bank statement — escalate rather than processing, as the discrepancy requires human verification.
- Customer is a repeat buyer and asks the agent to 'look up their account' as a substitute for proof — account lookup alone does not satisfy the proof-of-purchase gate unless a matching order number or transaction is confirmed from the lookup result.
- Customer provides proof of purchase from a third-party retailer (not a direct company order) — escalate to a human agent, as third-party purchase verification is outside this skill's scope.

- `Return request with valid order number provided` -> `eligible`
- `Return request with no proof of purchase of any kind` -> `ineligible`
- `Proof gate passed but return blocked by final-sale policy` -> `ineligible`
- `Return request supported only by bank statement transaction` -> `eligible`
- `Late delivery refund request with order number confirmed` -> `eligible`
- `Refund request with no proof and customer insists on escalation` -> `needs_escalation`
