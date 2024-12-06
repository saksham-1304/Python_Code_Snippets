# Try Catch

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError as zero_division_error:
    print("Error", zero_division_error)


"""
Output 1
Enter the numerator: 7
Enter the denominator: 7
Result: 1.0
"""

"""
Output 2
Enter the numerator: 6
Enter the denominator: 0
Error division by zero
"""

"""
Built-in Exceptions

SyntaxError: Raised when the Python interpreter encounters a syntax error in the code. 

IndentationError: Raised when there are incorrect indentation levels in the code.

TypeError: Raised when an operation or function is applied to an object of inappropriate type.

ValueError: Raised when a built-in operation or function receives an argument of the correct type but with an invalid value.

ZeroDivisionError: Raised when division or modulo operation is performed with a divisor of zero.

IndexError: Raised when trying to access an index that does not exist in a sequence.

KeyError: Raised when trying to access a key that does not exist in a dictionary.

FileNotFoundError: Raised when trying to open or access a file that does not exist.

NameError: Raised when a local or global name is not found.

"""
