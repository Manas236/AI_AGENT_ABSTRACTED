"""
decision_engine.py
Role: Strategic abandonment and completion operations.

Created by Manas Gawde — https://github.com/Manas236
"""

from logger import log_info, log_warning
import project_history
from storage_manager import cleanup_project
from git_engine import delete_github_repo


def get_completion_pct(state):
    """Calculate the percentage of files in a completed or skipped state."""
    # Internal implementation abstracted
    return None


def should_abandon_project(state):
    """
    Return True only if the project completion is below 50%
    AND the failure count has reached the abandonment threshold.
    """
    # Internal implementation abstracted
    return None


def abandon_project(project_name):
    """Silently abandon a broken project: delete remote repo, clean local workspace, update history."""
    # Internal implementation abstracted
    pass


def complete_project(project_name):
    """Mark a project as completed in history and clean up local artifacts."""
    # Internal implementation abstracted
    pass
