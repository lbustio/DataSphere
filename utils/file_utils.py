import os
import fnmatch

def parse_gitignore(gitignore_path):
    """Parse the .gitignore file to get patterns for ignoring files and directories."""
    ignore_patterns = []
    try:
        with open(gitignore_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):  # Skip empty lines and comments
                    ignore_patterns.append(line)
    except FileNotFoundError:
        print(f"Warning: '.gitignore' not found in {gitignore_path}.")
    return ignore_patterns

def should_ignore(path, ignore_patterns):
    """Check if the path matches any ignore pattern."""
    relative_path = os.path.relpath(path, start=os.getcwd())
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(relative_path, pattern):
            return True
    return False

def print_directory_structure(path, ignore_patterns, indent=0, prefix=""):
    """
    Prints the directory structure of the given path, excluding paths in the .gitignore file.

    Args:
        path (str): The directory path to start printing.
        ignore_patterns (list): Patterns to exclude from printing.
        indent (int): The indentation level for nested directories.
        prefix (str): The prefix for the current line to show the connection.
    """
    try:
        # List all files and directories in the current path
        entries = os.listdir(path)
        entries.sort()  # Optional: sort entries to make the output consistent

        # Filter out entries based on ignore patterns
        filtered_entries = []
        for entry in entries:
            full_path = os.path.join(path, entry)
            if not should_ignore(full_path, ignore_patterns):
                filtered_entries.append(entry)
        
        # Loop through entries and print them with indentation
        for i, entry in enumerate(filtered_entries):
            full_path = os.path.join(path, entry)
            is_last = i == len(filtered_entries) - 1
            connector = "└── " if is_last else "├── "
            new_prefix = prefix + ("    " if is_last else "│   ")

            if os.path.isdir(full_path):
                print(prefix + connector + f'[{entry}/]')
                # Recursively print the structure of the subdirectory
                print_directory_structure(full_path, ignore_patterns, indent + 4, new_prefix)
            else:
                print(prefix + connector + f'{entry}')
    except PermissionError:
        print(prefix + "└── [Permission Denied]")
    except FileNotFoundError:
        print(prefix + "└── [File Not Found]")