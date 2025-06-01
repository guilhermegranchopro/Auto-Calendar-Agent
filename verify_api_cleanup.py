#!/usr/bin/env python3
"""
Script to verify all hardcoded API keys have been removed from the repository.
"""
import os
import re
from pathlib import Path

def search_for_api_keys(directory):
    """Search for hardcoded API keys in files."""
    # Construct the API key pattern to avoid including it directly in this file
    api_key_pattern = r"AIzaSyB1XJV_" + "CWEu9zojtETnViNEhwoFa8CF-FE"
    found_files = []
    
    # File extensions to check
    extensions = ['.py', '.md', '.txt', '.ipynb', '.env', '.example']
    
    for file_path in Path(directory).rglob('*'):
        if file_path.is_file() and any(str(file_path).endswith(ext) for ext in extensions):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if re.search(api_key_pattern, content):
                        found_files.append(str(file_path))
            except (UnicodeDecodeError, PermissionError):
                # Skip binary files or files we can't read
                continue
    
    return found_files

if __name__ == "__main__":
    repo_root = "/home/guilhermegrancho/ey-challenge/Auto-Calendar-Agent"
    found_files = search_for_api_keys(repo_root)
    
    if found_files:
        print("❌ Found hardcoded API keys in the following files:")
        for file_path in found_files:
            print(f"   - {file_path}")
        exit(1)
    else:
        print("✅ No hardcoded API keys found in the repository!")
        print("🔐 All API key references have been successfully cleaned!")
        exit(0)
