### Singleton

class DatabaseConnection:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance

    def __str__(self):
        return "Connected"


db1 = DatabaseConnection.get_instance()
print(db1)  # Connected
db2 = DatabaseConnection.get_instance()
print(db2)  # Connected
print(db1 is db2)  # True


### Factory

class House:
    def __init__(self, house_type, size, rooms, floors):
        self.house_type = house_type
        self.size = size
        self.rooms = rooms
        self.floors = floors


class HouseFactory:
    @staticmethod
    def create_apartment(size, rooms, floors):
        return House("Apartment", size, rooms, floors)

    @staticmethod
    def create_bungalow(size, rooms, floors):
        return House("Bungalow", size, rooms, floors)

    @staticmethod
    def create_castle(size, rooms, floors):
        return House("Castle", size, rooms, floors)


apartment = HouseFactory.create_apartment(100, 2, 1)
print(apartment.house_type)  # Apartment
bungalow = HouseFactory.create_bungalow(200, 3, 2)
print(bungalow.house_type)  # Bungalow


### Builder

class HouseBuilder:
    def __init__(self):
        self.house = House("", 0, 0, 0)

    def set_house_type(self, house_type):
        self.house.house_type = house_type
        return self

    def set_size(self, size):
        self.house.size = size
        return self

    def set_rooms(self, rooms):
        self.house.rooms = rooms
        return self

    def set_floors(self, floors):
        self.house.floors = floors
        return self

    def build(self):
        return self.house


builder = HouseBuilder()
apartment = builder.set_house_type("Apartment").set_size(100).set_rooms(2).set_floors(1).build()
