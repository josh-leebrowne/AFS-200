employeeName = "John Smith"
employeeID = 1254 
employeeHourlyWage = 15.20
hoursWorked = 10

print("Employee {0} ({1}) hourly wage is ${2}".format(employeeName,employeeID,employeeHourlyWage))

print(f"Employee {employeeName} ({employeeID}) is due is ${employeeHourlyWage*hoursWorked}")
print(f"Employee {employeeName} is due ${(employeeHourlyWage * hoursWorked):,.2f}")

def weeklyPay(hrlyRate, hrsWorked):
	return hrlyRate * hoursWorked

print(f"Employee {employeeName} is due ${weeklyPay(employeeHourlyWage,hoursWorked):,.2f}")

def weeklyPay(hrlyRate, hrsWorked):
    overtimeBonus = 100
    return hrlyRate * hoursWorked + overtimeBonus

print(f"Employee {employeeName} is due ${weeklyPay(employeeHourlyWage,hoursWorked):,.2f}")