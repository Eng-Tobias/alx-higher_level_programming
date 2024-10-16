#!/usr/bin/python3
import os
import subprocess
import json

def clear_add_item_json():
    """Clear the contents of add_item.json if it exists."""
    if os.path.exists('add_item.json'):
        os.remove('add_item.json')

def run_add_item(*args):
    """Run the 7-add_item.py script with the provided arguments."""
    command = ['./7-add_item.py'] + list(args)
    subprocess.run(command)

def read_add_item_json():
    """Read the contents of add_item.json and return as a list."""
    if not os.path.exists('add_item.json'):
        return []
    with open('add_item.json', 'r') as f:
        return json.load(f)

def test_add_item():
    """Run a series of tests for 7-add_item.py."""
    clear_add_item_json()  # Start fresh

    # Test 1: No arguments
    run_add_item()
    assert read_add_item_json() == [], "Failed: Expected [] for no arguments"

    # Test 2: Single argument
    run_add_item("Best")
    assert read_add_item_json() == ["Best"], "Failed: Expected ['Best']"

    # Test 3: Multiple arguments
    run_add_item("School", "89", "Python", "C")
    assert read_add_item_json() == ["Best", "School", "89", "Python", "C"], "Failed: Expected ['Best', 'School', '89', 'Python', 'C']"

    # Test 4: No arguments again
    run_add_item()
    assert read_add_item_json() == ["Best", "School", "89", "Python", "C"], "Failed: Expected ['Best', 'School', '89', 'Python', 'C']"

    print("All tests passed!")

if __name__ == "__main__":
    test_add_item()
