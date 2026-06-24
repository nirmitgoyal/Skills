# Edge Cases

- Customer claims they never actually used or activated the license despite the system showing activation_status_confirmed=true—do not override confirmed system data; apply denial and note the discrepancy, escalating if the customer disputes system records.
- Customer activated the license but immediately discovered it is incompatible with their operating system—treat as a potential technical issue, not buyer's remorse; route to technical support instead of denying.
- Customer requests a refund within seconds of activation, arguing they activated by mistake—activation is still confirmed; denial applies, but offer technical support path as an alternative.
- Multiple licenses on the same order where only one was activated—denial applies only to the activated license; the unactivated license may follow standard digital return policy and requires separate evaluation.
- Customer is a business account requesting refund citing procurement error after activation—same denial policy applies; no exceptions for account type, but escalate if the order value or account tier requires senior review.
- Customer contacts support without an order_id—do not apply the denial path until order_id and activation status can be verified.

- `Buyer's remorse on confirmed activated digital license` -> `ineligible`
- `Digital license refund request with reported technical malfunction` -> `needs_escalation`
- `Digital license refund where activation status is unconfirmed` -> `needs_escalation`
- `Non-digital physical product refund request misdirected to this skill` -> `eligible`
- `Chargeback threat on an activated digital license buyer's remorse case` -> `needs_escalation`
- `Final-sale physical item refund denied for buyer's remorse` -> `ineligible`
