import time

startNumber = int(input("Current number? "))
start = time.perf_counter()
myNumber = int(input ("your number? "))
nextNumber = 1
currentNumber = startNumber + 1
while nextNumber != "0":
    nextNumber = input ("press enter when the next queue number is called; 0 to exit ")
    end = time.perf_counter()
    timeLeft = ((end - start) / (currentNumber - startNumber)) * (myNumber - currentNumber)
    currentNumber = currentNumber + 1
    print("current number:", currentNumber)
    print("your turn is in %d seconds" % timeLeft)
    print (end - start)