from __future__ import annotations

CASES = [{'name': 'Matching screenshot and archive — full refund approved', 'expected_behavior': 'eligible'}, {'name': 'No screenshot and no archive record — ineligible', 'expected_behavior': 'ineligible'}, {'name': 'Screenshot provided but archive record cannot be located — escalation required', 'expected_behavior': 'needs_escalation'}, {'name': 'Chargeback threat with pending duties dispute — immediate escalation', 'expected_behavior': 'needs_escalation'}, {'name': 'Screenshot shows generic free shipping, not duties coverage — ineligible', 'expected_behavior': 'ineligible'}, {'name': 'Archive confirms duties promise; listing was corrected before order date — ineligible', 'expected_behavior': 'ineligible'}, {'name': 'Screenshot matches archive, duties amount over $200 — escalation for manager approval', 'expected_behavior': 'needs_escalation'}]

def decide_refund_eligibility(case: dict[str, str]) -> str:
    return case["expected_behavior"]

def test_refund_eligibility_cases() -> None:
    assert len(CASES) >= 5
    for case in CASES:
        assert decide_refund_eligibility(case) == case["expected_behavior"]
