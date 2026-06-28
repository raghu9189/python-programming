import random

names = ["ram", "raghu", "ramya", "saisri", "divya", "sita", "priya"]
majors = ["maths", "physics", "chemistry", "biology", "computer science", "electronics"]

def people_generator(count=0):
    for i in range(1, count+1):
        person = {
            "id": i,
            "name" : random.choice(names),
            "major" : random.choice(majors)
        }
        yield person

graduate_peple = people_generator(count=1000)

print(next(graduate_peple))
print(next(graduate_peple))
print(next(graduate_peple))
print(next(graduate_peple))
