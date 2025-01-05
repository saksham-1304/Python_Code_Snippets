# List Comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)

"""
Output
[1, 4, 9, 16, 25]
"""
selected_squared_numbers = [x**2 if x % 2 == 0 else x for x in numbers]
print(selected_squared_numbers)

'''
Output
[1, 4, 3, 16, 5]
'''
