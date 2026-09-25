# series
import pandas as pd
import numpy as np

# print pandas version
print(pd.__version__)

# A Series is basically a one-dimensional labeled data structure.
sales = pd.Series(
    [12000, 18000, 9000],
    index=["Jan", "Feb", "Mar"]
)

print(sales)
print(sales, sales['Feb'])
print(sales.sum())
print(sales.mean())
print(sales.max())
print(sales.min())

# This is where Pandas becomes really important for data analysis.
# A DataFrame is a 2-dimensional table.

data = {
    "Name": ["Ravi", "Suresh", "Anil", "Kiran"],
    "Age": [25, 30, 28, 35],
    "Salary": [45000, 60000, 52000, 75000]
}

df = pd.DataFrame(data)

print(df)

# Inspecting a DataFrame
# df.head()
print(df.head())
print(df.head(2))

# Last 5 rows
print(df.tail())

# df.shape
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

# Selecting Columns
print(df["Name"])

# Selecting Rows
print(df.loc[0])

matrix_1 = pd.DataFrame(np.arange(1, 10, 1).reshape(3, 3))

matrix_2 = pd.DataFrame(np.arange(1, 10, 1).reshape(3, 3))
concat_matrix = pd.concat([matrix_1, matrix_2], axis=1)
print(concat_matrix)
