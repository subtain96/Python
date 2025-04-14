#  Write a python program to print the contents of a directory using OS module. Search online for the function which does that.
# Program to list contents of a directory using os module

import os

def list_directory_contents(path="."):
    """
    This function lists all files and directories in the specified path.
    If no path is provided, it lists the contents of the current directory.
    """
    try:
        print(f"\nContents of directory: '{os.path.abspath(path)}'")
        print("-" * 50)
        
        # Get list of all entries in the directory
        entries = os.listdir(path)
        
        # Print each entry
        for entry in entries:
            # Check if the entry is a file or directory
            if os.path.isfile(os.path.join(path, entry)):
                print(f"File: {entry}")
            elif os.path.isdir(os.path.join(path, entry)):
                print(f"Directory: {entry}")
                
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Usage example
if __name__ == "__main__":
    # List current directory contents (default)
    list_directory_contents()
    
    # You can also specify a different path like this:
    # list_directory_contents("C:/Users/YourName/Documents")