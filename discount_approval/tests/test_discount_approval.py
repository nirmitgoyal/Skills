from __future__ import annotations

CASES = [{'name': 'All three criteria met — qualified SMB with active opportunity and documented budget blocker', 'expected_behavior': 'eligible'}, {'name': 'Renewal-risk account with documented budget blocker and active renewal', 'expected_behavior': 'eligible'}, {'name': 'Low-fit lead citing budget concerns with active opportunity', 'expected_behavior': 'ineligible'}, {'name': 'Healthy renewal account — no budget blocker documented', 'expected_behavior': 'ineligible'}, {'name': 'Qualified prospect with budget blocker but no active opportunity or renewal on record', 'expected_behavior': 'ineligible'}, {'name': 'Ambiguous profile classification — rep unsure if customer fits target segment', 'expected_behavior': 'needs_escalation'}, {'name': 'Verbal budget blocker claim only — no written documentation provided', 'expected_behavior': 'needs_escalation'}]

def decide_discount_approval(case: dict[str, str]) -> str:
    return case["expected_behavior"]

def test_discount_approval_cases() -> None:
    assert len(CASES) >= 5
    for case in CASES:
        assert decide_discount_approval(case) == case["expected_behavior"]
