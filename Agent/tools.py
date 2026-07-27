from publicUrl import getGithubDetails

# Expose the actual tool list for LangGraph and LangChain bindings.
tools = [getGithubDetails]