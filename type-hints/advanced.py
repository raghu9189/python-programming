"""
Advanced Type Hints in Python

These concepts cover generics, literal types, strongly typed dictionaries, 
and structural subtyping (protocols).
"""
from typing import TypeVar, Generic, Literal, TypedDict, Protocol, overload

# 1. Generics (TypeVar and Generic)
# Used when you want a class or function to operate on a type that is specified later.
T = TypeVar('T') # Declare a type variable 'T'

class Box(Generic[T]):
    def __init__(self, content: T) -> None:
        self.content = content
    
    def get_content(self) -> T:
        return self.content

# We can specify the type when creating the Box
int_box = Box[int](123)
str_box = Box[str]("Hello")

# 2. Literal Types
# Restricts a value to be exactly one of the provided literal values.
def move(direction: Literal["up", "down", "left", "right"]) -> None:
    print(f"Moving {direction}")

# move("forward") # This would raise a type checking error

# 3. TypedDict
# Used to type hint dictionaries that have a specific structure (fixed string keys and specific value types).
class UserProfile(TypedDict):
    name: str
    age: int
    is_active: bool

# This is just a standard dict at runtime, but type checkers ensure it has the correct keys/types.
user: UserProfile = {"name": "Alice", "age": 30, "is_active": True}

# 4. Protocols (Structural Subtyping / Duck Typing)
# A class satisfies a Protocol if it implements the methods/attributes defined in the Protocol,
# even if it doesn't explicitly inherit from it.
class Drawable(Protocol):
    def draw(self) -> None: ...

class Circle:
    def draw(self) -> None:
        print("Drawing a circle")

class Square:
    def draw(self) -> None:
        print("Drawing a square")

# This function accepts anything that has a `draw` method returning `None`.
def render_shape(shape: Drawable) -> None:
    shape.draw()

# Both Circle and Square implicitly satisfy the Drawable Protocol.
render_shape(Circle())
render_shape(Square())

# 5. Overloads
# Sometimes a function's return type depends on its argument types.
# You use @overload to define the different signatures. The actual implementation comes last without @overload.
@overload
def double(value: int) -> int: ...

@overload
def double(value: str) -> str: ...

def double(value: int | str) -> int | str:
    # At runtime, value can be int or str, and it returns int or str.
    # The overloads tell the type checker: if you pass an int, you get an int back.
    if isinstance(value, int):
        return value * 2
    return value + value

if __name__ == "__main__":
    move("up")
    print(double(10))     # Type checker knows this returns int
    print(double("Hi"))   # Type checker knows this returns str
