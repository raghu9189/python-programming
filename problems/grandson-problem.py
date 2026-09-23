# find the grandson

person = "ross"
son = ""
grandson = "grand son not found"
people = [
    ["mike", "paul"],
    ["ross", "jack"],
    ["tom", "robin"],
    ["jae", "paul"],
    ["paul", "michael"],
    ["robin", "ross"]
]

for pair in people:
    if person == pair[1]:
        son = pair[0]
        break
# print(son)

for pair in people:
    if son == pair[1]:
        grandson = pair[0]
        break

print(grandson)