# Problem 10: Modify the tuple

tuple1 = (11, [22, 33], 44, 55)

result = list(tuple1)

result[1][0] = 222

tuple1 = tuple(result)
print(tuple1)