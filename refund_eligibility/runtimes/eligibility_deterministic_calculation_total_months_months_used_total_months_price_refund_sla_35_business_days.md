# Eligibility Deterministic Calculation Total Months Months Used Total Months Price Refund Sla 35 Business Days Runtime Profile

## Guidance

Step 1 — Collect all required fields: subscription_plan_type, annual_or_period_price, months_used, total_plan_months.

Step 2 — Confirm the plan qualifies as annual or long-term; if not, redirect or escalate.

Step 3 — Check eligibility gate: if months_used >= 6, respond as ineligible and do not calculate a refund.

Step 4 — If months_used < 6, calculate refund = (total_months - months_used) / total_months × annual_or_period_price. Round to two decimal places.

Step 5 — Present the calculated refund amount clearly to the customer and confirm: (a) access ends immediately upon cancellation, (b) refund will be processed within 35 business days.

Step 6 — Obtain explicit customer confirmation before processing the cancellation.

Step 7 — After confirmation, initiate cancellation and log the refund request with the calculated amount and SLA date.

Step 8 — If any required field is missing, ambiguous, or disputed, pause and escalate rather than proceeding with an unverified calculation.

## Install Instructions

Deploy under skill slug 'refund_eligibility'. Attach to cancellation intents for annual and long-term subscription plan types. Ensure the runtime has read access to the customer's subscription record (plan type, start date, price paid, total term months) to auto-populate months_used and plan_price where possible, reducing manual entry errors. Gate this skill so it does not fire for month-to-month plans or one-time digital license purchases.

## Test Instructions

Run all seven deterministic tests in the test suite before promoting to production. Verify that: (1) the eligibility gate correctly blocks months_used >= 6 as ineligible; (2) the refund formula produces the correct two-decimal-place value for each eligible test; (3) needs_escalation paths halt calculation and surface an escalation prompt; (4) the 35-business-day SLA and immediate access termination disclosures appear in every eligible response; (5) no refund figure is presented to the customer before explicit confirmation is solicited.
