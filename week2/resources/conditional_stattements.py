"""
The general format of the if statement is:

if condition:
	statement
	statement
	statement
	etc.
"""	

balance = 105.50

if balance > 0:
    print("You have a balance due on your bank account.")
    print("Your account balance is ${:.2f}".format(balance))
elif balance < 0:
    print("You have a credit on your account.")
    print("Your account balance is ${:.2f}".format(balance))
else:
    print("No Payment due on your account.")
    print("Thank you for being a loyal customer.")