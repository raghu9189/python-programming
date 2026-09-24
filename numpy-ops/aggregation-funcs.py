import numpy as np 

sales = np.array([100, 200, 300, 400, 500])

sum_total = np.sum(sales)
avg_total = np.mean(sales)
median_sales = np.median(sales)
min_value = np.min(sales)
max_value = np.max(sales)


# print(sum_total)


# The axis concept

sales = np.array([
    [100, 200, 300],
    [400, 500, 600]
])

print(np.sum(sales, axis=0)) # axis=0 → operate DOWN the rows → result for each column
print(np.sum(sales, axis=1)) # axis=1 → operate ACROSS the columns → result for each row

# Boolean filtering ⭐

print(sales[sales > 200])

# Sorting
print(np.sort(sales))

# Unique
print(np.unique(sales))
