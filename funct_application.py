# TYPEHINTING: it add readability to the code
def sum(a: int, b: int) -> int:
    sum = a + b
    return sum

def greetings(name):
    return f"Guten Morgen {name}"

def say_hi(greet: str, name: str) -> str:
    return (f"{greet} {name}")

def say_hello(greet, name):
    return (greet, name )
