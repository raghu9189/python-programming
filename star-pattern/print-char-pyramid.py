# print this pyramid

# A
# AB
# ABC
# ABCD
# ABCDE

n = 5

for i in range(1, 6, 1):
    for j in range(1, i+1, 1):
        print(chr(j+64), end="")
    print(end="\n")

#     *
#    **
#   ***
#  ****
# *****

for row in range(1, n+1, 1):
    spaces = n - row
    stars = n - spaces
    print(" " * spaces + "*" * stars)

