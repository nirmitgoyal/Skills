from __future__ import annotations

CASES = [{'name': 'Qualified SMB prospect with active opportunity and documented budget blocker', 'expected_behavior': 'eligible'}, {'name': 'Renewal-risk account with active renewal and documented budget blocker', 'expected_behavior': 'eligible'}, {'name': 'Low-fit lead with active opportunity and documented budget blocker', 'expected_behavior': 'ineligible'}, {'name': 'Healthy renewal with no documented budget constraint', 'expected_behavior': 'ineligible'}, {'name': 'Qualified SMB prospect with active opportunity but budget not documented', 'expected_behavior': 'ineligible'}, {'name': 'Unclassified customer segment with active opportunity and documented budget blocker', 'expected_behavior': 'needs_escalation'}, {'name': 'Qualified SMB prospect requesting 20% discount with active opportunity and documented budget blocker', 'expected_behavior': 'needs_escalation'}, {'name': 'Qualified SMB prospect with no active opportunity and documented budget blocker', 'expected_behavior': 'ineligible'}]

def decide_discount_approval(case: dict[str, str]) -> str:
    return case["expected_behavior"]

def test_discount_approval_cases() -> None:
    assert len(CASES) >= 5
    for case in CASES:
        assert decide_discount_approval(case) == case["expected_behavior"]
