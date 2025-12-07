# In class activities:
def max_args(*num):
    max_value = 0
    for i in num:
        if i > max_value:
            max_value = i
        else:
            continue
    print(max_value)

max_args(132,43,23,54,3)
