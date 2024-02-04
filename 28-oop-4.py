class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print('Diconnected')


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print('Your printer is not connected!')
            return
        print(f'Printing {pages} pages.')
        self.remaining_pages -= pages


printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)  # Device 'Printer' (USB) (480 pages remaining)


class Bookshelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."


class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return f"{self.name} by {self.author}"


book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("Python 101", "John Smith")
shelf = Bookshelf(book1, book2)

print(shelf)  # Bookshelf with 2 books.