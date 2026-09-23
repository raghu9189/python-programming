class Person:
    def __init__(self, Name):
        self.Name = Name

class Student(Person):
    def __init__(self, Name, Age, avgMarks):
        super().__init__(Name)  # calling parent constructor
        self.Age = Age
        self.avgMarks = avgMarks

s1 = Student("Raghu", 20, 35)
print(s1.Age, s1.avgMarks, s1.Name)
# | Inheritance                          | Description                                                       |
# | ------------------------------------ | ----------------------------------------------------------------- |
# | **Single Inheritance**               | One child, one parent                                             |
# | **Multiple Inheritance**             | One child, multiple parents (not supported in many other languages) |
# | **Multilevel Inheritance**           | A → B → C (chain of inheritance)                                  |
# | **Hierarchical Inheritance**         | One parent, multiple children                                     |
# | **Hybrid Inheritance**               | Combination of multiple inheritance types                         |
# | **Method Resolution Order (MRO)**    | The order in which Python searches for methods in inheritance chains |
# | **`super()` Function**               | Used to call parent class methods                                |
# | **`isinstance()` and `issubclass()`** | Built-in functions to check class relationships                    |