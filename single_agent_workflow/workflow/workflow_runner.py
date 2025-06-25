from agent.math_agent import MathAgent

def run_workflow():
    agent = MathAgent()

    print("=== Math Agent ===")
    
    operation = input("Choose operation (add / subtract / multiply / divide): ").strip().lower()
    
    if operation not in ["add", "subtract", "multiply", "divide"]:
        print("Unsupported operation. Exiting.")
        return
    
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number input. Exiting.")
        return

    print("\nStarting Task...")
    try:
        agent.execute(operation, a, b)
    except Exception as e:
        print(f"Error: {e}")
