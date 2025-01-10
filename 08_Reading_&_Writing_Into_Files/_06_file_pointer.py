# File Pointer

# Open a file in read mode
file_path = "example.txt"
with open(file_path, "r") as file_pointer:
    # Print the type of file pointer
    print("Type of file pointer:", type(file_pointer))
    # Print the file pointer itself
    print("File pointer:", file_pointer)


"""
Output:
Type of file pointer: <class '_io.TextIOWrapper'>
File pointer: <_io.TextIOWrapper name='example.txt' mode='r' encoding='cp1252'>
"""
