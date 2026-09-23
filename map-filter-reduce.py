# map func
from pprint import pp
def square(x: int) -> int:
    return x * x

nums = [1,2,3,4,5,6,7]

squared_nums = map(square, nums)

print(list(squared_nums))

# filter 

def isEven(x: int) -> bool:
    return x%2 == 0

even_nums = filter(isEven, nums)

print(list(even_nums))

# convert celcius to fahrenheit
# Formula (36°C × 9/5) + 32 = 96.8°F

temparature_values = [0,20,36,37,44]

def c_to_f(x):
    return (x * 9/5) + 32

fahrenheit_values = list(map(c_to_f, temparature_values))
print("temparature F values ", fahrenheit_values)

# using lambda + map cube the numbers

cubed_nums = list(map(lambda x: x*x*x, nums))
print(cubed_nums)

# extracting len of strings 
fruits = ["appale", "banana", "kiwi", "pineapple"]

word_lens = list(map(len, fruits))
print(word_lens)

# use filter func to get only positive nums

integer_nums = [-2, -1, 0, 1, 2,3]

positive_nums = list(filter(lambda x: x>0, integer_nums))

print(positive_nums)

# use filter get passed students 
students = [
    {"name": "Alice", "grade": 92},
    {"name": "Bob", "grade": 42},     # Failed
    {"name": "Charlie", "grade": 35}, # Failed
    {"name": "Diana", "grade": 88},
    {"name": "Evan", "grade": 28},    # Failed
    {"name": "Fiona", "grade": 49},   # Failed (just missed)
    {"name": "George", "grade": 73},
]

passed_students = list(filter(lambda student: student["grade"] >= 50, students))
pp(passed_students)

# reduce func
from functools import reduce

sum_total = reduce(lambda x,y: x+y, nums, 0)
print(sum_total)


total_score = reduce(lambda x, student: student["grade"]+x, students, 0)
print(total_score)