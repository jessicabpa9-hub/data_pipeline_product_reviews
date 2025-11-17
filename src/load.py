import os
import subprocess

def load_data(repo_url):
    git_cmd = "git"
    branch = "master"   # <-- IMPORTANT

    # Ensure .git exists
    if not os.path.exists(".git"):
        subprocess.run([git_cmd, "init"])
        subprocess.run([git_cmd, "branch", "-M", branch])
        subprocess.run([git_cmd, "remote", "add", "origin", repo_url])
    else:
        # Always update the remote to the provided repo URL
        subprocess.run([git_cmd, "remote", "set-url", "origin", repo_url])
        subprocess.run([git_cmd, "branch", "-M", branch])  # ensure correct branch

    # Add everything
    subprocess.run([git_cmd, "add", "."])

    # Git identity
    subprocess.run([git_cmd, "config", "user.name", "auto-user"])
    subprocess.run([git_cmd, "config", "user.email", "auto@example.com"])

    # Commit
    subprocess.run([git_cmd, "commit", "--allow-empty", "-m", "Publish processed data"])

    # PUSH to master
    subprocess.run([git_cmd, "push", "-u", "origin", branch, "--force"])

    print(f"Published updates to GitHub repo: {repo_url} (branch: {branch})")


if __name__ == "__main__":
    load_data("https://github.com/jessicabpa9-hub/-git-demo.git")
