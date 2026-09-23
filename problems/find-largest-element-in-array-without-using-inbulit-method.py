# find-largest-element-in-array-without-using-inbulit-method

# with inbuilt method

items = [20,3,9,1,19,78,45,23,90]

max_item = max(items)

print("Max item ", max_item)

# without inbuilt method

max_item_2 = items[0]

for item in items:
    if item > max_item_2:
        max_item_2 = item

print(max_item_2)
