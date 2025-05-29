# EY AI Challenge Deadline Manager - API Documentation

## Project Structure

```
ey-deadline-manager/
├── src/ey_deadline_manager/           # Main package
│   ├── __init__.py                    # Package initialization
│   ├── app/                           # Streamlit web application
│   │   ├── __init__.py
│   │   └── streamlit_app.py          # Main Streamlit app
│   ├── core/                          # Core business logic
│   │   ├── __init__.py
│   │   └── deadline_agent_backend.py # Deadline processing logic
│   ├── utils/                         # Utility functions
│   │   └── __init__.py
│   └── models/                        # Data models
│       └── __init__.py
├── tests/                             # Test files
│   ├── __init__.py
│   ├── test_agent.py                 # Core logic tests
│   └── test_streamlit_app.py         # App tests
├── docs/                              # Documentation
├── notebooks/                         # Jupyter notebooks
│   └── AutoCalendarAgent.ipynb       # Development notebook
├── data/                              # Sample data files
├── scripts/                           # Utility scripts
│   ├── dev-setup.sh                  # Development setup
│   ├── dev-workflow.sh               # Workflow guide
│   └── start.sh                      # Application launcher
├── config/                            # Configuration files
│   ├── .env.example                  # Environment template
│   └── .pre-commit-config.yaml       # Pre-commit hooks
└── reports/                           # Project reports
    ├── EY_Challenge_Results.md
    ├── FINAL_COMPLETION_REPORT.md
    └── other reports...
```

## Core Modules

### ey_deadline_manager.core.deadline_agent_backend

The core business logic module containing:

- `DeadlineManagerAgent`: Main agent class for deadline processing
- `add_working_days()`: Calculate working days with Portuguese holidays
- `apply_portuguese_tax_rules()`: Apply Portuguese tax-specific deadline rules
- `process_with_gemini_ai()`: AI-powered deadline extraction

### ey_deadline_manager.app.streamlit_app

The Streamlit web application providing:

- Multi-modal document processing (PDF, DOCX, images)
- Interactive deadline calendar
- AI-powered deadline extraction
- Portuguese tax law compliance
- Analytics dashboard

## Development Workflow

### Quick Start
```bash
# Install dependencies
make dev-install

# Setup git hooks
make setup-hooks

# Run the application
make run

# Run tests
make test

# Code quality
make lint
make format
```

### Environment Management with UV
```bash
# Sync dependencies
uv sync

# Add new dependency
uv add <package>

# Run with uv
uv run streamlit run src/ey_deadline_manager/app/streamlit_app.py
```

### Code Quality with Ruff
```bash
# Lint and auto-fix
uv run ruff check --fix

# Format code
uv run ruff format

# Check formatting
uv run ruff format --check
```

## Configuration

### Environment Variables
Copy `config/.env.example` to `config/.env` and configure:

- `GOOGLE_API_KEY`: Google Gemini AI API key
- Other configuration variables as needed

### Pre-commit Hooks
Pre-commit hooks are configured in `config/.pre-commit-config.yaml` and include:

- Ruff linting and formatting
- YAML/TOML validation
- Trailing whitespace removal
- MyPy type checking

## Testing

### Running Tests
```bash
# All tests
make test

# Specific test files
uv run pytest tests/test_agent.py -v
uv run python tests/test_streamlit_app.py
```

### Test Structure
- `tests/test_agent.py`: Core business logic tests
- `tests/test_streamlit_app.py`: Application integration tests

## Data Processing

### Supported Formats
- PDF documents
- Microsoft Word (.docx)
- Images (JPEG, PNG)
- Post-it notes and whiteboards

### Data Location
- Sample data: `data/` directory
- Processing results cached for performance

## Deployment

### Production Setup
```bash
# Install production dependencies only
make install

# Start application
make run
```

### Docker (if applicable)
```bash
# Build image
docker build -t ey-deadline-manager .

# Run container
docker run -p 8501:8501 ey-deadline-manager
```

## API Reference

### Main Functions

#### `process_with_gemini_ai(text, reference_date=None)`
Process text using Google Gemini AI for deadline extraction.

**Parameters:**
- `text` (str): Input text to process
- `reference_date` (datetime, optional): Reference date for calculations

**Returns:**
- Dict containing extracted deadline information

#### `add_working_days(start_date, days)`
Add working days to a date, accounting for Portuguese holidays.

**Parameters:**
- `start_date` (datetime): Starting date
- `days` (int): Number of working days to add

**Returns:**
- datetime: Calculated end date

#### `apply_portuguese_tax_rules(text, reference_date=None)`
Apply Portuguese tax law specific deadline rules.

**Parameters:**
- `text` (str): Input text containing deadline information
- `reference_date` (datetime, optional): Reference date

**Returns:**
- Dict with processed deadline information

## Contributing

### Code Style
- Use ruff for linting and formatting
- Follow PEP 8 conventions
- Add type hints where appropriate
- Write docstrings for public functions

### Development Process
1. Create feature branch
2. Write tests
3. Implement feature
4. Run `make lint` and `make test`
5. Submit pull request

### Git Hooks
Pre-commit hooks automatically:
- Run ruff linting and formatting
- Check YAML and TOML syntax
- Remove trailing whitespace
- Run type checking with MyPy

## Troubleshooting

### Common Issues

1. **Import errors**: Ensure `src/` is in Python path
2. **API key errors**: Configure Google API key in environment
3. **Dependency issues**: Run `uv sync` to update dependencies
4. **Port conflicts**: Use `--server.port` flag to change port

### Performance Tips

- Use cached results for repeated processing
- Process smaller document batches
- Monitor memory usage with large files

## License

MIT License - see LICENSE file for details.
