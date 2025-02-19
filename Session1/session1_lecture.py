def Hello():
    hello_str = "Hello, World!"
    name = "Eli"
    formatted_str = f"{hello_str} My name is {name}."
    print(formatted_str)
    
Hello()

    
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("The dog barks.")

class Cat(Animal):
    def speak(self):
        print("The cat meows.")

class Cow(Animal):
    def speak(self):
        print("The cow moos.")

def animal_sounds(animals):
    for animal in animals:
        animal.speak()

dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("MooMoo")

animals = [dog, cat, cow]
for animal in animals:
    print(animal.name)
animal_sounds(animals)

