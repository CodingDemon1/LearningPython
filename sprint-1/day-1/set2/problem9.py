# Problem 9: Create a dictionary by extracting the keys from a given dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

result = {}
for i in keys:
    result.update({i:sample_dict[i]})

print(result)