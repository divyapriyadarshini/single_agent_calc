from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ContextRequest(BaseModel):
    agent_id: str
    query: str

@app.post("/context")
def get_context(req: ContextRequest):
    return {"context": f"Context for {req.agent_id} based on '{req.query}'"}
