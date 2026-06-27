"""
Basic Type Hints in Python

Type hints (or type annotations) allow you to specify the expected types of variables, 
function arguments, and return values. They don't enforce types at runtime, but they 
help with static analysis tools (like mypy) and IDE autocompletion.
"""

# 1. Variable Type Hints
# You can specify the type of a variable by adding a colon and the type after the variable name.
age: int = 25
name: str = "Alice"
is_student: bool = True
pi_value: float = 3.14

# 2. Function Type Hints
# Specify argument types with `: type` and the return type with `-> type`.
def greet(person: str) -> str:
    return f"Hello, {person}!"

def add_numbers(a: int, b: int) -> int:
    return a + b

# 3. Collections (Lists, Dictionaries, Sets, Tuples)
# In Python 3.9+, you can use the standard collection types directly for hinting.
# For older Python versions, you would import these from the `typing` module (e.g., `from typing import List, Dict`).

# A list containing only integers
scores: list[int] = [95, 82, 100, 75]

# A dictionary with string keys and integer values
student_ages: dict[str, int] = {"Alice": 25, "Bob": 22}

# A set of strings
unique_names: set[str] = {"Alice", "Bob", "Charlie"}

# A tuple containing exactly a string followed by an integer
person_info: tuple[str, int] = ("Alice", 25)

# A tuple containing a variable number of integers
coordinates: tuple[int, ...] = (1, 2, 3, 4, 5)

if __name__ == "__main__":
    print(greet(name))
    print(f"Adding 5 and 10: {add_numbers(5, 10)}")
