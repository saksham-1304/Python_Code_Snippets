# Scope of Variables

## Global variable
greeting = "Hello"


def greet(name):
    # Local variable
    message = f"{greeting},{name}!"
    print(message)


greet("Alice")  # Output:Hello,Alice!
print(message) # NameError: name 'message' is not defined

