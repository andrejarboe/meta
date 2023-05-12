# kwargs
# args

def sumOf(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sumOf(10, 10, 20, 1))