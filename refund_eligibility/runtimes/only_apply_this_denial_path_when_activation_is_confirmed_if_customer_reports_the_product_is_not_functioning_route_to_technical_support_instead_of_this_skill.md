# Only Apply This Denial Path When Activation Is Confirmed If Customer Reports The Product Is Not Functioning Route To Technical Support Instead Of This Skill Runtime Profile

## Guidance

Always retrieve and verify order_id before applying any refund determination.

Check product_type_is_digital first; if false, exit this skill and route to the appropriate physical goods flow.

Check activation_status_confirmed; if not confirmed, do not issue denial—ask customer or verify via system before proceeding.

When issuing the denial, explicitly cite 'digital goods policy disclosed at checkout' as the basis—do not generalize to a vague 'no refund policy.'

Immediately follow the denial with a genuine, specific offer to assist with any technical issues—do not treat it as a throwaway line.

Do not apply this denial if the customer's stated reason is product malfunction or incompatibility—route to technical support.

Do not escalate to payments team solely because the customer is disappointed with the denial; escalate only if a chargeback threat, fraud indicator, or unresolved payment dispute is present.

Maintain an empathetic and non-accusatory tone when delivering the denial; acknowledge the customer's frustration before citing policy.

## Install Instructions

Deploy under the refund_eligibility skill namespace. Set required_inputs to [order_id, product_type_is_digital, activation_status_confirmed]. Gate execution on product_type_is_digital=true AND activation_status_confirmed=true before invoking the ineligible denial branch. Wire the technical-malfunction branch to the technical support routing skill. Ensure the digital goods policy disclosure text is injected from the policy content store at runtime so the denial citation remains accurate if policy language changes. Log all denial decisions with order_id and activation confirmation source for audit.

## Test Instructions

1. Submit a request with product_type_is_digital=true, activation_status_confirmed=true, reason=buyer_remorse and assert the response contains a refund denial citing digital goods policy and an offer of technical support (test_001). 2. Submit with activation_status_confirmed=true but reason=product_not_functioning and assert the response routes to technical support without a denial (test_002). 3. Submit with activation_status_confirmed=false and assert the response does not issue a denial and instead seeks confirmation or escalates (test_003). 4. Submit with product_type_is_digital=false and assert this skill exits without applying the digital goods denial (test_004). 5. Submit a buyer's remorse denial scenario followed by a chargeback threat message and assert the response includes escalation to senior payments team (test_005). 6. Verify tone checks: denial responses must not be accusatory and must include an empathetic acknowledgment before citing policy.
