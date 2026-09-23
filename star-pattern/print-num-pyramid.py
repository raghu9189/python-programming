# print this pyramid

# 1
# 12
# 123
# 1234
# 12345

n = 5

for i in range(1, n+1, 1):
    for j in range(1, i+1, 1):
        print(j, end="")
    print("\n")

for i in range(1, n+1, 1):
    for j in range(1, i+1, 1):
        print(i, end="")
    print("\n")