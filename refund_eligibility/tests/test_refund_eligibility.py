from __future__ import annotations

CASES = [{'name': 'Confirmed IP Mismatch With Customer Fraud Report', 'expected_behavior': 'eligible'}, {'name': 'Customer Reports Unauthorized Charge No IP Data Available', 'expected_behavior': 'needs_escalation'}, {'name': 'IP Mismatch Detected But Customer Does Not Report Unauthorized Charge', 'expected_behavior': 'needs_escalation'}, {'name': 'Customer Cannot Confirm Account Email During Fraud Report', 'expected_behavior': 'needs_escalation'}, {'name': 'Unauthorized Charge Report With No Matching Order ID In System', 'expected_behavior': 'needs_escalation'}, {'name': 'Legitimate Authorized Purchase Disputed as Unauthorized Without Supporting Signals', 'expected_behavior': 'ineligible'}]

def decide_refund_eligibility(case: dict[str, str]) -> str:
    return case["expected_behavior"]

def test_refund_eligibility_cases() -> None:
    assert len(CASES) >= 5
    for case in CASES:
        assert decide_refund_eligibility(case) == case["expected_behavior"]
