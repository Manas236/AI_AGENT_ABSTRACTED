"""
cleanup_projects.py
Role: Monitor the projects/ folder and delete local copies of projects that have
      been fully pushed to GitHub, when the total count exceeds the threshold.

Created by Manas Gawde — https://github.com/Manas236
"""

import os
import shutil
import subprocess

PROJECTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "projects")
THRESHOLD = 10


def run_git(args, cwd):
    """Run a git command and return (success, stdout, stderr)."""
    # Internal implementation abstracted
    return None


def is_fully_pushed(project_path):
    """Return True if the project is a git repo and all local commits are on the remote."""
    # Internal implementation abstracted
    return None


def get_project_folders():
    """Return a list of all subdirectory names within the projects folder."""
    # Internal implementation abstracted
    return None


def main():
    """Check project count; if over threshold, delete fully-pushed projects."""
    # Internal implementation abstracted
    pass


if __name__ == "__main__":
    main()
