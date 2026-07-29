from pathlib import Path
from langchain_core.tools import tool
import os
import datetime

@tool
def create_file(path: str, content: str):
    """This tool help to create open file and read, write file"""
    with open(str, "a") as f:
        return f.write(str)
    
        #open and read the file after the appending:
    with open(str) as f:
        return f.read(str)
    

@tool
def create_folder(path:str,content:str):
    """This tool will hepls to Create a file with the given content."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    
    return f"Created {path}"

