class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math)/3) + '%' 

    @property
    def percentageOne(self):
        return str((self.phy + self.chem + self.math)/3) + '%' 
    
s = Student(90,99,86)
print(s.percentage) # it will calculate percentage according to initial value
s.phy = 45
print(s.phy) # it will change the phy marks but not change percentage
print(s.percentage)

print(s.percentageOne)  # but using property method we can change the intance calculation on any value change



