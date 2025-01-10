# Using the os package

import os


def get_text_file_metadata(file_path):
    if os.path.exists(file_path):
        # Get file metadata
        file_metadata = {
            "File Name": os.path.basename(file_path),
            "File Size (bytes)": os.path.getsize(file_path),
            "Creation Time": os.path.getctime(file_path),
            "Last Modified Time": os.path.getmtime(file_path),
        }
        return file_metadata
    else:
        return None


# Example usage
test_file_path = "08_Reading_&_Writing_Into_Files/example.txt"
text_metadata = get_text_file_metadata(test_file_path)
if text_metadata:
    print("Metadata for text file:")
    for key, value in text_metadata.items():
        print(f"{key}:{value}")

else:
    print("File not found!")
