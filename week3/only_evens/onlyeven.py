def checkNum(num):
    if (num % 2) == 0 and num > 0:
        onlyEven(num)
    else:
        print("Please choose a positive and even number")


def onlyEven(num):

    for currentCount in range(0,num,2):
        print(currentCount)
        
    print("You have arrived at your number")



chosenNum = int(input("Enter a positive even number: "))
checkNum(chosenNum)
#onlyEven(chosenNum)