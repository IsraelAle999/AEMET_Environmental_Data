#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 15:54:02 2025

@author: israelale
"""

from datetime import datetime, timedelta

def split_date_range(start_date_str, end_date_str, max_months=6):
    """
    Split a date range into subranges of at most 'max_months' months
    """
    # Convert strings to datetime objects
    start_date = datetime.strptime(start_date_str.split('T')[0], '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str.split('T')[0], '%Y-%m-%d')
    
    date_ranges = []
    current_start = start_date
    
    while current_start < end_date:
        # Calculate end date of the subrange (6 months after current_start or end_date, whichever is earlier)
        if max_months == 6:
            # If we want to advance exactly 6 months
            month = current_start.month + 6
            year = current_start.year
            if month > 12:
                month -= 12
                year += 1
            # Adjust day to avoid issues with months of different lengths
            day = min(current_start.day, 28)  # Use 28 to avoid February issues
            current_end = datetime(year, month, day)
        else:
            # If using a different number of months
            current_end = current_start + timedelta(days=30 * max_months)
        
        # Ensure it does not exceed the original end date
        current_end = min(current_end, end_date)
        
        # Format dates as strings in the required format
        current_start_str = current_start.strftime('%Y-%m-%d') + 'T00:00:00UTC'
        current_end_str = current_end.strftime('%Y-%m-%d') + 'T23:59:59UTC'
        
        # Add the range to the list
        date_ranges.append((current_start_str, current_end_str))
        
        # Move to the next period
        current_start = current_end + timedelta(days=1)
    
    return date_ranges