# Function with arbitary number of arguments


def print_numbers(*args):
    """
    Prints all the numbers passed as arguments.

    Args:
    *args:An arbitary number of numeric arguments.

    Returns:
    None

    """
    for arg in args:
        print(arg)


# Calling the function with different number of arguments
print_numbers(1, 2, 3)
print_numbers(4, 5)
