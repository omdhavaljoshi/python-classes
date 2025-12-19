class Human:
    # 1. Constructor
    def __init__(self, nameValue, ageValue, weightValue):
        # 2. properites/characteristics: variables
        self.name = nameValue
        self.age = ageValue
        self.weight = weightValue

        print("Constructor of Human class")

    def displayInfo(self):
        print(f"""
    -------------------------------
        Name : {self.name}
        Age : {self.age}
        Weight: {self.weight}
    -------------------------------
        """)
    
    def sleep(self):
        print(f"{self.name} is sleeping.")


om = Human("Om",13,45)
jeet = Human("Jeet",9,30)
dhanush= Human("Dhanush",13,47)
print(om)
print(jeet)
print(dhanush)
print(om.name)
print(jeet.name)
print(dhanush.name)
om.displayInfo()
jeet.displayInfo()
dhanush.displayInfo()
om.sleep()