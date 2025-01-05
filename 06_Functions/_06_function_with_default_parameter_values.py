# Function with default parameter values


def greet_person(name, greeting="Hello"):
    """
    Greeting a person with a custom greeting.
    Args:
    name(str):The name of the person to greet.
    greeting(str,optional):The greeting to use.Default is "Hello"

    Returns:
    None
    """
    print(f"{greeting},{name}!")


# Calling the function with and without a custom greeting
greet_person("Alice")  # Output:Hello,Alice!
greet_person("Bob", "Hi")  # Output:Hi,Bob!
