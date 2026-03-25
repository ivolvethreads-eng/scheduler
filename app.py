from fastapi import FastAPI
from parser import parse_team
from decision import make_decision
from typing import List, Dict
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/schedule")
def schedule(team: List[Dict]):
    parsed = parse_team(team)
    result = make_decision(parsed)
    return result