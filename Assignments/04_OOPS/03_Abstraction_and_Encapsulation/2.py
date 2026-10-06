# Assignment 2: Animal Sounds

class Animal:
    def makeSound(self):
        print("Some generic sound.")

class Dog(Animal):
    def makeSound(self):
        print("Woof Woof.")

class Cat(Animal):
    def makeSound(self):
        print("Meow Meow.")

if __name__ == "__main__":
    Animal().makeSound()
    Dog().makeSound()
    Cat().makeSound()
