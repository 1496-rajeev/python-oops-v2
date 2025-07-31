class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car start...")

    @staticmethod
    def stop():
        print('car stop...')

class ToyotaCar(Car):
    def __init__(self, name, type): 
        super().__init__(type) # super method/constructer is instance of inheritate class
        self.name = name
        super().start # start method of parent class will be called

car1 = ToyotaCar('fortuner', 'petrol')

print(car1.name)
print(car1.type)
car1.start()

