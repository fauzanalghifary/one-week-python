from typing import List


def list_average(sequence: List) -> float:
    return sum(sequence) / len(sequence)


list_average([1, 2, 3])  # 2.0


# list_average([1, 2, 'a'])  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# list_average('a')  # TypeError: 'str' object is not iterable


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def softcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)


class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."
