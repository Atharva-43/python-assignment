try : 
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a/b
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error:please enter valid numbers!")
else:
    print("Division result is ", result)
finally :
    print("Program executed successfully") 