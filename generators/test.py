nums = [1,2,3,4,5,6,7,8,9,10]

def square(nums):
    for n in nums:
        yield n*n


mySquareNums = square(nums)

# u can use for loop over it

for value in mySquareNums:
    print(value)


