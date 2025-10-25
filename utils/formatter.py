def format_currency(value: float)->str:
    """Format float to currency string with commas and 2 decimals."""
    return f"{value:,.2f}"

def print_header(title:str, width: int=50):
    """Print a consistent section header."""
    print("\n" + "="*width)
    print(f"{title.center(width)}")
    print("="*width)

def print_line(char:str = "-", width: int=50):
    """Print a divider line"""
    print(char*width)
    
