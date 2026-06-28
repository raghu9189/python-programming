class Parent:
    car = "BMW"
    
    def drive(self):
        print("Parent is driving")


class Child(Parent):
    car = "Audi"

    def drive(self):
        print("Child is driving")

ch1 = Child()

print(ch1.car)
print(ch1.drive())

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