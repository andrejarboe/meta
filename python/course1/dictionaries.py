# Dictionaries
# used to store data values in key:value pairs.
# optimized to retrieve values
# key:value
# known as key value pair
# values can be changed

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

diction = {
    1: 'test',
    'name': "Andre",
    2: 74
}

# prints the whole thing
print(diction)

# prints the brand
print(thisdict["brand"])

thisdict["brand"] = "Honda"
print(thisdict["brand"])
del thisdict["year"]
print(thisdict)

for key, value in diction.items():
    print(str(key) + " : " + str(value))
