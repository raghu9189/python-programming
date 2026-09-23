# count uppercase and lowercase
word = "Elephant"

upper = 0
lower = 0

for ch in word:
    if ch.islower():
        lower = lower + 1
    
    if ch.isupper():
        upper = upper + 1

print("Uppercase ", upper, " Lower ", lower)