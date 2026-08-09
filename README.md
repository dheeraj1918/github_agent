## 📂 Local File & Folder Management

GitHub Agent can also directly manage files and folders in the local project using its file-system tools.

It can perform CRUD operations on local files and directories:

* **Create** files
* **Read** files
* **Update** existing files
* **Delete** files
* **Create** folders
* **Read** folder contents
* **Update** files inside folders
* **Delete** folders and their contents

This allows the agent to work directly inside an existing project and modify the codebase according to the user's requirements.

Example:

```text
Create a new authentication folder.
```

```text
Create auth/login.py and auth/register.py.
```

```text
Read the existing database.py file.
```

```text
Update the login function in auth/login.py.
```

```text
Delete the old test files.
```

The agent can understand the existing project structure before making changes, helping it preserve the architecture and coding style of the project.

---

## 🔐 GitHub Repository & File Management

With a GitHub Personal Access Token, GitHub Agent can manage repositories and files directly through the GitHub API.

It can perform CRUD operations such as:

* **Create** GitHub repositories
* **Read** repository information and files
* **Update** repository files
* **Delete** GitHub repositories
* **Create** files in repositories
* **Delete** files from repositories
* Upload generated project files directly to GitHub

This allows GitHub Agent to move from **code generation to actual project management and deployment to GitHub**.

Example:

```text
Create a repository called my-project.
```

```text
Create app.py and requirements.txt in the repository.
```

```text
Update app.py with the latest implementation.
```

```text
Delete the old test.py file.
```

🔑 Environment Variables

GitHub Agent uses Google Gemini for AI-powered reasoning and code generation, and the GitHub Personal Access Token for managing GitHub repositories and files.

Create a .env file inside the project root:

gemini_api=YOUR_GEMINI_API_KEY
GITHUB_TOKEN=YOUR_GITHUB_ACCESS_TOKEN
