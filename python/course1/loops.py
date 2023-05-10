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

# search for churros
for dessert in favorites:
    if dessert == 'Churros':
        print('Yes one of my favorite desserts is', dessert)
        break
else:
    print('No sorry, that dessert is not on my list')

# skips over churros
for dessert in favorites:
    if dessert == 'Churros':
        continue
    print('Other desserts I like are', dessert)

# ignore the if
for dessert in favorites:
    if dessert == 'Churros':
        pass
    print('Other desserts I like are', dessert) 