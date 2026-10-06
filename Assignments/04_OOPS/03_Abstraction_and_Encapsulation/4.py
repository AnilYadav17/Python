# Assignment 4: Vehicle Speeds

class Vehicle:
    def speed(self):
        print("Speed varies for different vehicles.")

class Car(Vehicle):
    def speed(self):
        print("The car speed is 120 km/h.")

class Bike(Vehicle):
    def speed(self):
        print("The bike speed is 80 km/h.")

if __name__ == "__main__":
    Vehicle().speed()
    Car().speed()
    Bike().speed()
