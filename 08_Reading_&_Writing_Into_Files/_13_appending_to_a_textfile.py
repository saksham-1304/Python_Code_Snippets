# Appending to a text file

new_lines = ["Additional Line1\n", "Additional Line 2\n"]
with open("output1.txt", "a") as file:
    file.writelines(new_lines)
