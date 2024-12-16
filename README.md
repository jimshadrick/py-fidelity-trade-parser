# Python

This script includes several key features:

File Handling:

- Skips the first two blank lines
- Reads headers from line 3
- Stops at the first blank line after data

Data Cleaning:

- Strips whitespace from all fields
- Converts numeric fields to float where appropriate
- Converts dates to datetime.date objects
- Handles empty fields gracefully

Data Structure:

- Creates a list of dictionaries where each dictionary represents a trade
- Uses meaningful key names
- Maintains data types appropriate for each field

Additional Functionality:

- Includes a summary function to generate basic statistics about the trades
- Handles error cases and empty fields
- Uses type hints for better code documentation

## Project Structure

- `app.py`: Contains the main Python script for parsing the file.
- `sample_export.csv`: A sample export file from Fidelity trade transactions.

## Setup Instructions

1. Clone the repository.
2. Install the necessary dependencies using `pip install -r requirements.txt`.

## Usage

## Additional Information

## License

This project is licensed under the [MIT License](LICENSE).