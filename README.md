🧩 LangGraph Beginner Examples





A simple, beginner-friendly LangGraph project created to understand the core concepts of graph-based workflows.

This project contains two practical examples:

👋 Greeting Workflow — passes a name through nodes and generates a greeting.

➕✖️ Calculation Workflow — adds two numbers and passes the result to another node for multiplication.

The examples focus on understanding State, Nodes, Edges, START, END, Compile, and Invoke before moving to advanced LangGraph applications.

🧠 What is LangGraph?

LangGraph is a framework for building stateful workflows and AI agents.

Instead of writing one large function, a workflow can be divided into small, independent nodes. Edges define how the workflow moves from one node to another.

🔄 Basic Workflow

┌─────────┐
│  START  │
└────┬────┘
     │
     ▼
┌─────────────┐
│    Node     │
└─────┬───────┘
      │
      ▼
┌─────────────┐
│    Node     │
└─────┬───────┘
      │
      ▼
┌─────────┐
│   END   │
└─────────┘

✨ Concepts Covered

Concept

Purpose

🗃️ State

Stores the data used by the workflow

⚙️ Node

Performs a specific task

🔗 Edge

Defines the flow between nodes

🟢 START

Starting point of the graph

🔴 END

Ending point of the graph

🛠️ Compile

Converts the graph into an executable workflow

▶️ Invoke

Executes the graph

🔄 State Flow

Passes data from one node to another

👋 Example 1: Greeting Workflow

🎯 Objective

Take a person's name and generate a personalized greeting.

Input:

Rahul

Output:

Hello Rahul!

🔄 Workflow

┌─────────┐
│  START  │
└────┬────┘
     │
     ▼
┌──────────────┐
│  name_node   │
│  Get the name│
└──────┬───────┘
       │
       ▼
┌─────────────────┐
│ greeting_node   │
│ Create greeting │
└───────┬─────────┘
        │
        ▼
   ┌─────────┐
   │   END   │
   └─────────┘

💻 Code

from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    name: str
    greeting: str


def name_node(state: State):
    return {
        "name": state["name"]
    }


def greeting_node(state: State):
    return {
        "greeting": "Hello " + state["name"] + "!"
    }


builder = StateGraph(State)

builder.add_node("name_node", name_node)
builder.add_node("greeting_node", greeting_node)

builder.add_edge(START, "name_node")
builder.add_edge("name_node", "greeting_node")
builder.add_edge("greeting_node", END)

graph = builder.compile()

result = graph.invoke({
    "name": "Rahul"
})

print(result)

📤 Output

{'name': 'Rahul', 'greeting': 'Hello Rahul!'}

➕ Example 2: Addition & Multiplication Workflow

🎯 Objective

This example demonstrates how data is created in one node and then used by the next node.

First, the add node calculates:

10 + 20 = 30

Then, the multiply node calculates:

30 × 10 = 300

🔄 Workflow

┌─────────┐
│  START  │
└────┬────┘
     │
     ▼
┌─────────────┐
│     add     │
│ 10 + 20 = 30│
└─────┬───────┘
      │
      ▼
┌────────────────┐
│    multiply    │
│  30 × 10 = 300 │
└───────┬────────┘
        │
        ▼
   ┌─────────┐
   │   END   │
   └─────────┘

💻 Code

from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# State
class State(TypedDict):
    a: int
    b: int
    sum: int
    result: int


# Add node
def add(state: State):
    return {
        "sum": state["a"] + state["b"]
    }


# Multiply node
def multiply(state: State):
    return {
        "result": state["sum"] * 10
    }


# Create graph
builder = StateGraph(State)


# Add nodes
builder.add_node("add", add)
builder.add_node("multiply", multiply)


# Add edges
builder.add_edge(START, "add")
builder.add_edge("add", "multiply")
builder.add_edge("multiply", END)


# Compile graph
graph = builder.compile()


# Run graph
result = graph.invoke({
    "a": 10,
    "b": 20,
    "sum": 0,
    "result": 0
})


print(result)

📤 Output

{'a': 10, 'b': 20, 'sum': 30, 'result': 300}

🔍 How LangGraph Works in These Examples

Both examples follow the same basic pattern:

1. Define State
       ↓
2. Create Node Functions
       ↓
3. Create StateGraph
       ↓
4. Add Nodes
       ↓
5. Add Edges
       ↓
6. Compile Graph
       ↓
7. Invoke Graph
       ↓
8. Get Final State

🗃️ 1. State

State defines the data that flows through the graph.

Example:

class State(TypedDict):
    a: int
    b: int
    sum: int
    result: int

⚙️ 2. Nodes

Nodes are Python functions that perform tasks.

Example:

def add(state: State):
    return {
        "sum": state["a"] + state["b"]
    }

🔗 3. Edges

Edges define which node runs next.

builder.add_edge("add", "multiply")

This creates:

add → multiply

🛠️ 4. Compile

The graph is compiled before execution:

graph = builder.compile()

▶️ 5. Invoke

The graph is executed using:

result = graph.invoke(...)

📁 Project Structure

langgraph/
│
├── app.py
├── README.md
└── requirements.txt

You can keep either example in app.py, or place the examples in separate Python files as the project grows.

🚀 Getting Started

1. Clone the Repository

git clone https://github.com/<your-username>/<your-repository>.git
cd langgraph

2. Install LangGraph

pip install langgraph

Or install all project dependencies:

pip install -r requirements.txt

3. Run the Project

python app.py

📦 Requirements

Create a requirements.txt file with:

langgraph

🎯 Learning Goal

After completing these examples, you should understand:

What LangGraph is

How State works

How nodes work

How edges control workflow

How START and END work

Why a graph is compiled

How invoke() executes a workflow

How data moves between nodes

🔭 Next Steps

Once these basics are clear, you can continue with:

🔀 Conditional Edges

🔁 Loops

🤖 LangGraph + LLM

💬 Chatbot with LangGraph

📚 LangGraph + RAG

🧠 Memory and Persistence

🛠️ LangGraph Agents

👨‍💻 Human-in-the-loop workflows

🔗 LangGraph + MCP

👨‍💻 Author

Ajay Sakle

GitHub: Ajaysakle721

📄 License

This project is licensed under the MIT License.
