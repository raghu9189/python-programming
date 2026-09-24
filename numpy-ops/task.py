
# Try to find:
# Total sales
# Average sales
# Highest sales
# Lowest sales
# Sales greater than ₹20,000
# Number of days with sales greater than ₹20,000
# Sales between ₹10,000 and ₹25,000
# Standard deviation
# Sort the sales
# Create a new array where every sale has a 10% increase

import numpy as np

sales = np.array([12000, 18000, 9000, 25000, 32000, 15000, 28000])


# Total sales
total_sales = sales.sum()
print("Total Sales: ",total_sales)

# Average sales
avg_sales = sales.mean()
print("avg Sales: ",avg_sales)

# Highest sales
highest_sales = sales.max()
print("Highest Sales: ",highest_sales)

# Lowest sales
lowest_sales = sales.min()
print("Lowest Sales: ",lowest_sales)

# Sales greater than ₹20,000
print("Sales greater than ₹20,000: ", sales[sales > 20_000])

# Sales between ₹10,000 and ₹25,000
print("Sales between ₹10,000 and ₹25,000: ", sales[(sales > 10_000) & (sales < 25_000)])

# Standard deviation
print("# Standard deviation: ", sales.std())

# Sort the sales
print("Sort the sales: ", np.sort(sales))
