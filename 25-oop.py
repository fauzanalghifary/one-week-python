class Puppy:
    species = "Canis familiaris"
    num_of_puppies = 0

    def __init__(self, name, breed, location):
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []
        Puppy.num_of_puppies += 1

    @staticmethod
    def count_puppies():
        print("Whine! Whine! Whine!")

    @classmethod
    def count_puppies(cls):
        print(f"There are {cls.num_of_puppies} puppies.")

    @classmethod
    def register_stray(cls):
        cls('coming soon', 'unknown', 'unknown')

    def bark(self):
        print(f"{self.name} is barking! Woof! Woof!")

    def eat(self):
        print("Nom! Nom! Nom!")

    def learn_trick(self, new_trick):
        if new_trick not in self.tricks:
            self.tricks.append(new_trick)

    def perform_trick(self, trick):
        if trick in self.tricks:
            print(f"{self.name} is performing {trick}!")
        else:
            print(f"{self.name} doesn't know how to {trick}.")


elton = Puppy("Elton", "Golden Retriever", "Cebu")
print(elton.name)  # Elton
print(elton.tricks)  # []
print(isinstance(elton, Puppy))  # True

elton.bark()  # Elton is barking! Woof! Woof!
elton.eat()  # Nom! Nom! Nom!

elton.learn_trick("sit")
elton.learn_trick("shake")
elton.learn_trick("shake")
print(elton.tricks)  # ['sit', 'shake']

elton.perform_trick("sit")  # Elton is performing sit!
elton.perform_trick("shake")  # Elton is performing shake!
elton.perform_trick("roll over")  # Elton doesn't know how to roll over.

print(elton.species)  # Canis familiaris
print(Puppy.species)  # Canis familiaris
print(Puppy.num_of_puppies)  # 1

Puppy.whine()  # Whine! Whine! Whine!
elton.whine()  # Whine! Whine! Whine!

Puppy.count_puppies()  # There are 1 puppy.

Puppy.register_stray()


class Dog(Puppy):
    def __init__(self, name, breed, location, color):
        super().__init__(name, breed, location)
        self.color = color

    def bark(self):
        print(f"{self.name} is barking! Woof! Woof! Woof!")


fido = Dog("Fido", "Labrador Retriever", "Manila", "black")
print(fido.name)  # Fido
