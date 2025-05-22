#!/usr/bin/env python3
"""
JSON Log Message Analyzer

**LLM generated, not reviewed**

This script reads all JSON files in a given directory and provides a summary
showing each unique "log_message" value and how many files contain each message.

Usage: python analyze_logs.py <directory_path>
"""

import json
import os
import sys
from pathlib import Path
from collections import Counter


def load_json_file(file_path):
    """Load and parse a JSON file, returning None if it fails."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Warning: Could not read {file_path}: {e}")
        return None


def get_log_message(json_data):
    """Extract the log_message from JSON data, returning None if not found."""
    if isinstance(json_data, dict) and 'log_message' in json_data:
        return json_data['log_message']
    return None


def analyze_json_files(directory_path):
    """
    Analyze JSON files in the given directory and count unique log_message values.
    """
    directory = Path(directory_path)
    
    if not directory.exists():
        print(f"Error: Directory '{directory_path}' does not exist.")
        return False
    
    if not directory.is_dir():
        print(f"Error: '{directory_path}' is not a directory.")
        return False
    
    # Find all JSON files
    json_files = list(directory.glob('*.json'))
    
    if not json_files:
        print(f"No JSON files found in '{directory_path}'.")
        return True
    
    print(f"Analyzing {len(json_files)} JSON files in '{directory_path}'")
    print("=" * 60)
    
    # Counter for log messages
    log_message_counts = Counter()
    files_processed = 0
    files_with_errors = 0
    files_without_log_message = 0
    
    # Process each JSON file
    for file_path in sorted(json_files):  # Sort for consistent processing order
        json_data = load_json_file(file_path)
        files_processed += 1
        
        if json_data is None:
            files_with_errors += 1
            continue
        
        log_message = get_log_message(json_data)
        
        if log_message is None:
            files_without_log_message += 1
        else:
            log_message_counts[log_message] += 1
    
    # Print summary statistics
    print(f"\nSUMMARY STATISTICS:")
    print(f"  Total JSON files: {len(json_files)}")
    print(f"  Files processed successfully: {files_processed - files_with_errors}")
    print(f"  Files with parsing errors: {files_with_errors}")
    print(f"  Files without 'log_message' key: {files_without_log_message}")
    print(f"  Files with 'log_message' key: {len(log_message_counts)}")
    print(f"  Unique log messages found: {len(log_message_counts)}")
    
    # Print detailed breakdown of log messages
    if log_message_counts:
        print(f"\nLOG MESSAGE BREAKDOWN:")
        print("-" * 60)
        
        # Sort by count (descending) then by message (ascending)
        sorted_messages = sorted(log_message_counts.items(), 
                               key=lambda x: (-x[1], x[0]))
        
        # Calculate the width needed for count column
        max_count = max(log_message_counts.values())
        count_width = len(str(max_count))
        
        for log_message, count in sorted_messages:
            # Truncate very long messages for display
            display_message = log_message
            if len(display_message) > 80:
                display_message = display_message[:77] + "..."
            
            print(f"  {count:>{count_width}} files: {display_message}")
        
        # Show percentage breakdown
        total_files_with_messages = sum(log_message_counts.values())
        print(f"\nPERCENTAGE BREAKDOWN:")
        print("-" * 60)
        
        for log_message, count in sorted_messages:
            percentage = (count / total_files_with_messages) * 100
            display_message = log_message
            if len(display_message) > 60:
                display_message = display_message[:57] + "..."
            
            print(f"  {percentage:5.1f}% ({count:>{count_width}} files): {display_message}")
    
    # Show files without log_message if any
    if files_without_log_message > 0:
        print(f"\nFILES WITHOUT 'log_message' KEY: {files_without_log_message}")
        if files_without_log_message <= 10:  # Only show individual files if not too many
            print("Files missing 'log_message':")
            for file_path in sorted(json_files):
                json_data = load_json_file(file_path)
                if json_data is not None and get_log_message(json_data) is None:
                    print(f"  - {file_path}")
    
    print("\n" + "=" * 60)
    print("Analysis completed successfully!")
    
    return True


def main():
    """Main function to handle command line arguments and run analysis."""
    if len(sys.argv) != 2:
        print("Usage: python analyze_logs.py <directory_path>")
        print("\nThis script will:")
        print("  1. Read all JSON files in the specified directory")
        print("  2. Count occurrences of each unique 'log_message' value")
        print("  3. Display a summary with counts and percentages")
        print("  4. Report files missing the 'log_message' key")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    
    print(f"Starting analysis of JSON files in directory: {directory_path}")
    
    success = analyze_json_files(directory_path)
    
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
