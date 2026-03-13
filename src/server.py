from fastmcp import FastMCP
import httpx

mcp = FastMCP("expense_management_system")
API = "http://127.0.0.1:8000"

@mcp.tool()
async def register_user(email: str, password: str, role: str) -> dict:
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{API}/auth/register", json={"email": email, "password": password, "role": role})
    return r.json()

@mcp.tool()
async def login_user(email: str, password: str) -> dict:
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{API}/auth/login", json={"email": email, "password": password})
    if r.status_code != 200:
        return {"error": "Login failed"}
    data = r.json()
    return {"access_token": data["access_token"], "token_type": data["token_type"]}

@mcp.tool()
async def add_expense(expense_amt: int, expense_category: str, token: str) -> dict:
    payload = {"expense_amt": expense_amt, "expense_category": expense_category}
    params = {"token": token}
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{API}/expense/expense", json=payload, params=params)
    return r.json()

@mcp.tool()
async def approve(emp_id: int, status: str, token: str) -> dict:
    params = {"token": token}
    async with httpx.AsyncClient() as client:
        r = await client.put(f"{API}/manager/{emp_id}", json={"status": status}, params=params)
    return r.json()

if __name__ == "__main__":
    mcp.run()
