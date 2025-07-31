# wrapping data and function into a single unit(object)

class Student:
    school_name = 'V.P.M' # data

    def __init__(self, name,roll_no):
        self.name = name
        self.roll_no = roll_no

    def get_datail(self): #function
       return f'name: {self.name}, school name: {self.school_name}'

student1 = Student('raj',29)
print(student1.get_datail())