# Deterministic Verify Health Concern Obtain Alternative Proof Of Purchase Approve Full Store Credit Or Refund Runtime Profile

## Guidance

Step 1: Confirm whether the customer is the original purchaser or a gift recipient.

Step 2: Ask whether the concern is health/safety related (allergic reaction or ingredient sensitivity); if yes, activate this exception pathway.

Step 3: Request alternative verification in priority order: (a) gift receipt first, (b) gifter name or email if no receipt is available.

Step 4: Locate the order using the provided verification; if order cannot be found, escalate — do not auto-deny.

Step 5: Capture the specific allergen or ingredient identified; if the customer cannot name it, capture described symptoms.

Step 6: Approve full store credit (or full refund if order is fully verified) without requiring the original purchaser to act.

Step 7: Regardless of refund outcome, flag the allergen/ingredient information to the product team as a mandatory parallel action.

Step 8: Check whether the item was part of a final-sale promotion before approving — if so, escalate rather than self-approve.

Do not apply the standard 'unused/unopened within 30 days' rule when a health/safety concern is documented and alternative verification is present.

Do not apply the 'original purchaser only' rule when the health/safety exception pathway is active.

Always confirm the resolution (store credit amount or refund amount) to the customer in writing before closing the interaction.

## Install Instructions

Deploy this skill under the refund_eligibility skill slug. Set the three required fields (order_or_gift_receipt, gifter_name_or_email, allergen_or_ingredient_identified) as prompted inputs at session start. Integrate a side-channel trigger to the product safety team that fires whenever allergen_or_ingredient_identified is populated, independent of the refund approval status. Ensure the final-sale flag from the order lookup is surfaced to the agent before auto-approval logic runs so that final-sale conflicts route to human escalation rather than auto-resolve.

## Test Instructions

To validate deployment: (1) Submit test_001 using a synthetic gift receipt — confirm store credit is issued and product team flag fires. (2) Submit test_003 with no health concern mentioned — confirm ineligible response and no exception pathway is triggered. (3) Submit test_004 with no verification details — confirm escalation routing fires and no auto-denial is returned. (4) Submit test_005 with a final-sale order number and a gift receipt — confirm escalation fires rather than auto-approval. (5) Verify that allergen flagging fires on all test cases where allergen_or_ingredient_identified is populated, even on ineligible or escalated outcomes.
