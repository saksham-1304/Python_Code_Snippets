x = "Haha"

##
print(x)  # Output: Haha

print(id(x))  # Output: 1697275325744


y = x[0]
print(y)  # Output:H


y = x[3]
print(y)  # Output: a

print(len(x))  # Output: 4

z = x + 2 * y

"""
z = x + 2  # TypeError: can only concatenate str (not "int") to str

"""

x = "A"
print(ord(x))  # Output: 65

x = "a"
print(ord(x))  # Output: 97

x = 65
print(chr(x))  # Output: A

a="2"
print(a.isdigit()) # Output:True

a="200"
print(a.isdigit()) # Output:True

a="A"
print(a.isdigit()) # Output:False

a="2.1"
print(a.isdigit()) # Output:False