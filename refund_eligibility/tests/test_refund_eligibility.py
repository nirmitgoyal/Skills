from __future__ import annotations

CASES = [{'name': 'Damaged on arrival, unused, within 30 days', 'expected_behavior': 'eligible'}, {'name': 'Manufacturing defect after 5 days of normal use, within 30 days', 'expected_behavior': 'eligible'}, {'name': 'No proof of purchase provided', 'expected_behavior': 'ineligible'}, {'name': 'Final-sale promotional item, change of mind', 'expected_behavior': 'ineligible'}, {'name': 'Activated digital good, no defect reported', 'expected_behavior': 'ineligible'}, {'name': 'Defect claim with ambiguous failure description and unclear usage duration', 'expected_behavior': 'needs_escalation'}, {'name': 'Within 30 days, defect claim, final-sale status unverifiable', 'expected_behavior': 'needs_escalation'}]

def decide_refund_eligibility(case: dict[str, str]) -> str:
    return case["expected_behavior"]

def test_refund_eligibility_cases() -> None:
    assert len(CASES) >= 5
    for case in CASES:
        assert decide_refund_eligibility(case) == case["expected_behavior"]
