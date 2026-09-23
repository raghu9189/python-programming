class Student:
    school: str = "NSV"
    def __init__(self, name):
        self.name = name

st_1 = Student("Raghu")
st_2 = Student("Ramya")
print(st_1.name)
print(st_2.name)
print(Student.school)
