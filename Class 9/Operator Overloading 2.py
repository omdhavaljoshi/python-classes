class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self):
        pass


# print(1 + 2)
p1 = Point(10,20)
p2 = Point(11,21)
print(p1)
print(p2)
print(2+4)
# print("akash".__add__( "roy"))
print("akash" + "roy")
print([1,2,3,4,5]+[12,3,4,66,22,66])
print(p1 + p2) # p1.__add__(p2)