import time

startNumber = int(input("Current number? "))
start = time.perf_counter()
myNumber = int(input ("your number? "))
nextNumber = 1
currentNumber = startNumber
while nextNumber != "0":
    nextNumber = input ("press enter when the next queue number is called; 0 to exit ")
    currentNumber = currentNumber + 1
    end = time.perf_counter()
    timeLeft = ((end - start) / (currentNumber - startNumber)) * (myNumber - currentNumber)
    print("current number:", currentNumber)
    if currentNumber < myNumber :
        if timeLeft < 60 :
            print("your turn is in %d seconds" % timeLeft)
        else :
            minutesLeft = int(timeLeft / 60)
            secondsLeft = int(timeLeft - (minutesLeft * 60))
            timeLeftString = "{} minutes, {} seconds."
            print("your turn is in " + timeLeftString.format(minutesLeft, secondsLeft))
    print ("waiting for ", int(end - start), "seconds so far") 
