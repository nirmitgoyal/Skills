# refund_eligibility

When a customer requests a refund on a digital license that has already been downloaded and activated, deny the refund by citing the digital goods policy disclosed at checkout, then offer technical support as an alternative resolution path. This denial path applies exclusively to confirmed activation cases with buyer's remorse; non-functioning products must be routed to technical support instead.

## Decision Rules

- Confirm order_id is present and retrievable before proceeding.
- Confirm product_type_is_digital is true; if not digital, this skill does not apply.
- Confirm activation_status_confirmed is true; if activation is unconfirmed, do not deny—gather confirmation first.
- If activation is confirmed and the reason is buyer's remorse, deny the refund citing the digital goods policy disclosed at checkout.
- If the customer reports a technical malfunction or product not functioning, do NOT apply this denial path—route to technical support instead.
- Do not make exceptions to the digital goods no-refund policy for buyer's remorse regardless of time elapsed since purchase.
- After denial, always offer to assist with any technical issues as an alternative path.
- Do not escalate to payments or senior teams solely for a buyer's remorse denial on an activated digital license.

## Required Fields

- order_id
- product_type_is_digital
- activation_status_confirmed

## Escalation

- If the customer reports the product is not functioning correctly after activation, escalate or route to technical support—do not apply the refund denial.
- If the customer threatens a chargeback or has an unresolved payment dispute unrelated to activation status, escalate to the senior payments team per standard escalation policy.
- If activation status cannot be confirmed by the system, escalate for manual verification before issuing any denial.
- If the customer presents evidence of unauthorized purchase or fraud, escalate immediately rather than applying this skill.
