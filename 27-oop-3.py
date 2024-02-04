class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        item = {'name': name, 'price': price}
        self.items.append(item)

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        # total = 0
        # for item in self.items:
        #     total += item['price']
        #
        # return total

        return sum(item['price'] for item in self.items)


store = Store("John's Store")
store.add_item("keyboard", 160)
store.add_item("laptop", 800)
print(store.stock_price())  # 960


class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method.")


test = ClassTest()
test.instance_method()
# ClassTest.instance_method() # Type Error

ClassTest.class_method()
# test.class_method() ??

ClassTest.static_method()
test.static_method()


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def softcover(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


print(Book.TYPES)  # ('hardcover', 'paperback')

book = Book.hardcover("Harry Potter", 1500)
print(book.name)  # Harry Potter
