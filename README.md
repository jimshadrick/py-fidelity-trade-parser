# Fidelity Trade Parser

This script processes trade data exported from Fidelity Investments, transforming and cleaning it into a more usable
format. It handles the specific formatting of Fidelity's export files and produces a standardized CSV output.

## Features

- Processes Fidelity trade export files (.csv format)
- Handles common data formatting issues
- Provides trade summary statistics
- Supports verbose logging for debugging
- Exports cleaned data to a new CSV file

## How It Works

The script follows this process flow:

### Data Parsing (parse_trade_data function):

- Skips initial blank lines in the input file
- Reads trade data using CSV DictReader
- Validates date formats to identify actual trade data
- Converts data types (strings to dates, numbers)
- Handles missing or empty values
- Standardizes trade actions (buy/sell)

### Trade Action Processing (get_trade_action function):

- Standardizes trade action descriptions
- Converts various "bought" and "sold" formats to consistent values
- Handles special cases like conversions

### Summary Report (get_trade_summary function):

- Counts total number of trades
- Separates buy and sell trades
- Tracks unique symbols traded

### CSV Output (write_trades_to_csv function):

- Writes processed data to a new CSV file
- Converts dates back to string format for CSV compatibility
- Maintains consistent field ordering

## Project Structure

- `app.py`: Contains the main Python script for parsing the file.
- `sample_import.csv`: A sample export file from Fidelity trade transactions.
- `sample_output.csv`: A sample reformatted file after cleanup and transformations.

## Requirements

- Python 3.6+
- No external dependencies required

## Setup Instructions

1. Clone the repository.
2. Install the necessary dependencies using `pip install -r requirements.txt`.

## Usage

Example:

```bash
python app.py input_file.csv output_file.csv
```

With verbose logging:

```bash
python script.py input_file.csv output_file.csv -v
```

## Additional Information

### Data Transformations

The script performs the following key transformations:

- Dates: Converts string dates to Python date objects (MM/DD/YYYY format)
- Quantities: Converts to absolute values and handles empty fields
- Monetary values: Converts string amounts to floats
- Trade actions: Standardizes various buying/selling descriptions

### Output Format

The processed CSV file includes the following fields:

- run_date: Trade execution date
- run_month: Month of trade
- run_year: Year of trade
- action: Standardized trade action (Bought/Sold/Conversion)
- symbol: Trading symbol
- description: Security description
- type: Trade type
- quantity: Number of shares/units
- price: Price per share/unit
- amount: Total transaction amount
- settlement_date: Trade settlement date

### Error Handling

The script includes error handling for common issues:

- File not found errors
- CSV parsing errors
- Date format validation
- Missing or malformed data fields

### Notes for Developers

- The script uses Python's built-in csv, datetime, and argparse modules
- Type hints are included for better code maintainability
- The code follows PEP 8 style guidelines
- The parse_trade_data function is designed to stop processing when it hits disclaimer text or invalid data
- All monetary values are converted to absolute values for consistency

## License

This project is licensed under the [MIT License](LICENSE).