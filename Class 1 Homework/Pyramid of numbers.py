num = int(input("Choose a number: "))
number = 1
num_of_rows = 1
for i in range(num):
    for j in range(num_of_rows):
        print(number," ", end = "")
        number += 1
    print()
    num_of_rows += 1