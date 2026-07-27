from tools import tools
from langchain_ollama import ChatOllama
import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()
geminiapi_key=os.getenv("gemini_api")

def model():
    return init_chat_model(
        "google_genai:gemini-3.6-flash",
        api_key=geminiapi_key,
        timeout=120,
        max_retries=10,
    )



def agent():
    llm = model()
    return llm.bind_tools(tools)
