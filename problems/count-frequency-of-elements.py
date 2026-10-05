l = [1,1,2,5,6,2,3,4,5]

d = {}

for i in l:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1

print(d)