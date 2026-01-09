"""
Utility functions for date and time operations in the todo application.
"""
from datetime import datetime, date
from typing import Union
import re


def parse_date(date_str: str) -> datetime:
    """
    Parse a date string into a datetime object.
    
    Supports multiple formats:
    - YYYY-MM-DD
    - MM/DD/YYYY
    - DD/MM/YYYY
    - YYYY-MM-DD HH:MM
    - MM/DD/YYYY HH:MM
    - DD/MM/YYYY HH:MM
    
    Args:
        date_str: Date string to parse
        
    Returns:
        datetime object
        
    Raises:
        ValueError: If the date string format is not recognized
    """
    if not date_str or not isinstance(date_str, str):
        raise ValueError("Date string must be a non-empty string")
    
    # Remove extra whitespace
    date_str = date_str.strip()
    
    # Define supported formats
    formats = [
        "%Y-%m-%d %H:%M",
        "%m/%d/%Y %H:%M",
        "%d/%m/%Y %H:%M",
        "%Y-%m-%d",
        "%m/%d/%Y",
        "%d/%m/%Y"
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    
    raise ValueError(f"Unable to parse date string '{date_str}'. Supported formats: YYYY-MM-DD, MM/DD/YYYY, DD/MM/YYYY, and variations with time")


def is_overdue(due_date: Union[datetime, date], completed: bool = False) -> bool:
    """
    Check if a task is overdue.
    
    Args:
        due_date: The due date of the task
        completed: Whether the task is completed
        
    Returns:
        True if the task is overdue, False otherwise
    """
    if completed or due_date is None:
        return False
    
    # Convert date to datetime if needed (assuming end of day for date-only)
    if isinstance(due_date, date) and not isinstance(due_date, datetime):
        due_date = datetime.combine(due_date, datetime.max.time())
    
    return due_date < datetime.now()


def compare_dates(date1: Union[datetime, date], date2: Union[datetime, date]) -> int:
    """
    Compare two dates.
    
    Args:
        date1: First date to compare
        date2: Second date to compare
        
    Returns:
        -1 if date1 < date2, 0 if equal, 1 if date1 > date2
    """
    # Convert date objects to datetime if needed
    if isinstance(date1, date) and not isinstance(date1, datetime):
        date1 = datetime.combine(date1, datetime.min.time())
    if isinstance(date2, date) and not isinstance(date2, datetime):
        date2 = datetime.combine(date2, datetime.min.time())
        
    if date1 < date2:
        return -1
    elif date1 > date2:
        return 1
    else:
        return 0


def format_datetime(dt: datetime) -> str:
    """
    Format a datetime object to a readable string.
    
    Args:
        dt: Datetime object to format
        
    Returns:
        Formatted date string
    """
    return dt.strftime("%Y-%m-%d %H:%M")


def add_interval_to_date(base_date: datetime, frequency: str, interval: int) -> datetime:
    """
    Add an interval to a date based on the frequency.
    
    Args:
        base_date: Base date to add interval to
        frequency: Frequency of recurrence ('daily', 'weekly', 'monthly', 'yearly')
        interval: Interval multiplier
        
    Returns:
        New datetime after adding the interval
    """
    if frequency == "daily":
        return base_date.replace(day=base_date.day + interval)
    elif frequency == "weekly":
        return base_date.replace(day=base_date.day + (interval * 7))
    elif frequency == "monthly":
        # Handle month overflow
        new_month = base_date.month + interval
        new_year = base_date.year
        while new_month > 12:
            new_month -= 12
            new_year += 1
        return base_date.replace(year=new_year, month=new_month)
    elif frequency == "yearly":
        return base_date.replace(year=base_date.year + interval)
    else:
        raise ValueError(f"Unsupported frequency: {frequency}")