num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

# for item in num_list:
#     if item > 45:
#         print(f"Over 45")
#     else:
#         print(f"Under 45")

count = 0

for index, item in enumerate(num_list):
    if item == 36:
        print(f"Number found at position: {index}")
        break
    if item > 45:
        print(f"Over 45")
    else:
        print(f"Under 45")

    count += 1

print(count)


