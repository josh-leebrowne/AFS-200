"""
The general format of the FOR loop in Python uses the key word FOR followed by a variable name, followed by the word "in" followed by the sequence of data items and then ends with a colon.  This is called the for statement.
A block of code begins on the next line and it is indented.

Format: 
for <var> in <iterable>:
    statement
	statement
	statement
	...
"""

def countDown():

    for currentCount in [5, 4, 3, 2, 1]:
        print(currentCount)

    print("Blast Off")

countDown()

#----------------------------------------------

def welcomeGuests(guestNames):
    for guest in guestNames:
        print("Welcome", guest)
    
guests = []
guests.append(input("Please enter the name of a guest: "))
guests.append(input("Please enter the name of a guest: "))
guests.append(input("Please enter the name of a guest: "))

welcomeGuests(guests)

#----------------------------------------------

"""
range(start, stop[, step])

start
The value of the start parameter (or 0 if the parameter was not supplied)

stop
The value of the stop parameter

step
The value of the step parameter (or 1 if the parameter was not supplied)

for (x=0; x < 10; x++) 
	<loop body>

"""

for x in range(0,10,1):
    print(x)

#----------------------------------------------

def countDown(start):

    for currentCount in range(start,-1,-1):
        print(currentCount)

    print("Blast Off!")

countDown(10)

#----------------------------------------------

def count(stop):
    for number in range(1,stop+1):
        print(number)

stoppingNum = int(input("Count to?: "))
count(stoppingNum)



