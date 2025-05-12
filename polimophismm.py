class Cat:
    def speak(self):
        print("Meow")
class Dog:
    def speak(self):
        print("Woof")
animals =[Cat(),Dog()]
for i in animals:
    i.speak()   