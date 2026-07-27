from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from model import agent as create_agent


class State(TypedDict):
    messages: Annotated[list, add_messages]


def bot(state: State):
    chat_agent = create_agent()
    print("The agent is created. \n")
    response = chat_agent.invoke(state["messages"])
    print("The agent got response. \n")
    return {
        "messages": [response]
    }