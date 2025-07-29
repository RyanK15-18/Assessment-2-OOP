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
    
def load_inventory(filename):
    fiction_inventory = []
    nonfiction_inventory = []
    electronic_inventory = []
    textbook_inventory = []

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) < 4:
                continue

            item_type = parts[0].lower()
            name = parts[1]
            author_or_brand = parts[2]
            serial = parts[3]
            
            if item_type == "fiction":
                fiction_inventory.append(Fiction(name, author_or_brand, serial))
            elif item_type == "nonfiction":
                nonfiction_inventory.append(NonFiction(name, author_or_brand, serial))
            elif item_type == "textbook":
                subject = parts[4] if len(parts) > 4 else "Unknown"
                textbook_inventory.append(TextBook(name, author_or_brand, serial, subject))
            elif item_type == "electronics":
                electronic_inventory.append(Electronics(name, author_or_brand, serial))

    return fiction_inventory, nonfiction_inventory, textbook_inventory, electronic_inventory


def main():
    fiction, nonfiction, textbooks, electronics = load_inventory('library_inventory.txt')

    item_types = {
        "fiction": fiction,
        "nonfiction": nonfiction,
        "textbook": textbooks,
        "electronics": electronics
    }

    while True:
        action = input("\nWould you like to borrow or return an item? (borrow/return/exit): ").strip().lower()
        if action == "exit":
            print("Thanks for visiting the library!")
            break

        category = input("Enter item type (fiction/nonfiction/textbook/electronics): ").strip().lower()
        if category not in item_types:
            print("Invalid category. Try again.")
            continue
