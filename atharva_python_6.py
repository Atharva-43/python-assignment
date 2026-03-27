class Vehicle:
    def move(self):
        print("Vehicle is moving")
class Car(Vehicle):
    def move(self):
        print("driving on road")
class Cycle(Vehicle):
    def move(self):
        print("pedalling on road")
c = Car()
c1 = Cycle()
c.move()
c1.move()