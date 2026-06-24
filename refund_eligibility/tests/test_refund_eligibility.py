from __future__ import annotations

CASES = [{'name': 'Classic wrong color variant — eligible for refund or exchange', 'expected_behavior': 'eligible'}, {'name': 'Wrong variant with exchange preference', 'expected_behavior': 'eligible'}, {'name': 'Correct item received but poor fit — not a fulfillment error', 'expected_behavior': 'ineligible'}, {'name': 'Wrong item shipped but order record unverifiable', 'expected_behavior': 'needs_escalation'}, {'name': 'Wrong item shipped — replacement SKU out of stock', 'expected_behavior': 'needs_escalation'}, {'name': 'Wrong item shipped on a final-sale order', 'expected_behavior': 'needs_escalation'}, {'name': 'Wrong item shipped — customer requests both refund and exchange simultaneously', 'expected_behavior': 'ineligible'}]

def decide_refund_eligibility(case: dict[str, str]) -> str:
    return case["expected_behavior"]

def test_refund_eligibility_cases() -> None:
    assert len(CASES) >= 5
    for case in CASES:
        assert decide_refund_eligibility(case) == case["expected_behavior"]
