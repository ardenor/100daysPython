def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 5, 6))

def calculate(n, **kwargs):
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["mult"]
    print(n)

calculate(2, add=3, mult=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")

my_car = Car(make="Nissan")
print(my_car.model)
print(my_car.make)