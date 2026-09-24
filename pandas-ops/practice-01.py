# Create a Pandas DataFrame using the above data.
# Display the complete DataFrame.
# Display the first 5 rows using head().
# Display the first 3 rows.
# Display the last 5 rows using tail().
# Display the last 2 rows.
# Find the number of rows and columns in the DataFrame.
# Display all column names.
# Display the data types of all columns.
# Display complete DataFrame information using info().
# Generate statistical summary using describe().
# Display only the Employee column.
# Display only the Salary column.
# Display Employee and Salary columns together.
# Display Employee, Department, and Salary columns.
# Display the first employee using iloc.
# Display the employee at index 2 using iloc.
# Display the first three rows using iloc.
# Display the last two rows using iloc.
# Display the employee at index 3 using loc.
# Display the Salary of the employee at index 2.
# Find the total salary of all employees.
# Find the average salary.
# Find the highest salary.
# Find the lowest salary.
# Find the average experience of all employees.
# Find the employee with the highest salary.
# Find the employee with the lowest salary.
# Find how many employees are present in the DataFrame.
# Find how many employees work in the IT department.

import pandas as pd

data = {
    "Employee": ["Ravi", "Priya", "Arjun", "Sneha", "Kiran"],
    "Department": ["IT", "HR", "IT", "Finance", "IT"],
    "Salary": [50000, 45000, 70000, 65000, 80000],
    "Experience": [2, 3, 5, 4, 7],
}

df = pd.DataFrame(data)
print(df)

# Display the first 5 rows using head().
print(df.head())

# Display the first 3 rows.
print(df.head(3))

# Display the last 5 rows using tail().
print(df.tail(5))

# Display the last 2 rows.
print(df.tail(2))

# Find the number of rows and columns in the DataFrame.
print(df.shape)

# # Display all column names.
print(df.columns)

# Display the data types of all columns.
print(df.dtypes)

# Display only the Employee column.
print(df['Employee'])

# Display only the Salary column.
print(df['Salary'])

# Display Employee and Salary columns together.
print(df[['Employee', 'Salary']])

# Display the first employee using iloc.
print(df.iloc[0])

# Display the first three rows using iloc.
print(df.iloc[0:3])

# Find the total salary of all employees.
print(df["Salary"].sum())

print(df["Salary"].mean())
print(df["Salary"].max())
print(df["Salary"].min())


