from statistics import mean, median, mode, variance, stdev

elements = [ 20, 23, 28, 19, 25, 26 , 23, 23, 22, 25]

min_value = min(elements)
max_value = max(elements)

# measures of central tendency
count = len(elements)
mean_value = mean(elements)
median_value = median(elements)
mode_value = mode(elements)

# measures of variability (despersion)
range_value = max_value - min_value
variance_value = variance(elements, mean_value)
standard_deviation = stdev(elements, mean_value)

print(f" no. of elements {count}")

print("measures of central tendency")
print(f" Average value {mean_value}")
print(f" Center value {median_value}")
print(f" Most repeated value {mode_value}")

print("measures of variability (despersion)")
print(f" Range {range_value}")
print(f" Variance value {variance_value}")
print(f" Standard Deviation {standard_deviation}")