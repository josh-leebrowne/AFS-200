"""
To get input from the user, we use the input function.  The input function takes one argument which is a string that provides the user with a prompt to let them know what information to enter.  
"""

employeeName = "John Smith"

employeeData = "How many hours did " + employeeName + " work last week?"

hoursWorked = int(input(employeeData))
print(hoursWorked)

prompt = "Does "+employeeName+"'s "+ str(hoursWorked)+" hours included any overtime? "
overtime = input(prompt)
print(overtime)