import time

startNumber = int(input("Current number? "))
start = time.perf_counter()
myNumber = int(input ("your number? "))
nextNumber = 1
currentNumber = startNumber
while nextNumber != "0":
    nextNumber = input ("Enter when next number is called; 0 to exit\n")
    currentNumber = currentNumber + 1
    end = time.perf_counter()
    timeLeft = ((end - start) / (currentNumber - startNumber)) * (myNumber - currentNumber)
    print(f"current number: {currentNumber} (-{myNumber - currentNumber})")
    if currentNumber < myNumber :
        if timeLeft < 60 :
            print("ETA: %d seconds" % timeLeft)
        else :
            minutesLeft = int(timeLeft / 60)
            secondsLeft = int(timeLeft - (minutesLeft * 60))
            #timeLeftString = "{}m {}s"
            print(f"ETA: {minutesLeft}m {secondsLeft}s");
        print (f"wait: {int(end - start)}s\n");
    else:
        print("Your turn! total wait:", int(end -start),"s");
        quit()
