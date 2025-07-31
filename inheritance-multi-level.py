class Car: # level 1
    @staticmethod
    def start():
        print("car start...")

    @staticmethod
    def stop():
        print('car stop...')

class ToyotaCar(Car): # level 2
    def __init__(self,brand):
        self.brand= brand

class Fortuner(ToyotaCar): # Level 3 - it will access all aatrribute of Car (level 1)
    def __init__(self,type):
        self.type = type

car1 = Fortuner('Petrol')

print(car1.type)
car1.start()
