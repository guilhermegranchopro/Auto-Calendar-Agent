#!/usr/bin/env python3
"""
EY AI Challenge Deadline Manager - Main Entry Point

This is the main entry point for the EY AI Challenge Deadline Manager application.
It provides a command-line interface to launch the Streamlit application.
"""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

from ey_deadline_manager.app.streamlit_app import main

if __name__ == "__main__":
    main()
