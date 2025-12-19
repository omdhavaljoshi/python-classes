class Animal:
    # 1. Constructor
    def __init__(self, speciesValue, max_ageValue, max_weightValue, dietValue):
        # 2. properites/characteristics: variables
        self.species = speciesValue
        self.max_age = max_ageValue
        self.max_weight = max_weightValue
        self.diet = dietValue
        print("Constructor of Human class")

    def displayInfo(self):
        print(f"""
    -------------------------------
        Species : {self.species}
        Max Age : {self.max_age}
        Max Weight: {self.max_weight}
    -------------------------------
        """)
    
    def sleep(self):
        print(f"{self.species} is sleeping.")
