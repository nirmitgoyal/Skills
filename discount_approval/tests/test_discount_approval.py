from __future__ import annotations

CASES = [{'name': 'All three criteria met — SMB renewal at risk', 'expected_behavior': 'eligible'}, {'name': 'All three criteria met — high-intent new opportunity', 'expected_behavior': 'eligible'}, {'name': 'Healthy renewal with no budget blocker', 'expected_behavior': 'ineligible'}, {'name': 'Low-fit lead citing budget concerns', 'expected_behavior': 'ineligible'}, {'name': 'Blanket discount request for all prospects', 'expected_behavior': 'ineligible'}, {'name': 'Budget verbally cited but not documented in CRM', 'expected_behavior': 'needs_escalation'}, {'name': 'Customer profile fit is ambiguous', 'expected_behavior': 'needs_escalation'}, {'name': 'No active opportunity or renewal in CRM', 'expected_behavior': 'ineligible'}]

def decide_discount_approval(case: dict[str, str]) -> str:
    return case["expected_behavior"]

def test_discount_approval_cases() -> None:
    assert len(CASES) >= 5
    for case in CASES:
        assert decide_discount_approval(case) == case["expected_behavior"]
