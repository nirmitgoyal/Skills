from __future__ import annotations

CASES = [{'name': '2-day shipping arrived 8 days late, item useless for passed event', 'expected_behavior': 'eligible'}, {'name': 'Expedited shipping arrived 1 day late, customer states no time-sensitive purpose', 'expected_behavior': 'ineligible'}, {'name': 'Refund previously issued for late delivery but not yet visible on credit card', 'expected_behavior': 'needs_escalation'}, {'name': '2-day shipping arrived 5 days late, customer states item was time-sensitive for a medical appointment', 'expected_behavior': 'eligible'}, {'name': 'Late delivery on a Black Friday final sale order', 'expected_behavior': 'ineligible'}, {'name': 'Customer claims late delivery but paid_shipping_tier was standard free shipping', 'expected_behavior': 'ineligible'}, {'name': 'Expedited shipping late delivery with unverifiable actual delivery date', 'expected_behavior': 'needs_escalation'}]

def decide_refund_eligibility(case: dict[str, str]) -> str:
    return case["expected_behavior"]

def test_refund_eligibility_cases() -> None:
    assert len(CASES) >= 5
    for case in CASES:
        assert decide_refund_eligibility(case) == case["expected_behavior"]
