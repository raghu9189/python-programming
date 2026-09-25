import pandas as pd

result = pd.read_excel('pandas-ops/data.xlsx')
df = pd.DataFrame(result)

print(df.groupby('Department')['Salary'].mean().sort_values(ascending=False))

