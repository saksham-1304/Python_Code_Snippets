# Using the with statement

# Definr the file path

file_path = "example.txt"

# Open the file in read mode using 'with' statement
with open(file_path, "r") as file:
    # Read the contents of the file
    file_contents = file.read()

    # Process the file contents
    print("File Contents:")
    print(file_contents)

# After the 'with' block ,the file is automatically closed
