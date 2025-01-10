# Reading a JOSN File

import json

# Reading JSON file
with open("data.json", "r") as json_file:
    data = json.load(json_file)
    print(data)
