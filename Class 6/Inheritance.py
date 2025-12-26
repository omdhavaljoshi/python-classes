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

# parent/super/base class
class Parent:
    def __init__(self,n):
        self.name = n
        print("parent object is created")
    def f1(self):
        print("f1 from parent class is called")
# derived class, sub class
class Child(Parent):
    def __init__(self,n,x):
        super().__init__(n)
        self.x = x
        print("child class object is created")
    def f2(self):
        print("f2 from class child")
# p = Parent("xyz")
c = Child("xyz",100)