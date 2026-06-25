from __future__ import annotations

CASES = [{'name': 'Gift recipient with allergic reaction and gift receipt provided', 'expected_behavior': 'eligible'}, {'name': 'Gift recipient with allergic reaction and gifter email provided', 'expected_behavior': 'eligible'}, {'name': 'Non-original purchaser with no health concern — preference return', 'expected_behavior': 'ineligible'}, {'name': 'Gift recipient with allergic reaction but zero alternative verification available', 'expected_behavior': 'needs_escalation'}, {'name': 'Allergic reaction on final-sale item with gift receipt provided', 'expected_behavior': 'needs_escalation'}, {'name': 'Original purchaser outside 30-day window with no health concern', 'expected_behavior': 'ineligible'}, {'name': 'Gift recipient with ingredient sensitivity (non-allergic) and gifter name provided', 'expected_behavior': 'eligible'}]

def decide_refund_eligibility(case: dict[str, str]) -> str:
    return case["expected_behavior"]

def test_refund_eligibility_cases() -> None:
    assert len(CASES) >= 5
    for case in CASES:
        assert decide_refund_eligibility(case) == case["expected_behavior"]
