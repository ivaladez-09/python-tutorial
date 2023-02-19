from dataclasses import dataclass, field


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
        """It can be called without instantiate the class.
        Also, you have access to cls = class"""
        return cls("Tedy", num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        """It can be called without instantiate the class."""
        return num1 + num2

    def __repr__(self):
        return f"PLayerCharacter(name={self.name}, age={self.age})"


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


@dataclass
class MyDataClass:
    """The 'dataclass decorator will allow us to have automatically the constructor '__init__()' and
    somo dunder methods as '__repr__'.'"""
    name: str
    age: int = field(repr=False, default=10)  # Not adding it to __repr__
    player: PLayerCharacter = PLayerCharacter("Aaron", 18)  # Default value


def main(*args, **kwargs) -> None:
    # The classmethod can be called without instantiate the class into an object
    player1 = PLayerCharacter.adding_things(12, 6)
    player1.shout()
    print(PLayerCharacter.adding_things2(3, 17))

    child1 = Child("Ivan", 24, "Juan", 49)
    child1.display()

    dunder = DunderClass("Ivan")
    print(dunder)
    print(dunder())
    print(dunder["name"])
    del dunder

    data_class: MyDataClass = MyDataClass("Ivan", 27, PLayerCharacter("Edgar", 22))
    print(data_class)

    data_class2: MyDataClass = MyDataClass("Alejandro", 32)
    print(data_class2)

    data_class3: MyDataClass = MyDataClass("Eduardo")
    print(data_class3)


if __name__ == '__main__':
    main()
