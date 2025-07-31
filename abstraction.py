# In class hiding the implemetation details and showing the essential details to the user 

class Car:
    def __init__(self):
        self.clutch = False
        self.brk = False
        self.acc = False

    def start(self):
        self.clutch=True
        self.acc=True
        print("Car started")

car = Car()
car.start()