# EY AI Challenge Deadline Manager - Makefile
# Usage: make <target>

.PHONY: help install dev-install run test lint format typecheck clean update check-format lint-check setup-hooks pre-commit-all

# Default target
help:
	@echo "🧠 EY AI Challenge Deadline Manager - Available Commands:"
	@echo ""
	@echo "Setup & Installation:"
	@echo "  install      - Install production dependencies"
	@echo "  dev-install  - Install all dependencies (including dev)"
	@echo ""
	@echo "Development:"
	@echo "  run          - Start the Streamlit application"
	@echo "  test         - Run the test suite"
	@echo "  lint         - Run code linting (ruff)"
	@echo "  format       - Format code (ruff)"
	@echo "  check-format - Check code formatting without applying changes"
	@echo "  lint-check   - Check linting without fixing issues"
	@echo "  typecheck    - Run type checking (mypy)"
	@echo ""
	@echo "Git Hooks:"
	@echo "  setup-hooks  - Install pre-commit hooks"
	@echo "  pre-commit-all - Run pre-commit on all files"
	@echo ""
	@echo "Maintenance:"
	@echo "  update       - Update all dependencies"
	@echo "  clean        - Clean cache and build files"
	@echo ""
	@echo "🚀 Quick start: make dev-install && make run"

# Install production dependencies
install:
	@echo "📦 Installing production dependencies..."
	uv sync --no-dev

# Install all dependencies including dev
dev-install:
	@echo "📦 Installing all dependencies..."
	uv sync

# Run the Streamlit application
run:
	@echo "🚀 Starting EY AI Deadline Manager..."
	uv run streamlit run src/ey_deadline_manager/app/streamlit_app.py

# Run tests
test:
	@echo "🧪 Running test suite..."
	python3 tests/test_streamlit_app.py
	@echo "🧪 Running agent tests..."
	python3 tests/test_agent.py

# Lint code
lint:
	@echo "🔍 Running code linting..."
	uv run ruff check --fix

# Format code
format:
	@echo "✨ Formatting code..."
	uv run ruff format

# Check formatting without applying changes
check-format:
	@echo "🔍 Checking code formatting..."
	uv run ruff format --check

# Run linting without fixing issues
lint-check:
	@echo "🔍 Checking code linting (no fixes)..."
	uv run ruff check --no-fix

# Type checking
typecheck:
	@echo "🔬 Running type checking..."
	uv run mypy *.py --ignore-missing-imports

# Update dependencies
update:
	@echo "📦 Updating dependencies..."
	uv sync --upgrade

# Setup pre-commit hooks
setup-hooks:
	@echo "🪝 Setting up pre-commit hooks..."
	uv run pre-commit install

# Run pre-commit on all files
pre-commit-all:
	@echo "🔍 Running pre-commit on all files..."
	uv run pre-commit run --all-files

# Clean cache and build files
clean:
	@echo "🧹 Cleaning cache and build files..."
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info/
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete

# Demo specific targets
demo:
	@echo "🎬 Starting demo mode..."
	uv run streamlit run src/ey_deadline_manager/app/streamlit_app.py --server.port 8504

# Batch process all documents
batch-process:
	@echo "📊 Running batch processing on all documents..."
	uv run python -c "import sys; sys.path.insert(0, 'src'); from ey_deadline_manager.app.streamlit_app import process_all_documents; from pathlib import Path; files = list(Path('data').iterdir()); process_all_documents(files[:5])"

# Check system requirements
check:
	@echo "🔍 Checking system requirements..."
	@echo "Python version:"
	@python3 --version
	@echo "UV version:"
	@uv --version
	@echo "Project dependencies:"
	@uv tree --depth 1
