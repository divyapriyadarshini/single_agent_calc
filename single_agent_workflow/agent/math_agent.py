from tools.calculator import add, subtract, multiply, divide
import requests

class MathAgent:
    
    def __init__(self, agent_id="math_agent"):
        self.agent_id = agent_id
    
    def execute(self, operation, a, b):
        context = self.get_context(operation)
        print(f"[Context] {context}")

        if operation == "add":
            result = add(a, b)
        elif operation == "subtract":
            result = subtract(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        elif operation == "divide":
            result = divide(a, b)
        else:
            raise ValueError("Unsupported operation")

        print(f"[Result] {result}")
        return result

    def get_context(self, query):
        try:
            resp = requests.post("http://localhost:8000/context", json={
                "agent_id": self.agent_id,
                "query": query
            })
            if resp.status_code == 200:
                return resp.json().get("context")
            else:
                return "Default context - MCP unavailable"
        except:
            return "Default context - MCP unavailable"
