def modify_content(content):
    """Modify file content by converting it to uppercase."""
    return content.upper()

try:
    # Ask the user for the input filename
    input_file = input("Enter the name of the file to read: ")

    # Open and read the file
    with open(input_file, "r") as file:
        data = file.read()

    # Modify the file content
    modified_data = modify_content(data)

    # Ask for the output file name
    output_file = input("Enter the name for the new modified file: ")

    # Write modified content to a new file
    with open(output_file, "w") as new_file:
        new_file.write(modified_data)

    print("🎉 File has been successfully read, modified, and saved as:", output_file)

except FileNotFoundError:
    print("Error: The file you entered does not exist.")
except PermissionError:
    print("Error: You don't have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
