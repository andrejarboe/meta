# functions
# declare function with def

def sun(x, y):
    return x + y

# Example 
bill = 175.00

tax_rate = 15

total_tax = (bill * tax_rate) / 100.00

print(f'total tax {total_tax}')

# turns into 
def calculateTax(bill, taxRate):
    return (bill * taxRate) / 100.00

print(f"total tax {calculateTax(175, 15)}")
