# Id Function 

# assign x to an int object

x=10
# we will use id() function 
# it returns a unique integer identifying for every object existing in memory
print(id(x)) # Output:2195928017488

# assign to y
y=x
print(id(y)) # Output:2195928017488

# assign x to a new int object 
x=20
print(id(x)) # Output:2632149592976
