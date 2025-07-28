exyrta line 
class ItemAtLibrary:
    def __init__(self, name, authorName, serialNumber):
        self.name = name
        self.authorName = authorName
        self.serialNumber = serialNumber
        self.borrowed = False

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            return f"{self.name} has been borrowed."
        return f"{self.name} has already been borrowed."

    def return_item(self):
        if self.borrowed:
            self.borrowed = False
            return f"{self.name} has been returned."
        return f"{self.name} was not borrowed."

    def get_info(self):
        return f"{self.name} by {self.authorName}, Serial: {self.serialNumber}"

    def __str__(self):
        return self.get_info()


class Book(ItemAtLibrary):
    def __init__(self, name, authorName, serialNumber, genre):
        super().__init__(name, authorName, serialNumber)
        self.genre = genre


class Fiction(Book):
    def __init__(self, name, authorName, serialNumber):
        super().__init__(name, authorName, serialNumber, genre="Fiction")

    def borrow(self):
        return f"{self.name} is Fiction and cannot be borrowed."


class NonFiction(Book):
    def __init__(self, name, authorName, serialNumber):
        super().__init__(name, authorName, serialNumber, genre="Non-Fiction")

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            return f"{self.name} has been borrowed for 2 weeks."
        return f"{self.name} is already borrowed."


class TextBook(Book):
    def __init__(self, name, authorName, serialNumber, subject):
        super().__init__(name, authorName, serialNumber, genre="Textbook")
        self.subject = subject

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            return f"{self.name} has been borrowed until the end of the school year."
        return f"{self.name} is already borrowed."


class Electronics(ItemAtLibrary):
    def __init__(self, name, brandName, serialNumber):
        super().__init__(name, brandName, serialNumber)
        self.brandName = brandName

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            return f"{self.name} has been borrowed until the end of the day."
        return f"{self.name} is already borrowed."
    
def main():
    # items in a library
    fiction_book = Fiction("The Lost World", "Arthur Conan Doyle", "FIC123")
    nonfiction_book = NonFiction("A Brief History of Time", "Stephen Hawking", "NF456")
    textbook = TextBook("Calculus Essentials", "John Smith", "TB789", subject="Mathematics")
    laptop = Electronics("Library Laptop", "Dell", "EL321")
    
    
#they want to return or borrow
#what item do they want Electronic, textbook, fiction, nonfiction
#


