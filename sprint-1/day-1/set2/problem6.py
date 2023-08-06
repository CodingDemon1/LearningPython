# Concatinate Two lists

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

result = []

for i in list1:
    for j in list2:
        result.append(i+j)

print(result)