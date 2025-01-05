# Function to calculate area


def calculate_area(length, width, unit="cm"):
    """
    Calculates the area of a rectangle.

    Parameters:
    length(float):The length of the rectangle.
    width(float):The width of the rectangle.
    unit(str):The unit of measurement(default is "cm")

    Returns:
    float:The area of the rectangle.
    """
    area = length * width
    print(f"The area is {area} {unit}^2")
    return area


# Calling the function with positional arguments
calculate_area(5.0, 3.0)  # 'length' and 'width' are arguments
# Output:The area is 15.0 cm^2

# Calling the function with the keyword arguments
calculate_area(width=2.5, length=4.0, unit="m")
# 'width' ,'length' and 'unit' are arguments
# Output:The area is 10.0 m^2
