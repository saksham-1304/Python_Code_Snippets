# Writing in a Excel file

import pandas as pd

# Creating DataFrame
data = {"Name": ["John", "Alice", "Bob"], "Age": [30, 25, 35]}
df = pd.DataFrame(data)

# Writing to Excel file
df.to_excel("output5.xlsx", index=False)
