#!/bin/bash

# EY AI Challenge Deadline Manager - Startup Script
# This script sets up and runs the application with proper environment management

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if we're in the right directory
if [[ ! -f "streamlit_app.py" ]]; then
    print_error "streamlit_app.py not found. Please run this script from the project root directory."
    exit 1
fi

print_status "🧠 EY AI Challenge Deadline Manager - Startup"
echo ""

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    print_error "uv is not installed or not in PATH. Please install uv first:"
    echo "curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

UV_VERSION=$(uv --version)
print_success "Found uv: $UV_VERSION"

# Check if virtual environment exists
if [[ ! -d ".venv" ]]; then
    print_warning "Virtual environment not found. Creating one..."
    uv venv
    print_success "Virtual environment created"
fi

# Install dependencies
print_status "📦 Installing dependencies..."
uv sync
print_success "Dependencies installed"

# Check if .env file exists
if [[ ! -f ".env" ]]; then
    print_warning ".env file not found. Creating from template..."
    cp .env.example .env
    print_success ".env file created from template"
    print_warning "Please review and update .env file with your actual configuration"
fi

# Run basic tests
print_status "🧪 Running basic functionality tests..."
if uv run python -c "import streamlit, pandas, plotly, google.generativeai; print('All imports successful')"; then
    print_success "All dependencies are working correctly"
else
    print_error "Some dependencies are not working. Please check your installation."
    exit 1
fi

# Check if Data directory exists
if [[ ! -d "Data" ]]; then
    print_warning "Data directory not found. Some features may not work without sample documents."
else
    DATA_COUNT=$(find Data -type f | wc -l)
    print_success "Found $DATA_COUNT sample documents in Data directory"
fi

echo ""
print_success "✅ Setup complete! Ready to start the EY AI Deadline Manager"
echo ""
echo "🚀 Starting Streamlit application..."
echo ""

# Start the application
uv run streamlit run streamlit_app.py
