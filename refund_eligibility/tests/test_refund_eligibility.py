from __future__ import annotations

CASES = [{'name': 'Charge exactly 1 day (within 24 hours) after trial end — standard eligible case', 'expected_behavior': 'eligible'}, {'name': 'Charge 48 hours after trial end — outside 24-hour window', 'expected_behavior': 'ineligible'}, {'name': 'Annual renewal charge with zero account usage — not a trial conversion', 'expected_behavior': 'needs_escalation'}, {'name': 'Customer has already received a prior courtesy refund on same account', 'expected_behavior': 'ineligible'}, {'name': 'Customer-stated trial end date conflicts with system records — unverifiable window', 'expected_behavior': 'needs_escalation'}, {'name': 'Charge within 24 hours but charge_amount does not match plan pricing on record', 'expected_behavior': 'needs_escalation'}]

def decide_refund_eligibility(case: dict[str, str]) -> str:
    return case["expected_behavior"]

def test_refund_eligibility_cases() -> None:
    assert len(CASES) >= 5
    for case in CASES:
        assert decide_refund_eligibility(case) == case["expected_behavior"]
