#Problem 8: Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

result = {}

for i in employees:
    result.update({i:defaults})

print(result)