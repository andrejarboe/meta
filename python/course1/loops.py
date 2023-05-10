favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for i in range(10):
    print(f"looping {i}")

for item in favorites:
    print(f"I like this {item}")

count = 0 

while count < len(favorites):
    print(f"I like this desert, {favorites[count]}")
    count += 1

for idx, item in enumerate(favorites):
    print(idx, item)