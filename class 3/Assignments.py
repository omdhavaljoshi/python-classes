# Assignment 1 --> Write a function called multiply_all that multiplies any number of arguments.
def multiply_all(*nums):
    multiply = 1
    for i in nums:
        multiply *= i
    print(multiply)
multiply_all(45,76,23,68)

# Assignment 2 --> Write a function that accepts keyword arguments for a product (name, price, category) and prints them in a clean format.
def product_format(**product):
    values = []
    for value in product.values():
        values.append(value)
    print("Name:", values[0])
    print("Price:", values[1])
    print("Category:", values[2])
product_format(Name = "Milk", Price = "$3.00", Category = "Dairy")

# Assignment 3 --> Using map and a lambda, convert a list of integers into their string representations.
print(list(map(lambda x: str(x),[10,15,30,35])))

# Assignment 4 --> Given a list of numbers, filter all values that are divisible by both 3 and 5.
print(list(filter(lambda x: x/3 == x//3 and x/5 == x//5,[23,45,35,23])))

# Assignment 5 --> 
data = [14, 50, 99, 101, 22, 33, 150]

# 1. Use filter to keep only values greater than 50.
over_100 = list(filter(lambda x: x>100, data))

# 2. Use map to multiply the remaining values by 2.
multiply_2 = list(map(lambda x: x*2, over_100))

# 3. Store and print the final list.
print(multiply_2)