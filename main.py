import os
from github import Github

# Get GitHub token from environment variable
GITHUB_TOKEN = os.environ.get("GH_TOKEN")

if not GITHUB_TOKEN:
    print("Error: GH_TOKEN environment variable not set.")
    exit(1)

g = Github(GITHUB_TOKEN)

print(f"Logged in as: {g.get_user().login}")

print("\nYour repositories:")
for repo in g.get_user().get_repos():
    print(f"- {repo.name}")
