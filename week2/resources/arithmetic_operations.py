"""
Python offers the following math operator.

Symbol		Operation			Description
----------------------------------------------
+ 			Addition 			Adds two numbers
_ 			Subtraction 		Subtracts one number from another
* 			Multiplication 		Multiplies one number by another
/ 			Division 			Divides one number by another and gives the result as a
                                floating-point number
// 			Integer division 	Divides one number by another and gives the result as
								an integer
% 			Remainder 			Divides one number by another and gives the remainder
** 			Exponent 			Raises a number to a power


These operators are performed on operands which may be numerical values or variables.
"""

print(8 + 3)
print(8 - 3)

a=7
b=2
print('Addition : ', a + b)
print('Subtraction : ', a - b)
print('Multiplication : ', a * b)
print('Division (float) : ', a / b)
print('Integer Division : ', a // b)
print('Modulus : ', a % b)
print('Exponent : ', a ** b)



x = "Hello"
y = "World"
z = x + " " + y

print(z)