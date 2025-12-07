# In class activity
def student_profile(**details):
    for i in details.keys():
        print(f"{i} : {details[i]}")

student_profile(Name = "Om", Age = 13, City = "Sydney")