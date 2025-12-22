class Student:
    def __init__(self,name,id,math_grade,science_grade,computer_grade):
        self.name = name
        self.student_id = id
        self.math = math_grade
        self.science = science_grade
        self.computer = computer_grade
    
    def calculate_total(self):
        total_marks = self.math+self.science+self.computer
        return total_marks

    def calculate_average(self):
        average = (self.math+self.science+self.computer)//3
        return average

    def calculate_grade(self):
        if self.calculate_average() >= 90:
            grade = "A"
        elif self.calculate_average() >= 75:
            grade = "B"
        elif self.calculate_average() >= 60: 
            grade = "C"
        elif self.calculate_average() >= 40:
            grade = "D"
        else:
            grade = "F"
        return grade

    def display_report(self):
        print(f"""
    ---------------------------------------------
            Student Name: {self.name}
            Student Id: {self.student_id}
            Total Marks: {self.calculate_total()}/300
            Average Marks: {self.calculate_average()}/100
            Grade: {self.calculate_grade()}
    ---------------------------------------------
            """)
        
om = Student("Om Joshi", 43275635, 87,92,93)

print(f"Total Marks: {om.calculate_total()}/300")
print(f"Average Marks: {om.calculate_average()}/100")
print(f"Grade: {om.calculate_grade()}")
om.display_report()