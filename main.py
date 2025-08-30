from fastapi import FastAPI, HTTPException
from typing import List
import uvicorn

from schemas import Requirement, TestCase
from services.testcase_generator import generate_testcases

app = FastAPI(
    title="Care2Test Backend",
    description="Healthcare-focused requirement → test case generator",
    version="0.1.0",
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/generate", response_model=List[TestCase])
def generate_endpoint(requirements: List[Requirement]):
    if not requirements:
        raise HTTPException(status_code=400, detail="No requirements provided")
    return generate_testcases(requirements)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
