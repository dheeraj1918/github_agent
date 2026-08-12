from ddgs import DDGS
from langchain_core.tools import tool
import traceback

@tool
def webSearch(query:str,max_results:int)->list:
    """This tool will allows the agent for web search
    Args:
    query: Required search query string.
        max_results: The maximum number of search results to return.
    Returns:
    List of search results object
    """
    results_ddg = DDGS().text(query=query, max_results=int(max_results))
    if results_ddg:
        return results_ddg
    else:
        return ("No results found from DuckDuckGo search.")