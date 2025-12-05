num = int(input("Please enter a number: "))
original = num
num_2 = num
count = 0
answer = 0
while num > 0:
    count += 1
    num //= 10
for i in range(count):
    digit = num_2%10
    answer += digit ** count
    num_2 //= 10
if original == answer:
    print("Yes, it is a Armstrong number.")
else:
    print("No, it is not a Armstrong number.")