# 1. Anagram Check

a,b = "cinema","iceman"

a = list(a)
a.sort()
b = list(b)
b.sort()


if a == b:
    print(True)
else:
    print(False)