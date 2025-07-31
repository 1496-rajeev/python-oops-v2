class Account:
    def __init__(self,acc_no,acc_name):
        self.acc_no=acc_no
        self.__acc_name=acc_name #private can't access outside class

    def get_name(self):
        print(self.__acc_name) # private attribute can be access inside class 

acc = Account(1234,'saving')
acc.get_name()
print(acc.acc_no) #public can be access
print(acc.__acc_name) # private can't acess 


# we can make same for method also by adding __ double underscore

