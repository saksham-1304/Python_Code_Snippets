# Opening and Closing Files

try:
    file = open("example.txt", "r")
    # Perform file operations
    
except FileNotFoundError:
    print("File not found!")

except PermissionError:
    print("Permission denied!")

finally:
    file.close()
