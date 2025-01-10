# Writing in a JSON File

import json

# Writing to JSON File

data = {"name": "John", "age": 30, "city": "New York"}
with open("output4.json", "w") as json_file:
    json.dump(data, json_file, indent=4)
