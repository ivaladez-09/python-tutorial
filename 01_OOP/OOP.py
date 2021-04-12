class PLayerCharacter:
    membership = True  # Public variable
    _private_var = 0  # Private by convention, it is still public
    __duder_var = 0  # Dunder var (starts with __) that works as private

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f"My name is {self.name} and I'm {self.age} years old.")

    @classmethod
    def adding_things(cls, num1, num2):
        """It can be called without instanciate the class.
        Also, you have acces to cls = class"""
        return cls("Tedy", num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        """It can be called without instanciate the class."""
        return num1 + num2


# The classmethod can be called without instaciate the class into an object
player1 = PLayerCharacter.adding_things(12, 6)
player1.shout()
print(PLayerCharacter.adding_things2(3, 17))


class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Parent class with name {self.name}")


class Child(Parent):
    def __init__(self, name, age, parent_name, parent_age):
        self.name = name
        self.age = age
        super().__init__(parent_name, parent_age)

    def display(self):
        print(f"Child class with name {self.name}")


child1 = Child("Ivan", 24, "Juan", 49)
child1.display()


class DunderClass:
    def __init__(self, name):
        self.name = name
        self.my_dict = {
            "name": "Francisco",
            "has_pets": False
        }

    def __str__(self):
        """Dunder method to tell Python what to do when the object is called as string"""
        return self.name

    def __call__(self):
        """Dunder method to be called as ()"""
        return "Yes?"

    def __del__(self):
        """Dunder method to be called when the object is deleted"""
        print("Deleted!")

    def __getitem__(self, i):
        """Dunder method to be called as []"""
        return self.my_dict[i]


dunder = DunderClass("Ivan")
print(dunder)
print(dunder())
print(dunder["name"])
del dunder
