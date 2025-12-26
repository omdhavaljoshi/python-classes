# Inheritance
# parent
# child
class A:
    x = 10
    def f1(self):
        print("This is the f1 function from class A")

class B(A):
    pass

a = A()
a.f1()
print(a.x)

b = B()
b.f1()
print(b.x)