num = int(input("Choose a number: "))
num_of_stars = 1
for i in range(num):
    for j in range(num_of_stars):
        print("*", end = "")
    print()
    num_of_stars += 1