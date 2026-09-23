# find factorial of x
# 5! = 1 x 2 x 3 x 4 x 5

n = 5
fact = 1

for i in range(1, n+1, 1):
    fact = fact * i

print(fact)
