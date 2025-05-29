# EY AI Challenge Deadline Manager - Development Scripts

# Activate the virtual environment
alias activate="source .venv/bin/activate"

# Run the Streamlit app
alias run-app="/home/guilhermegrancho/.local/bin/uv run streamlit run streamlit_app.py"

# Run tests
alias test="/home/guilhermegrancho/.local/bin/uv run pytest test_agent.py -v"

# Run the test suite
alias test-suite="/home/guilhermegrancho/.local/bin/uv run python test_streamlit_app.py"

# Format code with black
alias format="/home/guilhermegrancho/.local/bin/uv run black *.py"

# Lint code with flake8
alias lint="/home/guilhermegrancho/.local/bin/uv run flake8 *.py"

# Type check with mypy
alias typecheck="/home/guilhermegrancho/.local/bin/uv run mypy *.py"

# Install new dependencies
alias add-dep="/home/guilhermegrancho/.local/bin/uv add"

# Install new dev dependencies
alias add-dev="/home/guilhermegrancho/.local/bin/uv add --dev"

# Show dependencies
alias show-deps="/home/guilhermegrancho/.local/bin/uv tree"

# Update all dependencies
alias update-deps="/home/guilhermegrancho/.local/bin/uv sync --upgrade"

echo "🧠 EY AI Challenge Deadline Manager - Development Environment Ready!"
echo ""
echo "Available commands:"
echo "  run-app      - Start the Streamlit application"
echo "  test         - Run pytest tests"
echo "  test-suite   - Run full test suite"
echo "  format       - Format code with black"
echo "  lint         - Lint code with flake8"
echo "  typecheck    - Type check with mypy"
echo "  add-dep      - Add new dependency"
echo "  add-dev      - Add new dev dependency"
echo "  show-deps    - Show dependency tree"
echo "  update-deps  - Update all dependencies"
echo ""
echo "🚀 Quick start: run-app"
