from langchain_core.tools import tool
import requests


@tool
def getGithubDetails(username:str):
    """Help to fetch github details by providing username on link"""
    print("\n The tool has been activated. \n")
    url=f"https://api.github.com/users/{username}/repos"
    try:
        response=requests.get(url)
        if response.status_code==200:
            data=response.json()
            return data
    except Exception as e:
        return f"Error: {e}"

  