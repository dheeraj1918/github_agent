from dotenv import load_dotenv
from langchain_core.tools import tool
import requests
import base64
import os
load_dotenv()
GITHUB_TOKEN=os.getenv("GITHUB_TOKEN")
HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28"
}

BASE_URL = "https://api.github.com"

@tool
def github_create_repository(name,description=""):
    """This Tool will be helps to create new repository in github"""
    url = f"{BASE_URL}/user/repos"

    data = {
        "name": name,
        "description": description,
        "private": False,
        "auto_init": True
    }

    response = requests.post(
        url,
        headers=HEADERS,
        json=data
    )

    response.raise_for_status()
    return response.json()

@tool
def github_delete_repository(owner, repo):
    """This Tool will be helps to delete repository in github."""
    url = f"{BASE_URL}/repos/{owner}/{repo}"

    response = requests.delete(
        url,
        headers=HEADERS
    )

    response.raise_for_status()

    return True

@tool
def github_create_file(
    owner: str,
    repo: str,
    path: str,
    content: str
):
    """Create a file in GitHub. If the file already exists, update it."""

    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"

    # Check whether file already exists
    check_response = requests.get(
        url,
        headers=HEADERS
    )

    encoded = base64.b64encode(
        content.encode("utf-8")
    ).decode("utf-8")

    # FILE ALREADY EXISTS

    if check_response.status_code == 200:

        sha = check_response.json()["sha"]

        data = {
            "message": f"Update {path}",
            "content": encoded,
            "sha": sha
        }

        response = requests.put(
            url,
            headers=HEADERS,
            json=data
        )

        response.raise_for_status()

        return f"File {path} already existed, so it was updated."

    
    # FILE DOES NOT EXIST

    elif check_response.status_code == 404:

        data = {
            "message": f"Create {path}",
            "content": encoded
        }

        response = requests.put(
            url,
            headers=HEADERS,
            json=data
        )

        response.raise_for_status()

        return f"File {path} created successfully."

   # OTHER ERROR

    else:

        raise Exception(
            f"GitHub error {check_response.status_code}: "
            f"{check_response.text}"
        )

@tool
def github_delete_file(owner, repo, path):
    """This tool will be helps to delete files in github."""
    url = f"{BASE_URL}/repos/{owner}/{repo}/contents/{path}"

    # Get current SHA
    response = requests.get(
        url,
        headers=HEADERS
    )

    response.raise_for_status()

    sha = response.json()["sha"]

    data = {
        "message": f"Delete {path}",
        "sha": sha
    }

    response = requests.delete(
        url,
        headers=HEADERS,
        json=data
    )

    response.raise_for_status()

    return True

@tool
def github_update_file(owner, repo, path, content):
    """
    This tool will helps to update files in github."""
    url = f"{BASE_URL}/repos/{owner}/{repo}/contents/{path}"

    # Get current file SHA
    response = requests.get(
        url,
        headers=HEADERS
    )

    response.raise_for_status()

    sha = response.json()["sha"]

    encoded = base64.b64encode(
        content.encode()
    ).decode()

    data = {
        "message": f"Update {path}",
        "content": encoded,
        "sha": sha
    }

    response = requests.put(
        url,
        headers=HEADERS,
        json=data
    )

    response.raise_for_status()

    return response.json()
