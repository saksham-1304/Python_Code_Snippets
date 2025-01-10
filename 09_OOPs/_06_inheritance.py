# Define the base class (parent class)


class Animal:
    def __init__(self, name):
        self.name = name


def speak(self):
    pass


# Define a subclass (derived class) that inherits from Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"


# Define a subclass (derived class) that inherits from Animal
class Cat(Animal):
    def speak(self):
        return "Meow!"


# Create instances of the subclasses

dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the speak() method on instances of the subclasses
print(dog.name, "says:", dog.speak())
print(cat.name, "says:", cat.speak())
