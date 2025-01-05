# While loop

# Initialize a variable
count = 0

# Define the while loop condition
while count < 5:
    # Code block to be executed as long as the condition is true
    print("Count:", count)

    # Update the variable too avoid infinite loop
    count += 1

# Print a message after the loop terminates
print("Loop execution complete!")

'''
Output
Count: 0
Count: 1
Count: 2
Count: 3
Count: 4
'''