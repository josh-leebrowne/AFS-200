"""
The general format of the while loop in Python uses the key word WHILE followed by the true/false condition statment and then a colon.
A block of code begins on the next line and it is indented.

Format: 
while <condition>:
    statement
	statement
	statement
	...
    
"""

def countDown(start):

    while start > 0:
        print(start)
        start -= 1

    print("Blast Off!")

startingNum = int(input("Enter the countdown starting number: "))
countDown(startingNum)


#----------------------------------------------

def countDown(start):
    while True:
        print(start)
        start -= 1
        if(start == 0):
            print("Blast Off!")
            break

startingNum = int(input("Enter the countdown starting number: "))
countDown(startingNum)

#----------------------------------------------

def countDown(start):
	continueLoop = True
	while continueLoop:
		print(start)
		start -= 1
		if (start == 0):
			print("BLAST OFF!")
			continueLoop = False

startingNum = int(input("Enter the countdown starting number: "))
countDown(startingNum)