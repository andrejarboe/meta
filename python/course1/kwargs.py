# kwargs

def sumOf(**kwargs):
    sum = 0
    for key, value in kwargs.items():
        sum += value
    return round(sum, 2)

print(f"${sumOf(coffee = 2.99, cake=4.55, juice=2.99)}")