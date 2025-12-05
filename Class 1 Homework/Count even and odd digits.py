n = 568479
odd = []
even = []
while n>0:
    digit = n%10
    if digit//2 == digit/2:
        even.append(digit)
    else:
        odd.append(digit)
    n //= 10
print("Even: ", len(even), even)
print("Odd: ", len(odd), odd)