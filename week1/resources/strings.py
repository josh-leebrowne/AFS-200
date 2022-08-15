"""
The string object in Python has a number of very useful methods.  These methods return a value and do not modify the original string. This is because strings in Python are unmutable, which means that they can not be changed.

Method			Description
----------------------------------------------
capitalize()	Converts the first character to upper case
find()			Searches the string for a specified value and 
				returns the	position of where it was found
isalpha()		Returns True if all characters in the string are in the alphabet(a-z)
				Example of characters that are not alphabet letters: (space)!#%&? etc.
isdigit()		Returns True if all characters in the string are digits
islower()		Returns True if all characters in the string are lower case
isnumeric()		Returns True if all characters in the string are numeric
lower()			Converts a string into lower case
replace()		Returns a string where a specified value is replaced with a
				specified value
split()			Splits the string at the specified separator, and returns a list
startswith()	Returns true if the string starts with the specified value
title()			Converts the first character of each word to upper case
upper()			Converts a string into upper case
"""


message = "Python is a fun language to learn"
print("capitalize()", message.capitalize())
print("find('fun')", message.find("fun"))
print("isalpha()", message.isalpha())