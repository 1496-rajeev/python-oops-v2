class Car:
    @staticmethod
    def start():
        print("car start...")

    @staticmethod
    def stop():
        print('car stop...')

class ToyotaCar(Car):
    def __init__(self,name):
        self.name= name

car1 = ToyotaCar('fortuner')

print(car1.name)
car1.start()
