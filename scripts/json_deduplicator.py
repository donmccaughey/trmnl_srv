#!/usr/bin/env python3
"""
JSON Log File Deduplicator

**LLM generated, not reviewed**

This script reads all JSON files in a given directory and keeps only one representative
file for each unique "log_message" value, deleting the duplicates.

Usage: python deduplicate_logs.py <directory_path>
"""

import json
import os
import sys
from pathlib import Path
from collections import defaultdict


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


def deduplicate_json_files(directory_path):
    """
    Deduplicate JSON files in the given directory based on log_message values.
    Keeps the first occurrence of each unique log_message and deletes the rest.
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
    
    print(f"Found {len(json_files)} JSON files in '{directory_path}'")
    
    # Dictionary to track unique log messages and their first occurrence
    unique_messages = {}  # log_message -> file_path
    files_to_delete = []
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
            print(f"Warning: No 'log_message' found in {file_path}")
            continue
        
        if log_message in unique_messages:
            # This is a duplicate - mark for deletion
            files_to_delete.append(file_path)
            print(f"Duplicate found: {file_path} (same log_message as {unique_messages[log_message]})")
        else:
            # This is the first occurrence - keep it
            unique_messages[log_message] = file_path
            print(f"Keeping: {file_path} (log_message: '{log_message}')")
    
    # Summary before deletion
    print(f"\nProcessing Summary:")
    print(f"  Files processed: {files_processed}")
    print(f"  Files with errors: {files_with_errors}")
    print(f"  Files without log_message: {files_without_log_message}")
    print(f"  Unique log messages found: {len(unique_messages)}")
    print(f"  Duplicate files to delete: {len(files_to_delete)}")
    
    # Delete duplicate files
    if files_to_delete:
        print(f"\nDeleting {len(files_to_delete)} duplicate files...")
        deleted_count = 0
        
        for file_path in files_to_delete:
            try:
                file_path.unlink()
                deleted_count += 1
                print(f"Deleted: {file_path}")
            except OSError as e:
                print(f"Error deleting {file_path}: {e}")
        
        print(f"\nSuccessfully deleted {deleted_count} duplicate files.")
        print(f"Remaining files: {len(json_files) - deleted_count}")
    else:
        print("\nNo duplicate files found - nothing to delete.")
    
    return True


def main():
    """Main function to handle command line arguments and run deduplication."""
    if len(sys.argv) != 2:
        print("Usage: python deduplicate_logs.py <directory_path>")
        print("\nThis script will:")
        print("  1. Read all JSON files in the specified directory")
        print("  2. Keep only one file for each unique 'log_message' value")
        print("  3. Delete duplicate files (keeping the first occurrence)")
        print("\nWARNING: This script will permanently delete files!")
        print("Make sure you're running this on a copy of your data.")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    
    print(f"Starting deduplication process for directory: {directory_path}")
    print("WARNING: This will permanently delete duplicate files!")
    
    # Ask for confirmation
    response = input("Are you sure you want to continue? (yes/no): ").lower().strip()
    if response not in ['yes', 'y']:
        print("Operation cancelled.")
        sys.exit(0)
    
    success = deduplicate_json_files(directory_path)
    
    if success:
        print("\nDeduplication completed successfully!")
    else:
        print("\nDeduplication failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()
