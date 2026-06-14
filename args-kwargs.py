# unpacking arguments when u dont know how many no. of 

def sum(*vars):
    sum = 0
    for i in vars:
        sum += i
    print(sum)

sum(1,2,3)

def mul(**vars):
    for k, v in vars.items():
        print(k, v)

mul(var=2, var2=3, var3=4)