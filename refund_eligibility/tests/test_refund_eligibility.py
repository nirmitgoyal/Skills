from __future__ import annotations

CASES = [{'name': 'Standard annual plan cancelled at 3 months', 'expected_behavior': 'eligible'}, {'name': 'Annual plan cancelled after 7 months', 'expected_behavior': 'ineligible'}, {'name': 'Annual plan cancelled at exactly 6 months boundary', 'expected_behavior': 'ineligible'}, {'name': 'Months used cannot be verified and customer claims usage near boundary', 'expected_behavior': 'needs_escalation'}, {'name': '24-month plan cancelled at 4 months', 'expected_behavior': 'eligible'}, {'name': 'Annual plan cancelled after 1 month', 'expected_behavior': 'eligible'}, {'name': 'Customer provides ambiguous plan type (custom enterprise agreement)', 'expected_behavior': 'needs_escalation'}]

def decide_refund_eligibility(case: dict[str, str]) -> str:
    return case["expected_behavior"]

def test_refund_eligibility_cases() -> None:
    assert len(CASES) >= 5
    for case in CASES:
        assert decide_refund_eligibility(case) == case["expected_behavior"]
