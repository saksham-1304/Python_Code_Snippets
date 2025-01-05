# Function to square number


def square_number(num):
    """
    Calculates the square of a given number

    Args:
    num(int or float): The number to be squared.

    Returns:
    int or float: The square of the given number.
    """
    square = num**2
    return square


# Calling the function
original_num = 5
square_num = square_number(original_num)

# Using the returned value
print(f"The square of {original_num} is {square_num}")

# Output:The square of 5 is 25
