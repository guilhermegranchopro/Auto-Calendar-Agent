"""
EY AI Challenge Deadline Manager - Core Module
Core business logic for deadline processing and analysis.
"""

from .deadline_agent_backend import (
    DeadlineManagerAgent,
    create_agent,
    process_file,
    process_folder,
    process_text,
)

__version__ = "1.0.0"
