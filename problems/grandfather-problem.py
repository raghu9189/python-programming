# find the grandfather

person = "mike"
father = ""
grandfather = "grand father not found"
people = [
    ["mike", "paul"],
    ["ross", "jack"],
    ["tom", "robin"],
    ["jae", "paul"],
    ["paul", "michael"],
    ["robin", "ross"]
]

for i in people:
    if person == i[0]:
        father = i[1]
        # print(father)

for i in people:
    if father == i[0]:
        grandfather = i[1]

print(grandfather)