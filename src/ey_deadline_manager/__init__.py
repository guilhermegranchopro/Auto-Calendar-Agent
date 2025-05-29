"""
EY AI Deadline Manager - A comprehensive AI-powered solution for Portuguese tax deadline management.

This package provides intelligent deadline extraction and management capabilities for Portuguese
tax professionals, featuring multi-modal document processing, Portuguese tax law compliance,
and AI-powered deadline inference.
"""

__version__ = "1.0.0"
__author__ = "Guilherme Grancho"
__email__ = "guilherme@example.com"

from .deadline_agent_backend import (
    DeadlineManagerAgent,
    add_working_days,
    apply_portuguese_tax_rules,
    process_with_gemini_ai,
)
from .streamlit_app import main

__all__ = [
    "DeadlineManagerAgent",
    "add_working_days",
    "apply_portuguese_tax_rules",
    "main",
    "process_with_gemini_ai",
]
