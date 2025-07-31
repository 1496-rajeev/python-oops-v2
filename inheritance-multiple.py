class A:
    varA = 'class A'

class B:
    varB = 'class B'

class C(A,B): # can inherite multiple class attributes
    varC = 'class C'

c = C()

print(c.varA)
print(c.varB)
print(c.varC)