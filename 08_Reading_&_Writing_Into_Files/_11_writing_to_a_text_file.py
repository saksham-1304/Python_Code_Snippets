# Writing to a text file

lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output2.txt", "w") as file:
    file.writelines(lines)
