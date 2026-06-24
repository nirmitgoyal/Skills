# Trust Packet Review

## Summary

Draft review packet for `refund_eligibility`.

## Source Inventory

Approved source bundle hash: `sha256:35ff95d407f302b68342489825afe711e99d78bec35e397b899cf1c2d38edb4e`

## Policy Claims

- claim_1_test_001: Ineligible when Customer purchased a software license (Order #ORD-78234), downloaded and activated it, and now states they do not need it. Activation is confirmed and reason is buyer's remorse. Agent must deny the refund citing digital goods policy disclosed at checkout and offer technical support as an alternative. Evidence: src_slack_c0ba1v2k269_1781262743711859.
- claim_2_test_002: Escalate when Customer purchased and activated a digital license but reports the software is not functioning correctly. Activation is confirmed but reason is product failure, not buyer's remorse. Agent must NOT apply the denial path and must route to technical support instead.
- claim_3_test_003: Escalate when Customer requests a refund on a digital license order but activation_status_confirmed is false or unknown. Agent must not issue a denial without confirmation of activation; must gather or verify activation status before proceeding, escalating for manual verification if system cannot confirm.
- claim_4_test_004: Eligible when Customer requests a refund on a physical product (e.g., headphones sent in wrong color, Order #ORD-31502). product_type_is_digital is false, so this skill does not apply. Agent must not deny under the digital goods policy and must handle via the appropriate physical goods refund path. Evidence: src_slack_c0ba1v2k269_1781262649628429.
- claim_5_test_005: Escalate when Customer has an activated digital license denied for refund but now threatens an immediate chargeback. The base denial stands under digital goods policy, but the chargeback threat triggers escalation to the senior payments team per escalation policy. Evidence pattern: src_slack_c0ba1v2k269_1781262823049209.
- claim_6_test_006: Ineligible when Customer purchased a dress during a Black Friday final sale (Order #ORD-67890) and requests a refund because it does not fit. This is ineligible under the final sale promotional terms disclosed at checkout, not under the digital goods policy. Confirms policy-at-checkout denial pattern is consistent but scoped correctly to non-digital context. Evidence: src_slack_c0ba1v2k269_1781262732047749.

## Required Fields

- order_id
- product_type_is_digital
- activation_status_confirmed

## Edge Cases

- Customer claims they never actually used or activated the license despite the system showing activation_status_confirmed=true—do not override confirmed system data; apply denial and note the discrepancy, escalating if the customer disputes system records.
- Customer activated the license but immediately discovered it is incompatible with their operating system—treat as a potential technical issue, not buyer's remorse; route to technical support instead of denying.
- Customer requests a refund within seconds of activation, arguing they activated by mistake—activation is still confirmed; denial applies, but offer technical support path as an alternative.
- Multiple licenses on the same order where only one was activated—denial applies only to the activated license; the unactivated license may follow standard digital return policy and requires separate evaluation.
- Customer is a business account requesting refund citing procurement error after activation—same denial policy applies; no exceptions for account type, but escalate if the order value or account tier requires senior review.
- Customer contacts support without an order_id—do not apply the denial path until order_id and activation status can be verified.
- test_001: Buyer's remorse on confirmed activated digital license -> pass
- test_002: Digital license refund request with reported technical malfunction -> pass
- test_003: Digital license refund where activation status is unconfirmed -> pass
- test_004: Non-digital physical product refund request misdirected to this skill -> pass
- test_005: Chargeback threat on an activated digital license buyer's remorse case -> pass
- test_006: Final-sale physical item refund denied for buyer's remorse -> pass

## Test Results

Generated deterministic pilot tests are included under `tests/`.

## Only Apply This Denial Path When Activation Is Confirmed If Customer Reports The Product Is Not Functioning Route To Technical Support Instead Of This Skill Install/Test Instructions

Runtime profile: `runtimes/only_apply_this_denial_path_when_activation_is_confirmed_if_customer_reports_the_product_is_not_functioning_route_to_technical_support_instead_of_this_skill.md`

Owner: `[redacted-email]`

Install Instructions

Deploy under the refund_eligibility skill namespace. Set required_inputs to [order_id, product_type_is_digital, activation_status_confirmed]. Gate execution on product_type_is_digital=true AND activation_status_confirmed=true before invoking the ineligible denial branch. Wire the technical-malfunction branch to the technical support routing skill. Ensure the digital goods policy disclosure text is injected from the policy content store at runtime so the denial citation remains accurate if policy language changes. Log all denial decisions with order_id and activation confirmation source for audit.

Test Instructions

1. Submit a request with product_type_is_digital=true, activation_status_confirmed=true, reason=buyer_remorse and assert the response contains a refund denial citing digital goods policy and an offer of technical support (test_001). 2. Submit with activation_status_confirmed=true but reason=product_not_functioning and assert the response routes to technical support without a denial (test_002). 3. Submit with activation_status_confirmed=false and assert the response does not issue a denial and instead seeks confirmation or escalates (test_003). 4. Submit with product_type_is_digital=false and assert this skill exits without applying the digital goods denial (test_004). 5. Submit a buyer's remorse denial scenario followed by a chargeback threat message and assert the response includes escalation to senior payments team (test_005). 6. Verify tone checks: denial responses must not be accusatory and must include an empathetic acknowledgment before citing policy.

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
