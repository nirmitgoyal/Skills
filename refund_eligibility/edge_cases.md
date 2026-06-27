# Edge Cases

- Customer claims the promotional terms were buried or not clearly visible at checkout — treat as a disclosure dispute and escalate rather than auto-deny.
- Item purchased as a gift during a final-sale event where the gift recipient (not the purchaser) is requesting the refund — order_id lookup must still confirm original promotional flags; same ineligible outcome if confirmed, but agent should handle sensitivity around gift context.
- Order partially contains final-sale promotional items and partially contains non-promotional items — apply ineligibility only to the confirmed final-sale line items; process eligible items under standard policy.
- Customer purchased during a promotional event that was not explicitly designated as 'final sale' (e.g., a discount code with no final-sale disclosure) — absence of promotional_terms_disclosure_record means final-sale policy does not apply; handle under standard return policy.
- Customer attempts to return a final-sale item for exchange rather than refund — policy denies returns categorically (non-returnable), so exchanges are also disallowed; agent must not offer exchange as a workaround.
- Subscription renewal auto-charge scenario intersecting with a promotional signup rate — treat under subscription refund logic (cf. src_slack_c0ba1v2k269_1781262784193319), not final-sale policy.

- `Confirmed Final-Sale Order — Fit Complaint` -> `ineligible`
- `Confirmed Final-Sale Order — Defect Claim` -> `ineligible`
- `Non-Promotional Order — Standard Return Window Active` -> `eligible`
- `Final-Sale Flag Present but Disclosure Record Missing` -> `needs_escalation`
- `Customer Disputes Checkout Disclosure — Claims Final-Sale Terms Not Shown` -> `needs_escalation`
- `Order ID Unresolvable` -> `needs_escalation`
- `Confirmed Final-Sale Order — Personal Hardship Plea` -> `ineligible`
