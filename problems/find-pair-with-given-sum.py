# find pair with given sum
pairs = [11, 2, 15, 7]
target = 9

n = len(pairs)

for i in range(0, n, 1):
    # print(i)
    for j in range(i+1, n, 1):
        # print(pairs[i] + pairs[j])
        if pairs[i] + pairs[j] == target:
            print(i, j)
            break
        # break
