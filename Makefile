# EY AI Challenge Deadline Manager - Makefile
# Usage: make <target>

.PHONY: help install dev-install run test lint format typecheck clean update

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
	@echo "  lint         - Run code linting (flake8)"
	@echo "  format       - Format code (black)"
	@echo "  typecheck    - Run type checking (mypy)"
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
	uv run streamlit run streamlit_app.py

# Run tests
test:
	@echo "🧪 Running test suite..."
	uv run python test_streamlit_app.py
	@echo "🧪 Running pytest..."
	uv run pytest test_agent.py -v

# Lint code
lint:
	@echo "🔍 Running code linting..."
	uv run flake8 *.py --max-line-length=88 --extend-ignore=E203,W503

# Format code
format:
	@echo "✨ Formatting code..."
	uv run black *.py

# Type checking
typecheck:
	@echo "🔬 Running type checking..."
	uv run mypy *.py --ignore-missing-imports

# Update dependencies
update:
	@echo "📦 Updating dependencies..."
	uv sync --upgrade

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
	uv run streamlit run streamlit_app.py --server.port 8504

# Batch process all documents
batch-process:
	@echo "📊 Running batch processing on all documents..."
	uv run python -c "from streamlit_app import process_all_documents; from pathlib import Path; files = list(Path('Data').iterdir()); process_all_documents(files[:5])"

# Check system requirements
check:
	@echo "🔍 Checking system requirements..."
	@echo "Python version:"
	@python3 --version
	@echo "UV version:"
	@uv --version
	@echo "Project dependencies:"
	@uv tree --depth 1
