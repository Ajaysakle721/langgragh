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


# Print final result
print(result)