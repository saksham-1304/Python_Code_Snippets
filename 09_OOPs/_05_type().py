class MyClass:
    def __init__(self, attribute):
        self.attribute = attribute

    def method(self):
        pass


obj = MyClass("value")

# Using type() on the class

print("Type of MyClass:", type(MyClass))


# Using type() on an instance of the class
print("Type of obj:", type(obj))
