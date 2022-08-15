"""
In Python, the print function is used to display output to the user.
"""

print('Hello world')



employeeName = "John Smith"
employeeID = 1254 
employeeHourlyWage = 15.20

print("Employee",employeeName,"(",employeeID,") hourly wage is",employeeHourlyWage)

"""
# Syntax string.format(value1, value2, ...)
"""

#positional arguments

print("Employee {0} ({1})'s hourly wage is {2}".format(employeeName,employeeID,employeeHourlyWage))

print("Employee {2} ({0})'s hourly wage is {1}".format(employeeID,employeeHourlyWage,employeeName))



# keyword arguments

print("Employee {name} ({id})'s hourly wage is {pay}".format(name = employeeName,id = employeeID, pay = employeeHourlyWage))


# empty placeholders

print("Employee {} ({})'s hourly wage is {}".format(employeeName,employeeID,employeeHourlyWage))


yearlySalary = 52148.50

# This portion is responsible for grouping the number
commas_only = "{:,}".format(yearlySalary)
print(commas_only)

# To ensure we have two decimal places
two_decimal_places = "{:.2f}".format(yearlySalary)
print(two_decimal_places)

# Both combined along with the currency symbol(in this case $)
currency_format = "${:,.2f}".format(yearlySalary)
print(currency_format)