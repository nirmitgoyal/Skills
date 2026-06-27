# refund_eligibility

When a customer requests a refund for an item purchased during an explicitly marked final-sale promotional event (e.g., Black Friday), the system performs a deterministic lookup of order metadata to verify the promotional event flag and associated non-refund disclosure record. If both are confirmed, the refund request is categorically denied with no exceptions permitted, regardless of fit, condition, defect claims, or personal circumstances. The agent acknowledges the customer's concern, cites the final-sale terms disclosed at checkout, and may offer forward-looking assistance (e.g., sizing guidance) but must not offer partial refunds, store credit alternatives, or escalation paths as substitutes for policy compliance.

## Decision Rules

- RULE-1: If order metadata confirms a promotional_event_flag is present AND a promotional_terms_disclosure_record is on file for that order, classify as ineligible and deny refund — no exceptions.
- RULE-2: The ineligibility determination is independent of reason for return: fit issues, condition complaints, preference changes, and defect claims are all equally non-qualifying under a confirmed final-sale flag.
- RULE-3: If order_id cannot be resolved or promotional_event_flag is absent from order metadata, do not assume ineligibility — escalate to human review.
- RULE-4: If promotional_terms_disclosure_record is missing or cannot be confirmed despite a promotional_event_flag being present, escalate to human review rather than auto-denying.
- RULE-5: Agent must not offer store credit, partial refunds, or exchanges as policy workarounds when final-sale status is confirmed.
- RULE-6: Agent may offer non-compensatory forward-looking assistance (e.g., sizing guidance for future purchases) after delivering the denial.
- RULE-7: If the customer raises a potential false-advertising or disclosure failure claim (e.g., asserts final-sale terms were not shown at checkout), escalate immediately rather than denying.

## Required Fields

- order_id
- promotion_flag_at_checkout
- promotional_terms_disclosure_record

## Escalation

- Escalate if order_id cannot be located in the order management system.
- Escalate if promotional_event_flag is present but promotional_terms_disclosure_record is missing, ambiguous, or disputed by the customer.
- Escalate if customer provides evidence or credible assertion that final-sale terms were not disclosed at checkout (potential false-advertising or disclosure failure scenario, analogous to the duties-included case in src_slack_c0ba1v2k269_1781262809670129).
- Escalate if the item shows evidence of a manufacturing defect that predates purchase — quality-team review may be warranted as a separate track from refund policy (cf. defect-escalation precedent in src_slack_c0ba1v2k269_1781262697508679), but this escalation must be framed as a quality review, not a refund override.
- Do not escalate solely because the customer is dissatisfied with the denial; the policy is categorical once both flags are confirmed.
