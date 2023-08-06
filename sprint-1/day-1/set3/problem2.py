# 2. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
#     - *Input*: Add "John": 25, Update "John": 26, Delete "John"
#     - *Output*: "{}, {'John': 26}, {}"


dics = {}
print(dics)

dics["John"] = 25

print(dics)

dics["John"] = 26

print(dics)

dics.pop("John")

print(dics)

