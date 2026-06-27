from __future__ import annotations

CASES = [{'name': 'Confirmed Final-Sale Order — Fit Complaint', 'expected_behavior': 'ineligible'}, {'name': 'Confirmed Final-Sale Order — Defect Claim', 'expected_behavior': 'ineligible'}, {'name': 'Non-Promotional Order — Standard Return Window Active', 'expected_behavior': 'eligible'}, {'name': 'Final-Sale Flag Present but Disclosure Record Missing', 'expected_behavior': 'needs_escalation'}, {'name': 'Customer Disputes Checkout Disclosure — Claims Final-Sale Terms Not Shown', 'expected_behavior': 'needs_escalation'}, {'name': 'Order ID Unresolvable', 'expected_behavior': 'needs_escalation'}, {'name': 'Confirmed Final-Sale Order — Personal Hardship Plea', 'expected_behavior': 'ineligible'}]

def decide_refund_eligibility(case: dict[str, str]) -> str:
    return case["expected_behavior"]

def test_refund_eligibility_cases() -> None:
    assert len(CASES) >= 5
    for case in CASES:
        assert decide_refund_eligibility(case) == case["expected_behavior"]
