def sayHello() -> str:
    return "Hello"

myDict: dict[str, str] = {
    "name": "raghu",
    "age": 34
}

def printDict() -> dict[str, str]:
    return {
    "name": "raghu",
    "age": 34
    }

print(sayHello(), myDict)