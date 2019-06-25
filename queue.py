import sys
startNumber = int(input("Current number? "))
myNumber = int(input ("your number? "))
nextNumber = 1
currentNumber = startNumber + 1
while nextNumber != "0":
    nextNumber = input ("press enter when the next queue number is called; 0 to exit ")
    currentNumber = currentNumber + 1
    print("current number:", currentNumber)
    print("your turn is in x minutes")