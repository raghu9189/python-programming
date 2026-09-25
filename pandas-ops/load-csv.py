import pandas as pd

data_obj = pd.read_csv('pandas-ops/csv_data.csv')
df = pd.DataFrame(data_obj)
# print(df.groupby("Department")[[ 'Salary']].mean())
print(df.info())

