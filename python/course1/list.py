# list is an array
# list start at 0
arr = [1,2,3,4]

arr2 = [1, [2,3,4], 5, 6]

print(*arr)
#1 2 3 4

print(arr, sep = "+")

arr.insert(len(arr), 16)
arr.append(90)
arr.extend([6,7,8,9])
print(arr)

arr.pop(4)
del arr[0]
print(arr)

for item in arr:
    print(f"Value: {item}")

