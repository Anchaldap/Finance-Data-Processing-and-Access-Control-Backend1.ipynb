import uuid
from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

# Initialize App
app = FastAPI(title="Zorvyn Finance Backend")

# Enable CORS (Required for web access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock Database
db = {
    "users": [{"id": "admin-123", "role": "Admin", "name": "Anchal Patel"}],
    "records": [{"id": "1", "amount": 5000.0, "type": "income", "category": "Salary", "date": "2026-04-01"}]
}

# Data Model
class RecordIn(BaseModel):
    amount: float
    type: str
    category: str
    date: str

# Root Endpoint
@app.get("/")
async def root():
    return {"message": "Zorvyn Backend is Running!", "status": "Online"}

# Dashboard Summary Endpoint
@app.get("/dashboard/summary")
async def get_summary(x_user_id: str = Header("admin-123")):
    recs = db["records"]
    income = sum(r["amount"] for r in recs if r["type"] == "income")
    expense = sum(r["amount"] for r in recs if r["type"] == "expense")
    return {
        "total_income": income,
        "total_expense": expense,
        "net_balance": income - expense
    }

# Create Record Endpoint
@app.post("/records")
async def add_record(rec: RecordIn):
    new_rec = rec.dict()
    new_rec["id"] = str(uuid.uuid4())
    db["records"].append(new_rec)
    return new_rec
