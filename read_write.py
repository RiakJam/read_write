import os

def modify_content(content):
    """Modify file content by converting it to uppercase."""
    return content.upper()

try:
    # Get the directory where the script is located
    base_path = os.path.dirname(__file__)

    # Ask the user for the input filename
    input_file = input("Enter the name of the file to read: ")

    # Build the full path automatically
    input_path = os.path.join(base_path, input_file)

    # Open and read the file
    with open(input_path, "r") as file:
        data = file.read()

    # Modify the file content
    modified_data = modify_content(data)

    # Ask for the output file name
    output_file = input("Enter the name for the new modified file: ")
    output_path = os.path.join(base_path, output_file)

    # Write modified content to a new file
    with open(output_path, "w") as new_file:
        new_file.write(modified_data)

    print("File has been successfully read, modified, and saved as:", output_file)

except FileNotFoundError:
    print("Error: The file you entered does not exist.")
except PermissionError:
    print("Error: You don't have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
