import requests
from typing import Dict

API = "http://127.0.0.1:8000"

AGENT_MEMORY = {
    "token": None
}

async def execute_action(action: str, data: Dict):
    token = AGENT_MEMORY.get("token")
    if action == "add_user":
        r = requests.post(f"{API}/auth/register", json=data)
    elif action == "verify_user":
       r = requests.post(f"{API}/auth/login", json=data)
       if r.status_code == 200:
            AGENT_MEMORY["token"] = r.json().get("access_token")

    elif action == "add_expense":
        r = requests.post(
            f"{API}/expense/expense",
            params={"token":token},
            json=data
        )
    elif action == "generate_report":
        r = requests.get(f"{API}/report/report",
                         params={"token":token},
                          json=data)
    elif action == "manager_action":
        r = requests.post(f"{API}/manager/report", 
                          params={"token":token},
                          json=data)
    else:
        return {"error": "unknown action"}
    return r.json()


    
