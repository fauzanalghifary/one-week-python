from datetime import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.created_at = datetime.now()

    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, datetime.now().year - birth_year)

    @staticmethod
    def is_adult(age):
        return age > 18

    def display(self):
        print(self.name + "'s age is: " + str(self.age))


person1 = Person('Adam', 19)
person2 = Person.from_birth_year('John', 1985)

person1.display()
person2.display()
