"""
A variable is a name that represents a value stored in the computer's memory.

In Python, the assignment statement is used to create a variable and have it reference a piece of data. 

An assignment statement is written in the following general format:

variable = expression (value)

with the equal sign used as the assignment operator.
"""

from re import A


appleSold = 10

"""									|    |
	applesSold   -------------->	| 10 |
									|____|
	

Note that the variable name "appleSold" is a reference or pointer to the memory location where 10 is stored.

You can not use a variable name until have it has been assigned a value.
"""

x = 5
print(x)

a = 5
b = a
a = 7 
print(a)
print(b)


"""
There are rules when naming variables and these include:
• You cannot use one of Python’s key words as a variable name. 
• A variable name cannot contain spaces.
• The first character must be one of the letters a through z, A through Z, or an underscore character (_).
• After the first character you may use the letters a through z or A through Z, the digits 0 through 9, or underscores.
• Uppercase and lowercase characters are distinct. 

Other naming conventions include choosing a variable name that is meaningful to the value to be stored and its purpose in the program.  If you variable name is a combination of multiple words, it helpful to seperate the words either using an underscore (_) or camel case where the first word begins with a lowercase letter and each additional word starts with an uppercase letter.
"""

x = 10
applesSold = 10
apples_sold = 10


a = 5
print(a)
print(type(a))

a = 5.0
print(a)
print(type(a))

a = "5.0"
print(a)
print(type(a))