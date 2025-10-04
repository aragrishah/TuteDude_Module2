# Calculate Factorial Using a Function 

def factorial(num):
    if num < 0:
        return("Factorial is not defined for negative numbers.")
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)
    
result = factorial(5)
print(result)