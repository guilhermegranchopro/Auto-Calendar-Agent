"""
EY AI Challenge Deadline Manager

A sophisticated AI-powered deadline management system for Portuguese tax professionals.
"""

__version__ = "1.0.0"
__author__ = "Guilherme Grancho"
__email__ = "guilherme@example.com"

# Import main modules
from . import core, models, utils

# Import key functions from core
from .core.deadline_agent_backend import (
    DeadlineManagerAgent,
    create_agent,
    process_file,
    process_folder,
    process_text,
)

__all__ = [
    "DeadlineManagerAgent",
    "app",
    "core",
    "create_agent",
    "main",
    "models",
    "process_file",
    "process_folder",
    "process_text",
    "utils",
]
