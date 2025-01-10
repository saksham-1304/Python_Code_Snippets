# define the class


class Planet:
    count = 0

    def revolutions(self):
        self.count = self.count + 1
        print(self.count)


# create an object of the above class
x = Planet()

# print an attribute of this class
print(x.count)

# Call a method of this class
x.revolutions()
x.revolutions()
x.revolutions()
# another approach
Planet.revolutions(x)
