# Trust Packet Review

## Summary

Draft review packet for `refund_eligibility`.

## Source Inventory

Approved source bundle hash: `sha256:0472a7b0bc5984aa318e75939b753ac9d3ef36fd4afad5be1f64906aea049730`

## Policy Claims

- claim_1_test_001: Ineligible when Customer submits Order #ORD-67890 purchased during Black Friday. System lookup confirms promotional_event_flag = BLACK_FRIDAY_FINAL_SALE and promotional_terms_disclosure_record = present. Customer reason is poor fit. Expected: categorical denial, no exceptions, optional forward-looking sizing offer. Directly evidenced by src_slack_c0ba1v2k269_1781262732047749.
- claim_2_test_002: Ineligible when Customer submits a final-sale order with promotional_event_flag confirmed and promotional_terms_disclosure_record on file, but claims item arrived defective. Expected: refund request denied as ineligible under final-sale policy; agent may separately note quality-team escalation as a distinct non-refund track but cannot use defect as a refund exception. Synthesized from RULE-2 and defect-escalation precedent in src_slack_c0ba1v2k269_1781262697508679.
- claim_3_test_003: Eligible when Customer submits an order with no promotional_event_flag and purchase date within 30 days, item unused and unopened. Expected: eligible for standard return/refund processing. This establishes the baseline non-final-sale eligible path, grounded in standard 30-day window policy evidenced across multiple source excerpts.
- claim_4_test_004: Escalate when Customer submits order with promotional_event_flag = BLACK_FRIDAY_FINAL_SALE but promotional_terms_disclosure_record is absent from system. Expected: cannot auto-deny; escalate to human review to verify whether disclosure was actually presented at checkout. Grounded in RULE-4 and false-advertising escalation precedent in src_slack_c0ba1v2k269_1781262809670129.
- claim_5_test_005: Escalate when Customer acknowledges purchasing during a promotional event but asserts final-sale terms were never displayed at checkout, characterizing the situation as a disclosure failure. Expected: immediate escalation to human review; agent must not override the customer's disclosure dispute with an automated denial. Grounded in false-advertising/disclosure escalation precedent in src_slack_c0ba1v2k269_1781262809670129 and RULE-7.
- claim_6_test_006: Escalate when Customer provides an order_id that cannot be found in the order management system. Neither promotional_event_flag nor promotional_terms_disclosure_record can be retrieved. Expected: escalate to human review; do not assume ineligibility in the absence of confirmed metadata. Grounded in RULE-3.
- claim_7_test_007: Ineligible when Customer cites financial hardship or personal circumstances as grounds for an exception to the final-sale policy. System confirms promotional_event_flag and promotional_terms_disclosure_record. Expected: denial stands; policy is categorical and personal circumstances are explicitly excluded as exception grounds per the policy summary and RULE-1.

## Required Fields

- order_id
- promotion_flag_at_checkout
- promotional_terms_disclosure_record

## Edge Cases

- Customer claims the promotional terms were buried or not clearly visible at checkout — treat as a disclosure dispute and escalate rather than auto-deny.
- Item purchased as a gift during a final-sale event where the gift recipient (not the purchaser) is requesting the refund — order_id lookup must still confirm original promotional flags; same ineligible outcome if confirmed, but agent should handle sensitivity around gift context.
- Order partially contains final-sale promotional items and partially contains non-promotional items — apply ineligibility only to the confirmed final-sale line items; process eligible items under standard policy.
- Customer purchased during a promotional event that was not explicitly designated as 'final sale' (e.g., a discount code with no final-sale disclosure) — absence of promotional_terms_disclosure_record means final-sale policy does not apply; handle under standard return policy.
- Customer attempts to return a final-sale item for exchange rather than refund — policy denies returns categorically (non-returnable), so exchanges are also disallowed; agent must not offer exchange as a workaround.
- Subscription renewal auto-charge scenario intersecting with a promotional signup rate — treat under subscription refund logic (cf. src_slack_c0ba1v2k269_1781262784193319), not final-sale policy.
- TEST-001: Confirmed Final-Sale Order — Fit Complaint -> pass
- TEST-002: Confirmed Final-Sale Order — Defect Claim -> pass
- TEST-003: Non-Promotional Order — Standard Return Window Active -> pass
- TEST-004: Final-Sale Flag Present but Disclosure Record Missing -> pass
- TEST-005: Customer Disputes Checkout Disclosure — Claims Final-Sale Terms Not Shown -> pass
- TEST-006: Order ID Unresolvable -> pass
- TEST-007: Confirmed Final-Sale Order — Personal Hardship Plea -> pass

## Test Results

Generated deterministic pilot tests are included under `tests/`.

## Deterministic Lookup Check Order Metadata For Promotional Event Flag And Associated Non Refund Disclosure Install/Test Instructions

Runtime profile: `runtimes/deterministic_lookup_check_order_metadata_for_promotional_event_flag_and_associated_non_refund_disclosure.md`

Owner: `[redacted-email]`

Install Instructions

Deploy this skill under the refund_eligibility skill slot. Configure the runtime to perform an order metadata lookup using the provided order_id against the order management system, retrieving the promotional_event_flag and promotional_terms_disclosure_record fields. Both fields must return affirmative values to trigger the ineligible determination. If either field is null, missing, or disputed by the customer, the skill must route to the needs_escalation path. Ensure the skill has read-only access to order metadata and does not require write permissions for denial logging — logging should be handled by the calling orchestration layer. Link the escalation path to the human-review queue with case context pre-populated (order_id, flag status, disclosure status, and customer claim summary).

Test Instructions

To validate this skill in a staging environment: (1) Seed a test order with promotional_event_flag = BLACK_FRIDAY_FINAL_SALE and a valid promotional_terms_disclosure_record — submit a refund request and confirm ineligible response is returned with no exception paths offered. (2) Seed a test order with promotional_event_flag present but promotional_terms_disclosure_record null — submit a refund request and confirm needs_escalation is triggered. (3) Seed a test order with no promotional_event_flag — submit a refund request and confirm the skill routes to standard refund policy rather than applying final-sale denial. (4) Simulate a customer message asserting checkout disclosure was not shown — confirm needs_escalation is triggered even when both flags are technically present in metadata. (5) Confirm that no test path results in a partial refund or store credit offer being generated by the skill itself.

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
