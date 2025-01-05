# Recursive Functions


def factorial(n):
    """
    Calculates the factorial of a given number
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

# Output:120
