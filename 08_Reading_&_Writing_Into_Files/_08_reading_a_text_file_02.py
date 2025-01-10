# Reading a text file

with open("example.txt", "r") as file:
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()
