
def max_num(num1, num2, num3):          # Test for the maximum number
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num3
    else:
        return num3


print(max_num(3, 4, 5))
