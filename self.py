class Car:
    company = 'TATA'
    def __init__(self, name ):
        self.name = name

    def get_company(self,name):
        print("get commpany self:",self)
        return [name,self.company]
    
    @staticmethod #decorator - Its takes a function as argument and return modified function
    def print_message():
        print('hello')

print('class attribute',Car.company)

car1 = Car('Punch')
print("instance or object atrribute", car1.company,car1.name)


print(car1.get_company('Nexon'))

car1.print_message()