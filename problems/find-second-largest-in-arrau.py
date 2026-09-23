# find 2nd largest in the array
# using sorted method
arr = [9,0,1,3,2,7,4]
second_largest = sorted(arr, reverse=True)[1]
print(second_largest)