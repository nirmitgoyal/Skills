# refund_eligibility

Allow non-original purchasers to receive store credit or a full refund when a documented health or safety concern (e.g., allergic reaction, ingredient sensitivity) is present, bypassing the standard proof-of-purchase requirement. Accept a gift receipt OR the gifter's name/email as alternative order-location verification. Capture the specific allergen or ingredient identified and flag it to the product team. This pathway is explicitly supported for gift recipients who cannot obtain a return from the original purchaser.

## Decision Rules

- ELIGIBLE if: customer is a non-original purchaser AND reports a health/safety concern (allergic reaction or ingredient sensitivity) AND provides at least one of: (a) gift receipt, or (b) gifter name or gifter email sufficient to locate the order.
- ELIGIBLE outcome is full store credit for the item value; a full refund may be issued if order can be fully located and verified.
- INELIGIBLE if: no health or safety concern is stated — standard return policy applies (unused/unopened within 30 days, original purchaser only).
- INELIGIBLE if: item was purchased under a final-sale or promotional event — final-sale terms are non-overridable even under this pathway.
- INELIGIBLE if: customer cannot provide any alternative verification (neither gift receipt nor gifter name/email) — escalate rather than deny outright.
- INELIGIBLE if: the return window concern is purely preference-based (dislike of product, fit, or performance) with no health/safety claim.
- Always capture the specific allergen or ingredient identified and flag it internally to the product team regardless of refund outcome.
- Do not require the original purchaser to initiate the return when a valid health/safety concern and alternative verification are both present.

## Required Fields

- order_or_gift_receipt
- gifter_name_or_email
- allergen_or_ingredient_identified

## Escalation

- Escalate to product/safety team whenever an allergen or ingredient is identified, even if the refund is approved — this is a mandatory parallel action.
- Escalate to a human agent if no alternative verification (gift receipt or gifter name/email) can be obtained but health/safety concern is credible — do not auto-deny.
- Escalate if the item in question was part of a final-sale promotion and a health/safety concern is raised — policy conflict requires human review.
- Escalate if the customer describes a severe reaction (e.g., anaphylaxis, medical treatment required) — may require safety incident documentation beyond standard refund workflow.
