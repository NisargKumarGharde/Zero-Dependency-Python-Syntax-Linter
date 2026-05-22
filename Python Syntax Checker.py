import argparse

def check_python_syntax(filepath):
    '''
    Reads a Python script from the given filepath and checks its syntax.

    Args:
        filepath (str): The full path to the Python (.py) file.
    '''
    try:
        # Read the entire content of the script using file handling.
        with open(filepath, 'r') as file:
            script_content = file.read()

        # Use the compile() function to validate the syntax.
        # A try-except block is used to catch syntax errors. 
        try:
            compile(script_content, filepath, 'exec')
            # If no errors are found, display a success message. 
            print("\nSuccess! No Syntax Errors Found in '{}'.".format(filepath))
        except SyntaxError as e:
            # If a syntax error is detected, display the error message with the line number. 
            print("\nSyntax Error Found:")
            print("File: '{}'".format(e.filename))
            print("Line: {}".format(e.lineno))
            print("Error: {}".format(e.msg))

    except FileNotFoundError:
        print("\nError: The file '{}' was not found.".format(filepath))
    except Exception as e:
        print("\nAn unexpected error occurred: {}".format(e))

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Lightweight Python Syntax Linter")
    parser.add_argument(
        "-f", "--file", 
        required=True, 
        help="Path to the Python (.py) file to check"
    )
    
    args = parser.parse_args()
    check_python_syntax(args.file)
