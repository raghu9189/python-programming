# this is class 

class Phone:
    ram = "8GB" # class variable
    
    def __init__(self, brand, price):
        self.brand = brand # instance variable
        self.price = price # instance variable
        pass

p1 = Phone("Iphone", 120000)
p2 = Phone("Samsung", 120000)

# print(id(p1))
# print(id(p2))
print(p1.brand)
print(p2.brand)
p1.price = 130000
p2.price = 140000
print(p1.price)
print(p2.price)
# p1.ram = "8GB"
Phone.ram = "12GB"
print(p1.ram)
print(f"p2 {p2.ram}" )

# | Concept                      | Meaning                                                                                                   |
# | ---------------------------- | --------------------------------------------------------------------------------------------------------- |
# | **Class**                    | Blueprint for creating objects                                                                            |
# | **Object**                   | Instance created from a class                                                                             |
# | **Constructor (`__init__`)** | Automatically initializes an object when it's created                                                     |
# | **`self`**                   | Reference to the current object                                                                           |
# | **Instance Variable**        | Belongs to one specific object (`self.variable`)                                                          |
# | **Class Variable**           | Shared by all objects; defined in the class body                                                          |
# | **Static Variable**          | Another name commonly used for a class variable in Python; there is no separate `static` variable keyword |

