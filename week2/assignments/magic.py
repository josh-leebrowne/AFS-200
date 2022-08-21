# Input any number and get 2 as an answer.

userPrompt = "Please input a number: "
userNumber = int(input(userPrompt))
# print(userNumber)

makeTwo = (userNumber*3+6)//3-userNumber
print(makeTwo)

