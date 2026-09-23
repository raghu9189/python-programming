# basic file reading 

file = open('file-ops/sample.txt', mode="r", encoding="utf-8")
content = file.read()
file.close()
print(content)

# using context managers 

with open('file-ops/sample.txt', mode="r", encoding="utf-8") as f:
    print(f.read())

# reading specific number of chars from begining

with open('file-ops/sample.txt', mode="r", encoding="utf-8") as f:
    print(f.read(10)) # here specify

# reading specific number of lines from begining

with open('file-ops/sample.txt', mode="r", encoding="utf-8") as f:
    print(f.readlines(1)) # here specify