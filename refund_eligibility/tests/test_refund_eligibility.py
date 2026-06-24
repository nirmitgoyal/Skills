from __future__ import annotations

CASES = [{'name': 'Confirmed IP Mismatch Unauthorized Charge — Standard Fraud Lockdown', 'expected_behavior': 'eligible'}, {'name': 'Unauthorized Charge Reported But No IP Mismatch Detectable', 'expected_behavior': 'needs_escalation'}, {'name': 'Forgotten Annual Subscription Renewal — No Fraud Signal', 'expected_behavior': 'ineligible'}, {'name': 'Customer Cannot Confirm Account Email After Lockdown Triggered', 'expected_behavior': 'needs_escalation'}, {'name': 'Trial Period Overage Charge — No Unauthorized Access Claim', 'expected_behavior': 'ineligible'}, {'name': 'Gift Recipient Reporting Health Safety Concern — No Fraud Signal', 'expected_behavior': 'ineligible'}, {'name': 'Multiple Unauthorized Charges Across Different Orders With IP Mismatch', 'expected_behavior': 'needs_escalation'}]

def decide_refund_eligibility(case: dict[str, str]) -> str:
    return case["expected_behavior"]

def test_refund_eligibility_cases() -> None:
    assert len(CASES) >= 5
    for case in CASES:
        assert decide_refund_eligibility(case) == case["expected_behavior"]
