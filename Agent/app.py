from builder import builder
from langchain_core.messages import HumanMessage 
from model import model
state = {
    "messages": []
}

print("Type 'exit' to quit.\n")

while True:
    query = input("You: ")

    if query.lower() in {"quit", "exit"}:
        break

    state["messages"].append(HumanMessage(content=query))
    graph=builder()
    state = graph.invoke(state)

    print("Bot:", state["messages"][-1].content[0]["text"])