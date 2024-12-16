import csv
from datetime import datetime
from typing import Dict, List, Union


def parse_trade_data(file_path: str) -> List[Dict[str, Union[str, float, None]]]:
    """
    Parse trade data from CSV file with specific formatting requirements.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        List[Dict]: List of dictionaries containing parsed trade data
    """
    trades = []

    with open(file_path, 'r', encoding='utf-8') as file:
        # Skip first two blank lines
        next(file)
        next(file)

        # Create CSV reader
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            # Validate that this is a trade data row by checking date format
            try:
                # First check if the Run Date field looks like a date
                date_str = row['Run Date'].strip()
                if not date_str or len(date_str.split('/')) != 3:
                    break  # Exit if we hit non-date data (like disclaimer text)

                # Process the row only if it passes date validation
                trade_dict = {
                    'run_date': datetime.strptime(date_str, '%m/%d/%Y').date(),
                    # 'action': row['Action'].strip(),
                    'run_month': datetime.strptime(date_str, '%m/%d/%Y').date().month,
                    'run_year': datetime.strptime(date_str, '%m/%d/%Y').date().year,
                    'action': get_trade_action(row['Action']),
                    'symbol': row['Symbol'].strip(),
                    'description': row['Description'].strip(),
                    'type': row['Type'].strip(),
                    'quantity': float(row['Quantity']) if row['Quantity'].strip() else None,
                    'price': float(row['Price ($)']) if row['Price ($)'].strip() else None,
                    'commission': float(row['Commission ($)']) if row['Commission ($)'].strip() else None,
                    'fees': float(row['Fees ($)']) if row['Fees ($)'].strip() else None,
                    'accrued_interest': float(row['Accrued Interest ($)']) if row[
                        'Accrued Interest ($)'].strip() else None,
                    'amount': float(row['Amount ($)']) if row['Amount ($)'].strip() else None,
                    # 'cash_balance': row['Cash Balance ($)'].strip(),
                    'settlement_date': datetime.strptime(row['Settlement Date'].strip(), '%m/%d/%Y').date() if row[
                        'Settlement Date'].strip() else None
                }
                trades.append(trade_dict)
            except (ValueError, KeyError):
                # If we hit any parsing errors, assume we've reached the end of the trade data
                break

    return trades


def get_trade_action(action: str) -> str:
    """Extract the core trade type from the action string."""
    action = action.upper()
    if 'BOUGHT' in action:
        return 'Bought'
    elif 'SOLD' in action:
        return 'Sold'
    elif 'CONVERSION' in action:
        return 'Conversion'
    # Add any other trade actions you want to capture
    else:
        return action  # or return some default value


def get_trade_summary(trades: List[Dict]) -> Dict:
    """
    Generate summary statistics from the trade data.
    
    Args:
        trades (List[Dict]): List of trade dictionaries
        
    Returns:
        Dict: Summary statistics
    """
    summary = {
        'total_trades': len(trades),
        'total_buy_trades': sum(1 for trade in trades if 'BOUGHT' in trade['action'].upper()),
        'total_sell_trades': sum(1 for trade in trades if 'SOLD' in trade['action'].upper()),
        'unique_symbols': len(set(trade['symbol'] for trade in trades)),
        'total_fees': sum(trade['fees'] for trade in trades if trade['fees'] is not None),
        'total_commission': sum(trade['commission'] for trade in trades if trade['commission'] is not None)
    }
    return summary


# Example usage:
if __name__ == "__main__":
    file_path = "sample_export.csv"
    trades = parse_trade_data(file_path)

    # Example of accessing the data
    print("\nFirst trade details:")
    if trades:
        first_trade = trades[0]
        for key, value in first_trade.items():
            print(f"{key}: {value}")

    # Get and print summary
    summary = get_trade_summary(trades)
    print("\nTrade Summary:")
    for key, value in summary.items():
        print(f"{key}: {value}")
