from typing import Literal, TypedDict, List, Optional

# type literals
MyType = Literal["a", "b", "c"]

myList: MyType = ["a", "b", "c"]
print(myList)

# type dict
class User(TypedDict):
    name: str
    age: int
    is_student: bool
    hobbies: List[str]
    userId: str | int # union type
    isHuman: Optional[None]

myUser: User = {
    "name": "Raghu",
    "age": 23,
    "is_student": True,
    "hobbies": ["cricket", "reading", "coding"],
    "userId": 1234567890,
    "isHuman": True
}

print(myUser)