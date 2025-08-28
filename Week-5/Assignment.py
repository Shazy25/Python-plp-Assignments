# Question 1 

class Book:
    def __init__(self, title, author, pages):
        self.title = title 
        self.author = author
        self.pages = pages


    def info(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"

    def read(self):
        print(f"Reading '{self.title}'...")


class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size

    def info(self):
        return f"{super().info()}, file size: {self.file_size}MB"

    def read(self):
        print(f"Opening digital book '{self.title}' on your device 📱")


 #Example usage

Book = physical_book = Book("1984", "George Orwell", 328)
digital_book = EBook("Digital Fortress", "Dan Brown", 356, 2)

print(physical_book.info())
physical_book.read()

print(digital_book.info())
digital_book.read()



# Question 2 
class Animal:
    def move(self):
        print("Animal moving")

class Dog(Animal):
    def move(self):
        print("Dog is running 🐕")

class Bird(Animal):
    def move(self):
        print("Bird is flying 🐦")

class Fish(Animal):
    def move(self):
        print("Fish is swimming 🐟")

# Testing
dog = Dog()
bird = Bird()
fish = Fish()

dog.move()    # Dog is running 🐕
bird.move()   # Bird is flying 🐦
fish.move()   # Fish is swimming 🐟





        



