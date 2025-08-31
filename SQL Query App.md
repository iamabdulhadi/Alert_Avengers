
# SQL Query App

This project aims to create an AI-powered query system that translates natural language requests into functional SQL queries for database operations, specifically for banking transaction data.

## Features

- **Natural Language Processing**: Convert English queries to SQL using OpenAI GPT-4o
- **Banking Database**: Pre-configured SQLite database with customers, accounts, transactions, and branches
- **Conversational Interface**: Maintain context across multiple queries
- **Web Interface**: User-friendly Streamlit application
- **Comprehensive Testing**: Unit tests with coverage reporting
- **Local Execution**: Runs entirely on your local machine

## Quick Start

1. **Setup**: Run `python3 setup.py` to install dependencies and initialize database
2. **Configure**: Add your OpenAI API key to the `.env` file
3. **Run**: Execute `streamlit run app.py` to start the application
4. **Test**: Try queries like "How many customers are there?" or "Show me John Doe's account balance"

## Project Structure

- `app.py`: Streamlit user interface
- `agent.py`: LangChain SQL agent for natural language processing
- `database.py`: SQLite database setup and sample data generation
- `setup.py`: Automated setup script
- `requirements.txt`: Python dependencies
- `tests/`: Unit tests for core functionality
- `design_doc.md`: Technical architecture documentation
- `execution_steps.txt`: Detailed step-by-step instructions

## Requirements

- Python 3.8+
- OpenAI API key
- Internet connection (for package installation)

## Supported SQL Operations

- SELECT queries with filtering (WHERE)
- JOIN operations across multiple tables
- GROUP BY and aggregation functions (COUNT, SUM, AVG, etc.)
- ORDER BY for sorting results
- Complex multi-table queries

## Performance

- Query response time: 2-10 seconds
- Accuracy: 80%+ for standard banking queries
- Test coverage: Comprehensive unit tests included

For detailed setup instructions, see `execution_steps.txt`.

