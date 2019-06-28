class Cat:
    def sound(self):
        print("Nya")

class Dog:
    def sound(self):
        print("Mung")

cat = Cat()
dog = Dog()

animals = [cat, dog]

for animal in animals:
    animal.sound()