# Assignment 1: Design Your Own Class - Book

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")

    def change_title(self, new_title):
        self.title = new_title
        print(f"Title has been updated to: {self.title}")


# Example usage:
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
book1.display_info()

book1.change_title("The Great Gatsby: Revised Edition")
book1.display_info()

# Assignment 2: Polymorphism Challenge - Vehicles

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement this method")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")


# Example usage:
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()  # Polymorphism: each object has its own implementation of move()



