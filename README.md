# Calculator Agent with MCP Integration

This project demonstrates a simple AI agent that performs basic arithmetic operations using a custom tool. It also showcases integration with a custom MCP (Model Context Provider) server that supplies context to the agent — following principles of the Agent2Agent (A2A) ecosystem.

## Features

- Single-agent workflow
- Supports:
  - Addition
  - Subtraction
  - Multiplication
  - Division
- Uses an MCP server to provide the operation context
- Clean, modular structure
- Beginner-friendly example of agentic AI with MCP

## Technologies Used

- Python
- FastAPI (for MCP server)
- Modular tool-based design
- Command-line interface

## How It Works

The MCP server provides the operation to perform (e.g., "addition").  
The agent receives the numbers and operation context, performs the calculation, and returns the result.

## How to Run

### 1. Setup

git clone https://github.com/divyapriyadarshini/single_agent_calc.git
cd single_agent_calc
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


### 2. Run MCP Server (Separate Terminal)

cd mcp_server
python server.py


### 3. Run Main Workflow

In another terminal:

source .venv/bin/activate
python executor.py


Follow the prompts to input numbers, the system will use MCP to get the operation context.

## Project Structure

single_agent_calc/
├── tools/
│ └── math_tool.py
├── agent.py
├── workflow.py
├── executor.py
├── requirements.txt
├── mcp_server/
│ └── server.py
├── .gitignore
└── README.md