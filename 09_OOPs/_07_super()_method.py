class Parent:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Print class display method:", self.name)


class Child(Parent):
    def __init__(self, name, age):
        # Calling the Parent class's __init__ method using super()
        super().__init__(name)
        self.age = age

    def display(self):
        # Calling the Parent class's display method
        super().display()
        print("Child class display method:", self.age)


# Creating an instance of the Child class
child = Child("Alice", 10)

# Calling the display method of the Child class
child.display()
