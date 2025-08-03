# it help to change the class attribute

class Person:
    name='anonymous'

    def changeclassName(self,name):
        self.name = name # it will not directly change the class name attribute it create new name attribute inside changeclassName

        self.__class__.name = name # it will change the class name attribute
        Person.name = name # it will also change the class attribute directly

    @classmethod
    def changeName(cls,name):
        cls.name = name # it will also change class name attribute by using classmethod decorator

p = Person()
p.changeclassName('john')
print(p.name)
print(Person.name)
p.changeName('kunal')
print(Person.name)

