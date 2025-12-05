num = int(input("Choose a number: "))
reversed_num = 0
num_2 = num
while num_2>0:
    digit = num_2%10
    reversed_num = (reversed_num*10)+digit
    num_2 //= 10
print(reversed_num)
if reversed_num == num:
    print("Yes, it's a palindrome.")
elif reversed_num != num:
    print("No, it's not a palindrome.")