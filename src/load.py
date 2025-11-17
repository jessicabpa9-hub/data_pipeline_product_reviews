import os
import subprocess

def load_data():
    file_path = "data/processed/reviews_products.processed.csv"
    git_cmd = "git"

    # Initialize repo if missing
    if not os.path.exists(".git"):
        subprocess.run([git_cmd, "init"])
        subprocess.run([git_cmd, "branch", "-M", "main"])
        subprocess.run([
            git_cmd, "remote", "add", "origin",
            "https://github.com/jessicabpa9-hub/test_pipeline.git"
        ])

    # Add everything so it always matches the repo
    subprocess.run([git_cmd, "add", "."])

    subprocess.run([git_cmd, "config", "user.name", "jessicabpa9-hub"])
    subprocess.run([git_cmd, "config", "user.email", "your-email@example.com"])

    subprocess.run([git_cmd, "commit", "--allow-empty", "-m", "Publish processed data"])

    # 🚨 FORCE PUSH — overwrite remote completely
    subprocess.run([git_cmd, "push", "-u", "origin", "main", "--force"])

    print("Pushed to: https://github.com/jessicabpa9-hub/test_pipeline.git")

if __name__ == "__main__":
    load_data()
