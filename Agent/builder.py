from langgraph.graph import StateGraph,START,END
from state import State,bot
from langgraph.prebuilt import ToolNode,tools_condition
from tools import tools
def builder():
    builder = StateGraph(State)

    builder.add_node("bot", bot)
    builder.add_node("tools", ToolNode(tools))

    builder.add_edge(START, "bot")

    builder.add_conditional_edges(
        "bot",
        tools_condition,
    )

    builder.add_edge("tools", "bot")

    builder.add_edge("bot", END)

    graph = builder.compile()
    print("The graph has been build. \n")
    return graph