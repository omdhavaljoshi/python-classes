# Activity 1 --> Use map + lambda to convert each score to a GPA (GPA = score / 20).
print(list(map(lambda x: x/20, [95, 67, 88, 76, 45, 99, 100, 52])))

# Activity 2 --> Use filter + lambda to keep only GPAs above 3.0.
print(list(filter(lambda x: x>3.0,[4.75, 3.35, 4.4, 3.8, 2.25, 4.95, 5.0, 2.6])))

# Activity 3 --> Write a function using *args to calculate the average of all GPAs.
def avarage_gpa(*gpa):
    gpa_list = []
    for i in gpa:
        gpa_list.append(i)
    print(sum(gpa_list)/len(gpa)+1)
avarage_gpa(4.75, 3.35, 4.4, 3.8, 2.25, 4.95, 5.0, 2.6)

# Activity 4 --> Write a function using **kwargs to print a summary containing: total students, passed count, average GPA.
def summary(**scores):
    score_list = []
    for values in scores.values():
        score_list.append(values)
    passed = filter(lambda x: x>50, score_list)
    print("Number of Students:",len(scores))
    print("Passed:",len(list(passed)))
    print("Avarage GPA:",end = " ")
    avarage_gpa(4.75, 3.35, 4.4, 3.8, 2.25, 4.95, 5.0, 2.6)
summary(student1 = 95, student2 = 67, student3 = 88, student4 = 76, student5 = 45, student6 = 99, student7 = 100, student8 = 52)