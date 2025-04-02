def read_and_write_file():
    try:
        filename = input("Enter the filename to read: ")
        with open(filename, 'r') as file:
            content = file.read()
            print("File read successfully!")

        # Modify the content (e.g., converting to uppercase)
        modified_content = content.upper()

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
            print(f"Modified content written to {new_filename}!")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You don't have permission to read/write the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the function
read_and_write_file()