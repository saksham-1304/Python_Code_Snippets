class MyClass:
    def __init__(self, attribute):
        self.attribute = attribute

    def method(self):
        pass


obj = MyClass("value")

# Using dir() on the class

print("Attributes and methods of MyClass:")
print(dir(MyClass))


# Using dir() on an instance of the class
print("Attributes and methods of obj:")
print(dir(obj))
