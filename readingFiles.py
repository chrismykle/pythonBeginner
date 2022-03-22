
employee_file = open("employees.txt", "a")      # "w" overwrites everything, "r" read only, "a" is append

employee_file.write("\nEirin - Artist")

employee_file.close()

employee_file1 = open("employees.txt", "r")

print(employee_file1.read())

employee_file1.close()
