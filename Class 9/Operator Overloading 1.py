class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self): #represent
        return "xyz"
    
    def __str__(self):
        return f"Object Human({self.name},{self.age})"

om = Human("Om Joshi",13)
print(om.__repr__())
print(om)