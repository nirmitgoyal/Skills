# Trust Packet Review

## Summary

Draft review packet for `refund_eligibility`.

## Source Inventory

Approved source bundle hash: `sha256:286b71392b7ef89e5707dc09358df5316dd2c0c6a3559a497d8f6eb5ef61c3c0`

## Policy Claims

- claim_1_test_001: Eligible when Customer received a skincare kit as a gift, experienced an allergic reaction to a listed ingredient, provides the gift receipt, and the original gifter declines to process the return. Agent locates the order via gift receipt, issues full store credit, captures the ingredient name, and flags it to the product team.
- claim_2_test_002: Eligible when Customer received a skincare kit as a gift, experienced an allergic reaction, cannot produce a gift receipt but provides the gifter's email address. Agent locates the order via email, issues full store credit, records the allergen, and flags to the product team.
- claim_3_test_003: Ineligible when Customer received a product as a gift and wants to return it because they simply do not like it. No health or safety concern is stated. Standard return policy applies: only original purchaser within 30-day window for unused/unopened items. Request is denied; no exception pathway is triggered.
- claim_4_test_004: Escalate when Customer reports an allergic reaction to a gifted skincare product but cannot provide a gift receipt and does not know the gifter's name or email. Health/safety concern is credible but order cannot be located. Agent does not auto-deny; case is escalated to a human agent for manual resolution and the allergen is still flagged to the product team.
- claim_5_test_005: Escalate when Customer reports an allergic reaction to a product received as a gift that was purchased during a Black Friday final-sale event. Gift receipt is available. Final-sale terms are non-overridable by the standard agent workflow, but the health/safety concern creates a policy conflict. Case is escalated to a human agent; allergen is flagged to the product team regardless of outcome.
- claim_6_test_006: Ineligible when Customer is the original purchaser and requests a refund for a product purchased 4 months ago citing quality degradation. No health or safety concern is raised. Request falls outside the 30-day return window; no allergy exception pathway applies. Agent may offer escalation to a quality/defect review team as a separate pathway.
- claim_7_test_007: Eligible when Customer received a food or skincare product as a gift and reports ingredient sensitivity (not a full allergic reaction but a documented health concern). Provides gifter's full name. Agent locates the order, applies the health/safety exception, issues full store credit, captures the ingredient identified, and flags to the product team.

## Required Fields

- order_or_gift_receipt
- gifter_name_or_email
- allergen_or_ingredient_identified

## Edge Cases

- Customer reports allergic reaction but item was a final-sale purchase — policy conflict requires human escalation, not auto-approval or auto-denial.
- Customer provides gifter name but the name returns multiple orders — agent must request additional detail (e.g., approximate purchase date or item name) before issuing store credit.
- Customer describes a severe medical reaction (anaphylaxis, hospitalization) — standard refund approval should still proceed, but a safety incident report must be opened in parallel.
- Gifter is willing to process the return themselves — agent should offer both paths (gifter-initiated return or health/safety exception) and let the customer choose.
- Customer cannot identify the specific allergen but describes a clear reaction — still eligible; capture symptoms and flag to product team even without a named ingredient.
- Item is a perishable or consumable that has been fully used — health/safety exception still applies; do not apply the 'used item' ineligibility rule from standard policy when a health concern is documented.
- Customer is also the original purchaser AND experienced an allergic reaction — no alternative verification needed; process as a standard health/safety return without invoking the gift-receipt pathway.
- test_001: Gift recipient with allergic reaction and gift receipt provided -> pass
- test_002: Gift recipient with allergic reaction and gifter email provided -> pass
- test_003: Non-original purchaser with no health concern — preference return -> pass
- test_004: Gift recipient with allergic reaction but zero alternative verification available -> pass
- test_005: Allergic reaction on final-sale item with gift receipt provided -> pass
- test_006: Original purchaser outside 30-day window with no health concern -> pass
- test_007: Gift recipient with ingredient sensitivity (non-allergic) and gifter name provided -> pass

## Test Results

Generated deterministic pilot tests are included under `tests/`.

## Deterministic Verify Health Concern Obtain Alternative Proof Of Purchase Approve Full Store Credit Or Refund Install/Test Instructions

Runtime profile: `runtimes/deterministic_verify_health_concern_obtain_alternative_proof_of_purchase_approve_full_store_credit_or_refund.md`

Owner: `[redacted-email]`

Install Instructions

Deploy this skill under the refund_eligibility skill slug. Set the three required fields (order_or_gift_receipt, gifter_name_or_email, allergen_or_ingredient_identified) as prompted inputs at session start. Integrate a side-channel trigger to the product safety team that fires whenever allergen_or_ingredient_identified is populated, independent of the refund approval status. Ensure the final-sale flag from the order lookup is surfaced to the agent before auto-approval logic runs so that final-sale conflicts route to human escalation rather than auto-resolve.

Test Instructions

To validate deployment: (1) Submit test_001 using a synthetic gift receipt — confirm store credit is issued and product team flag fires. (2) Submit test_003 with no health concern mentioned — confirm ineligible response and no exception pathway is triggered. (3) Submit test_004 with no verification details — confirm escalation routing fires and no auto-denial is returned. (4) Submit test_005 with a final-sale order number and a gift receipt — confirm escalation fires rather than auto-approval. (5) Verify that allergen flagging fires on all test cases where allergen_or_ingredient_identified is populated, even on ineligible or escalated outcomes.

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
