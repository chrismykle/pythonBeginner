
try:
    number = int(input("Enter a number: "))
    answer = 10 / 0
except ZeroDivisionError as err:            # Storing the error message in a variable
    print(err)
except ValueError as err1:                  # Use specific error catching
    print(err1)
