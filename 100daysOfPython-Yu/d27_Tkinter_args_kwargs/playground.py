def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


func_sum = add(1, 5, 6, 10)
print(func_sum)
