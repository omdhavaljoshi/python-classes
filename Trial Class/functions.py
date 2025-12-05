list1 =  [4,56,43,7,2,35]

def list_min(list):
    minimun = list[0]
    for i in list:
        if i < minimun:
            minimum = i
    return minimum

def list_max(list):
    maximum = list[0]
    for i in list:
        if i > maximum:
            maximum = i
    return maximum

def list_sum(list):
    total = 0
    for i in list:
        total += i
    return total
def list_len(list):
    lenght = 0
    for i in list:
        lenght += 1
    return lenght

print(list_sum(list1))
print(list_min(list1))
print(list_max(list1))
print(list_len(list1))