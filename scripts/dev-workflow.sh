#!/bin/bash
# EY AI Deadline Manager - Development Workflow Summary
# This script demonstrates the new development workflow using uv and ruff

set -e  # Exit on any error

echo "🧠 EY AI Challenge Deadline Manager - Development Workflow"
echo "================================================="
echo ""

echo "📦 Environment Management with UV:"
echo "  uv sync              # Install dependencies"
echo "  uv sync --no-dev     # Install production only"
echo "  uv sync --upgrade    # Update all dependencies"
echo "  uv add <package>     # Add new dependency"
echo "  uv remove <package>  # Remove dependency"
echo ""

echo "🚀 Running the Application:"
echo "  uv run streamlit run streamlit_app.py"
echo "  make run             # Alternative using Makefile"
echo ""

echo "🔍 Code Quality with Ruff (replacing black + flake8):"
echo "  uv run ruff check --fix     # Lint and auto-fix"
echo "  uv run ruff format          # Format code"
echo "  uv run ruff check --no-fix  # Check without fixing"
echo "  uv run ruff format --check  # Check formatting"
echo ""

echo "🛠️ Makefile Targets:"
echo "  make help            # Show all available commands"
echo "  make dev-install     # Install all dependencies"
echo "  make lint            # Run ruff linting with fixes"
echo "  make format          # Run ruff formatting"
echo "  make check-format    # Check formatting without changes"
echo "  make lint-check      # Check linting without fixes"
echo "  make typecheck       # Run mypy type checking"
echo "  make test            # Run test suite"
echo "  make setup-hooks     # Install pre-commit hooks"
echo "  make pre-commit-all  # Run pre-commit on all files"
echo ""

echo "🪝 Git Hooks with Pre-commit:"
echo "  pre-commit install   # Install hooks (make setup-hooks)"
echo "  pre-commit run --all-files  # Run on all files"
echo ""

echo "⚡ Performance Comparison:"
echo "  Old: black + flake8 (slower, separate tools)"
echo "  New: ruff (ultra-fast, all-in-one linter + formatter)"
echo ""

echo "🎯 Current Status:"
if command -v uv &> /dev/null; then
    echo "  ✅ UV $(uv --version) installed"
else
    echo "  ❌ UV not installed"
fi

if [ -f "pyproject.toml" ]; then
    echo "  ✅ pyproject.toml configured"
else
    echo "  ❌ pyproject.toml missing"
fi

if [ -f ".pre-commit-config.yaml" ]; then
    echo "  ✅ Pre-commit configuration ready"
else
    echo "  ❌ Pre-commit configuration missing"
fi

if [ -d ".venv" ]; then
    echo "  ✅ Virtual environment created"
else
    echo "  ❌ Virtual environment missing"
fi

echo ""
echo "🚀 Quick Start:"
echo "  1. uv sync"
echo "  2. make setup-hooks"
echo "  3. make run"
echo ""
echo "Happy coding! 🎉"
