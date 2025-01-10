# Define a class
class MyClass:
    # Constructor method
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    # Method to perform an action
    def method1(self):
        return f"Method 1 called with attributes {self.attribute1} and {self.attribute2}"

# Create objects (instances) of the class
obj1=MyClass("value1","value2")
obj2=MyClass("value3","value4")

# Access attributes and call methods of objects
print(obj1.attribute1)
print(obj2.attribute2)

print(obj1.method1())
print(obj2.method1())