def safe_division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Cannot divide by zero."

print(safe_division(5, 0)) 

