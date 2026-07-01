# Trust Packet Review

## Summary

Draft review packet for `refund_eligibility`.

## Source Inventory

Approved source bundle hash: `sha256:d8401dda43f3be7d403843340d8ed9f0be8c2b1705b5cc38d2be9c6ff45ea79e`

## Policy Claims

- claim_1_test_001: Eligible when Customer submits Order #ORD-88123, $45 customs charge, destination Canada, with a screenshot showing 'duties included' at checkout. Archive record for that SKU and region on the order date confirms the same messaging. Agent verifies match and issues full $45 refund, flags listing to product team. Directly backed by src_slack_c0ba1v2k269_1781262809670129.
- claim_2_test_002: Ineligible when Customer claims duties were promised but provides no screenshot. Checkout archive contains no 'duties included' messaging for the relevant SKU, destination, and order date. No basis to approve refund; agent closes with explanation and instructs customer that proof is required.
- claim_3_test_003: Escalate when Customer provides a screenshot appearing to show 'duties included'. However, the checkout archive has a data gap for the relevant date range and the record cannot be confirmed or denied. Agent cannot make a deterministic decision and must escalate to senior agent with all collected evidence within 4 business hours.
- claim_4_test_004: Escalate when Customer reports $78 customs charge and states they are filing a chargeback today if not resolved immediately. Even if a screenshot is available, the chargeback threat triggers immediate escalation to senior payments team per the urgency protocol established in src_slack_c0ba1v2k269_1781262823049209. Regular refund approval flow is suspended pending escalation outcome.
- claim_5_test_005: Ineligible when Customer submits a screenshot of checkout messaging reading 'Free Shipping on this order' with no reference to duties or customs. The messaging does not constitute a promise to cover duties. Refund is denied; agent explains the distinction between shipping cost coverage and duties coverage.
- claim_6_test_006: Ineligible when Customer claims duties were promised. Archive confirms the listing carried 'duties included' language historically, but a product team correction log shows the messaging was removed two days before the customer's order timestamp. The promise was not active at time of purchase. Refund is denied and agent explains the timeline.
- claim_7_test_007: Escalate when Customer reports $230 customs charge on a bulk order. Screenshot and archive both confirm 'duties included' messaging. Because the amount exceeds the $200 threshold, the agent cannot self-approve and must escalate to a manager. Case is held open pending manager authorization before refund is issued.

## Required Fields

- order_id
- charged_amount
- customer_screenshot_of_checkout_messaging
- order_timestamp
- destination_country

## Edge Cases

- Customer submits a screenshot but it is cropped or low-resolution — request a clearer image before proceeding; do not deny outright.
- The checkout archive itself is ambiguous (e.g., A/B test variant shown to some customers) — escalate for product team to confirm which variant was served to this customer's session.
- Customer was charged duties by their national customs authority rather than by the merchant — clarify that a refund covers only merchant-controlled duties fees; third-party government fees may not be refundable and require escalation.
- Multiple orders with duties charges from the same customer in a short period — flag for pattern review to trust-and-safety before approving any individual refund.
- Customer already received a partial refund for the same duties charge from a previous interaction — deduct prior refunded amount from the approved refund to avoid double-payment.
- Destination country charges are split between duties and VAT/GST — only the duties portion covered by 'duties included' promise is refundable; tax components are handled separately.
- test_001: Matching screenshot and archive — full refund approved -> pass
- test_002: No screenshot and no archive record — ineligible -> pass
- test_003: Screenshot provided but archive record cannot be located — escalation required -> pass
- test_004: Chargeback threat with pending duties dispute — immediate escalation -> pass
- test_005: Screenshot shows generic free shipping, not duties coverage — ineligible -> pass
- test_006: Archive confirms duties promise; listing was corrected before order date — ineligible -> pass
- test_007: Screenshot matches archive, duties amount over $200 — escalation for manager approval -> pass

## Test Results

Generated deterministic pilot tests are included under `tests/`.

## Deterministic Verify Screenshot Against Checkout Archive If Match Found Full Refund Approved With Listing Correction Flag To Product Team Install/Test Instructions

Runtime profile: `runtimes/deterministic_verify_screenshot_against_checkout_archive_if_match_found_full_refund_approved_with_listing_correction_flag_to_product_team.md`

Owner: `[redacted-email]`

Install Instructions

1. Deploy this skill under the slug 'refund_eligibility' in the agent routing layer. 2. Connect the checkout_archive_lookup tool to the archive database, scoped to read-only access on the checkout messaging history table, indexed by SKU, destination_country, and order_timestamp. 3. Connect the refund_issuance tool with write permissions limited to the charged_amount field; cap single-agent approval at $200 and require manager_approval_token for amounts above. 4. Connect the listing_correction_flag tool with write access to the product team's issue tracker; ensure flags include SKU, destination_country, and order_timestamp fields. 5. Configure the escalation routing rule to forward cases tagged NEEDS_ESCALATION to the senior_payments_queue with all collected evidence attached. 6. Set case-hold timeout to 72 hours for screenshot-pending cases; auto-close with denial notice if no screenshot is received within that window. 7. Enable audit logging on all archive lookups and refund approvals for compliance traceability.

Test Instructions

1. Seed the checkout archive with a test record for SKU 'TEST-SKU-001', destination 'CA', date '2024-06-15', messaging 'Duties Included'. 2. Run test_001: submit order_id='ORD-TEST-001', charged_amount=45, order_timestamp='2024-06-15T10:00:00Z', destination_country='CA', with a matching screenshot; confirm the system returns an eligible decision, issues a $45 refund, and creates a listing-correction flag. 3. Run test_002: submit the same order details with no screenshot and no archive record; confirm the system returns an ineligible decision with no refund action taken. 4. Run test_003: submit an order_timestamp falling in a date range where the archive has a known data gap; confirm the system routes to the senior_payments_queue escalation path. 5. Run test_004: include the phrase 'I am filing a chargeback' in the customer message; confirm the system immediately escalates regardless of screenshot or archive status. 6. Run test_007: set charged_amount=230 with a confirmed archive match; confirm the system blocks self-approval and requires a manager_approval_token before the refund is issued. 7. After each eligible test, verify the listing_correction_flag tool was called exactly once with the correct SKU, destination_country, and order_timestamp. 8. Verify that no test produces a refund without a corresponding audit log entry.

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
