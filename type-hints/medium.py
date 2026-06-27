"""
Medium Type Hints in Python

These concepts cover more complex scenarios where a variable might have multiple types,
might be a function itself, or when you want to define your own custom type names.
"""
from typing import Any, Callable

# 1. Union Types (Multiple possible types)
# In Python 3.10+, you can use the `|` operator. 
# For older versions, use `from typing import Union` and `Union[int, str]`.
def process_id(item_id: int | str) -> str:
    return f"Processing ID: {item_id}"

# 2. Optional Types
# When a value can be of a specific type or `None`.
# `int | None` is equivalent to `Optional[int]` (from typing import Optional).
def find_user(username: str) -> str | None:
    if username == "admin":
        return "Admin User Found"
    return None

# 3. Any Type
# Use `Any` when a value can literally be of any type, essentially disabling type checking for it.
# Use sparingly, as it defeats the purpose of type hinting.
def print_anything(item: Any) -> None:
    print(item)

# 4. Callable Type (Functions as arguments)
# Used when a function accepts another function as an argument.
# Callable[[Arg1Type, Arg2Type], ReturnType]
def execute_operation(operation: Callable[[int, int], int], x: int, y: int) -> int:
    return operation(x, y)

def multiply(a: int, b: int) -> int:
    return a * b

# 5. Type Aliases
# You can assign complex types to a variable to make your code more readable.
# In Python 3.12+, you can use the `type` keyword: `type Point = tuple[float, float]`
Point = tuple[float, float]

def calculate_distance(p1: Point, p2: Point) -> float:
    # Dummy calculation for demonstration
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

# 6. Classes and `self`
class User:
    # Type hinting instance variables (attributes)
    username: str
    age: int

    def __init__(self, username: str, age: int) -> None:
        self.username = username
        self.age = age
    
    # You generally don't need to type hint `self`
    def get_info(self) -> str:
        return f"{self.username} is {self.age} years old"

if __name__ == "__main__":
    print(process_id(123))
    print(process_id("ABC-456"))
    print(execute_operation(multiply, 4, 5))
