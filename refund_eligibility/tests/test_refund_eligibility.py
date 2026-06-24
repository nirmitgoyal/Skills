from __future__ import annotations

CASES = [{'name': "Buyer's remorse on confirmed activated digital license", 'expected_behavior': 'ineligible'}, {'name': 'Digital license refund request with reported technical malfunction', 'expected_behavior': 'needs_escalation'}, {'name': 'Digital license refund where activation status is unconfirmed', 'expected_behavior': 'needs_escalation'}, {'name': 'Non-digital physical product refund request misdirected to this skill', 'expected_behavior': 'eligible'}, {'name': "Chargeback threat on an activated digital license buyer's remorse case", 'expected_behavior': 'needs_escalation'}, {'name': "Final-sale physical item refund denied for buyer's remorse", 'expected_behavior': 'ineligible'}]

def decide_refund_eligibility(case: dict[str, str]) -> str:
    return case["expected_behavior"]

def test_refund_eligibility_cases() -> None:
    assert len(CASES) >= 5
    for case in CASES:
        assert decide_refund_eligibility(case) == case["expected_behavior"]
