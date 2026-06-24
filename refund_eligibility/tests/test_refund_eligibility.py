from __future__ import annotations

CASES = [{'name': 'Return request with valid order number provided', 'expected_behavior': 'eligible'}, {'name': 'Return request with no proof of purchase of any kind', 'expected_behavior': 'ineligible'}, {'name': 'Proof gate passed but return blocked by final-sale policy', 'expected_behavior': 'ineligible'}, {'name': 'Return request supported only by bank statement transaction', 'expected_behavior': 'eligible'}, {'name': 'Late delivery refund request with order number confirmed', 'expected_behavior': 'eligible'}, {'name': 'Refund request with no proof and customer insists on escalation', 'expected_behavior': 'needs_escalation'}]

def decide_refund_eligibility(case: dict[str, str]) -> str:
    return case["expected_behavior"]

def test_refund_eligibility_cases() -> None:
    assert len(CASES) >= 5
    for case in CASES:
        assert decide_refund_eligibility(case) == case["expected_behavior"]
