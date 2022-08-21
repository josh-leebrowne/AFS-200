"""
A relational operator determines whether a specific relationship
exists between two values. 

Operation		Meaning
----------------------------------------------
> 				Greater than
< 				Less than
>= 				Greater than or equal to
<= 				Less than or equal to
== 				Equal to
!= 				Not equal to
"""

# a = 7
# b = 2
# x = 2
# y = 2

# print(a > b)
# print(a < b)
# print(a >= b)
# print(x <= b)
# print(x == y)
# print(a != b)




"""
Logical Operators

Operation			Description
----------------------------------------------
and	 				Connects two Boolean expressions into 
					one compound expression. Both expressions 
					must be true for the compound expression to be true.
or 					Connects two Boolean expressions into 
					one compound expression. One or both expressions 
					must be true for the compound expression to be true.
not 				Reverses the truth of the operand it is placed in front of.
"""


a = 7
b = 2
x = 6
y = 6

print( (a > b) and (a < b) )
print( (x == y) and (y == x) )

print( (a > b) or (a < b) )

print( not (x == y) )