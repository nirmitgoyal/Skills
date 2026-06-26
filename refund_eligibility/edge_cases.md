# Edge Cases

- Annual or multi-year renewal charges are not covered by this trial courtesy refund policy even if the customer has been non-active; escalate per src_slack_c0ba1v2k269_1781262784193319.
- Charge that falls exactly at the 24-hour boundary (e.g., charge timestamp equals trial_end_date + 24:00:00) should be treated as eligible, but document precisely for audit trail.
- Customer who cancelled during the trial but was still charged due to a billing system error is a separate billing dispute, not a courtesy refund scenario; escalate to payments team.
- If the customer's account is already on the free plan (subscription already inactive) when they contact support, verify whether the refund was already processed before re-issuing.
- Customers with multiple trial subscriptions across different plans in the same billing cycle may have ambiguous trial_end_date records; escalate to avoid duplicate refunds.
- Delayed return refund issues (as in src_slack_c0ba1v2k269_1781262796239039) are entirely out of scope for this skill and should be routed to the payments team.

- `Charge exactly 1 day (within 24 hours) after trial end — standard eligible case` -> `eligible`
- `Charge 48 hours after trial end — outside 24-hour window` -> `ineligible`
- `Annual renewal charge with zero account usage — not a trial conversion` -> `needs_escalation`
- `Customer has already received a prior courtesy refund on same account` -> `ineligible`
- `Customer-stated trial end date conflicts with system records — unverifiable window` -> `needs_escalation`
- `Charge within 24 hours but charge_amount does not match plan pricing on record` -> `needs_escalation`
