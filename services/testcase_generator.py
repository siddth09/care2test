from typing import List
from schemas import Requirement, TestCase

def generate_testcases(requirements: List[Requirement]) -> List[TestCase]:
    """Simple deterministic generator (placeholder for AI/LLM later)."""
    testcases = []
    for i, req in enumerate(requirements, start=1):
        tc = TestCase(
            id=f"TC-{i:03}",
            requirement_id=req.id,
            description=f"Validate healthcare requirement: {req.text}",
            steps=[
                "1) Prepare test environment with anonymized patient data",
                f"2) Execute requirement: {req.text}",
                "3) Validate outcome against healthcare compliance standards"
            ],
            expected_result="System behaves according to requirement without violating patient safety/privacy",
            compliance_tags=["IEC-62304", "HIPAA", "GDPR"]
        )
        testcases.append(tc)
    return testcases
