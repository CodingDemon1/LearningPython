s='PyNaTive'
lower_case = []
upper_case = []

for char in s:
    if char.islower():
        lower_case.append(char)
    else:
        upper_case.append(char)

result = ''.join(lower_case + upper_case)
print(result)