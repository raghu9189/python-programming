# check wether 
word = "madam"

pali = ""
n = len(word) - 1

while (n >= 0):
    pali = pali + word[n]
    n = n - 1

if word == pali:
    print("Palindrome")
else:
    print("Not a Palindrome")