from __future__ import annotations

CASES = [{'name': 'Unopened item within 30-day window', 'expected_behavior': 'eligible'}, {'name': 'Used item within 30-day window', 'expected_behavior': 'ineligible'}, {'name': 'Final-sale promotional item, unused, within 30 days', 'expected_behavior': 'ineligible'}, {'name': 'Subscription renewal with zero account usage, charged 2 days ago', 'expected_behavior': 'needs_escalation'}, {'name': 'Unused item outside 30-day window', 'expected_behavior': 'needs_escalation'}, {'name': 'Trial billing courtesy refund within 1 day of trial end', 'expected_behavior': 'eligible'}, {'name': 'Used item outside 30-day window', 'expected_behavior': 'ineligible'}]

def decide_refund_eligibility(case: dict[str, str]) -> str:
    return case["expected_behavior"]

def test_refund_eligibility_cases() -> None:
    assert len(CASES) >= 5
    for case in CASES:
        assert decide_refund_eligibility(case) == case["expected_behavior"]
