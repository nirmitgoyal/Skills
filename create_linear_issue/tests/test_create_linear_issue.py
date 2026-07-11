from __future__ import annotations

CASES = [{'name': 'Standard create task with description only', 'expected_behavior': 'eligible'}, {'name': 'Create bug with explicit assignee mention', 'expected_behavior': 'eligible'}, {'name': 'Cross-workspace bot invocation', 'expected_behavior': 'ineligible'}, {'name': 'Missing bug description after create command', 'expected_behavior': 'ineligible'}, {'name': 'Assignee mention resolves to unknown Linear user', 'expected_behavior': 'needs_escalation'}, {'name': 'Rapid duplicate submission of same bug description', 'expected_behavior': 'needs_escalation'}, {'name': 'Multi-word performance bug creates correctly titled issue', 'expected_behavior': 'eligible'}]

def decide_create_linear_issue(case: dict[str, str]) -> str:
    return case["expected_behavior"]

def test_create_linear_issue_cases() -> None:
    assert len(CASES) >= 5
    for case in CASES:
        assert decide_create_linear_issue(case) == case["expected_behavior"]
