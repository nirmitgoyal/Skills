# Verify Trial End Date In System Confirm Charge Occurred Within 24 Hours Post Trial Runtime Profile

## Guidance

Always retrieve trial_end_date and charge_date from system records; never rely solely on customer-stated dates.

Compute the window as: (charge_date − trial_end_date) ≤ 24 hours. If true and no prior courtesy refund exists, proceed with full refund.

State the exact refund amount equal to charge_amount when confirming with the customer before processing.

Explicitly cancel the subscription and confirm account reversion to free plan as part of the same interaction.

Communicate the 3–5 business day refund timeline to the customer at the point of confirmation.

Log the courtesy refund in the system so future agents can identify repeat requests on the same account.

If any required field (trial_end_date, charge_date, charge_amount, subscription_plan_name) is missing or unverifiable, pause and escalate rather than proceeding on assumptions.

Do not apply this policy to annual renewals, mid-cycle upgrades, or any charge type other than the initial post-trial conversion charge.

## Install Instructions

Register this skill under the 'refund_eligibility' skill slug. Ensure the runtime has read access to subscription billing records including trial_end_date, charge_date, charge_amount, subscription_plan_name, and prior courtesy refund history. Grant write access to initiate refunds, cancel subscriptions, and update account plan status. Configure escalation routing to the billing manager queue for out-of-window or ambiguous cases. Set the one-time courtesy refund flag as a checkable account attribute to prevent duplicate issuance.

## Test Instructions

To validate this skill in a staging environment: (1) Seed a test account with trial_end_date = T and charge_date = T+20 hours; invoke skill and assert full refund issued, subscription cancelled, free plan restored. (2) Seed a second account with charge_date = T+30 hours; invoke and assert escalation path triggered, no refund issued. (3) Seed a third account with a prior courtesy refund flag set and charge_date = T+10 hours; invoke and assert ineligible response with escalation. (4) Seed an annual renewal scenario (no trial record); invoke and assert needs_escalation output matching manager-approval flow. (5) Seed an account with missing trial_end_date in system; invoke and assert escalation triggered before any refund action. Confirm all refund amounts in passing tests equal the seeded charge_amount exactly.
