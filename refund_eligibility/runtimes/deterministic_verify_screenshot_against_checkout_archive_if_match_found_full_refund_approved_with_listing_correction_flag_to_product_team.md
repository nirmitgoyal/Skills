# Deterministic Verify Screenshot Against Checkout Archive If Match Found Full Refund Approved With Listing Correction Flag To Product Team Runtime Profile

## Guidance

Step 1 — Collect required fields: Greet the customer and confirm you have order_id, charged_amount, order_timestamp, and destination_country before proceeding.

Step 2 — Request screenshot: If the customer has not attached a screenshot of the 'duties included' messaging, ask for it explicitly and hold the case open. Do not deny or approve without it, unless the archive alone is definitive.

Step 3 — Archive lookup: Query the checkout archive using the order_id and order_timestamp to retrieve the exact messaging displayed to this customer at time of purchase for their SKU and destination country.

Step 4 — Compare: If the archive record and screenshot both confirm a 'duties included' or equivalent promise, proceed to full refund approval. If only one source confirms it and they do not conflict, use judgment per decision rules.

Step 5 — Approve or escalate: Approve the full charged_amount refund if match is confirmed. Escalate per escalation_notes rules if the archive is missing, the screenshot is suspicious, the amount exceeds $200, or a chargeback is mentioned.

Step 6 — Flag listing: On every approved refund, raise a listing-correction flag to the product team with the SKU, destination country, and order_timestamp so the messaging can be reviewed and corrected.

Step 7 — Communicate outcome: Inform the customer of the refund amount and expected processing timeline. Reference the promise they saw as validation of their concern (see tone in src_slack_c0ba1v2k269_1781262809670129: 'You're absolutely right to flag this').

Never approve a refund based solely on the customer's verbal claim with no corroborating evidence from either a screenshot or the checkout archive.

Never deny a refund solely because the listing has already been corrected — what matters is the messaging active at the customer's order_timestamp.

## Install Instructions

1. Deploy this skill under the slug 'refund_eligibility' in the agent routing layer. 2. Connect the checkout_archive_lookup tool to the archive database, scoped to read-only access on the checkout messaging history table, indexed by SKU, destination_country, and order_timestamp. 3. Connect the refund_issuance tool with write permissions limited to the charged_amount field; cap single-agent approval at $200 and require manager_approval_token for amounts above. 4. Connect the listing_correction_flag tool with write access to the product team's issue tracker; ensure flags include SKU, destination_country, and order_timestamp fields. 5. Configure the escalation routing rule to forward cases tagged NEEDS_ESCALATION to the senior_payments_queue with all collected evidence attached. 6. Set case-hold timeout to 72 hours for screenshot-pending cases; auto-close with denial notice if no screenshot is received within that window. 7. Enable audit logging on all archive lookups and refund approvals for compliance traceability.

## Test Instructions

1. Seed the checkout archive with a test record for SKU 'TEST-SKU-001', destination 'CA', date '2024-06-15', messaging 'Duties Included'. 2. Run test_001: submit order_id='ORD-TEST-001', charged_amount=45, order_timestamp='2024-06-15T10:00:00Z', destination_country='CA', with a matching screenshot; confirm the system returns an eligible decision, issues a $45 refund, and creates a listing-correction flag. 3. Run test_002: submit the same order details with no screenshot and no archive record; confirm the system returns an ineligible decision with no refund action taken. 4. Run test_003: submit an order_timestamp falling in a date range where the archive has a known data gap; confirm the system routes to the senior_payments_queue escalation path. 5. Run test_004: include the phrase 'I am filing a chargeback' in the customer message; confirm the system immediately escalates regardless of screenshot or archive status. 6. Run test_007: set charged_amount=230 with a confirmed archive match; confirm the system blocks self-approval and requires a manager_approval_token before the refund is issued. 7. After each eligible test, verify the listing_correction_flag tool was called exactly once with the correct SKU, destination_country, and order_timestamp. 8. Verify that no test produces a refund without a corresponding audit log entry.
