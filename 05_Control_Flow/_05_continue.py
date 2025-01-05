# Continue

# Example of using continue in a while loop
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # Skip the rest of the loop body for i=3
    print(i)

'''
Output
1
2
4
5
'''