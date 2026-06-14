list_one = [1,2,3,4,5]
list_two = [6,7,8,9,10]
list_three = [1,2,3,4,5]

list_one.append(list_two)
list_three.extend(list_two)

print(list_one)
print(list_three)