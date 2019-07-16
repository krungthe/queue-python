import time

def timeFormat(secs):
    if secs < 60:
        string = str(secs) + "s"
        return string
    elif secs < 3600:
        minutes = secs // 60
        rest = secs % 60
        string = str(minutes) + "m " + str(rest) + "s"
        return string
    else:
        hours = secs // 3600
        minutes = (secs - (hours * 3600)) // 60
        rest = secs -(hours * 3600) - (minutes * 60)
        string = str(hours) + "h " + str(minutes) + "m " + str(rest) + "s"
        return string

string = ""
string2 = ""
startNumber = int(input("Current number? "))
start = time.perf_counter()
myNumber = int(input ("your number? "))
nextNumber = 1
currentNumber = startNumber
while nextNumber != "0":
    nextNumber = input ("Enter when next number is called; 0 to exit\n")
    currentNumber = currentNumber + 1
    end = time.perf_counter()
    timeLeft = int(((end - start) / (currentNumber - startNumber)) * (myNumber - currentNumber))
    print(f"current number: {currentNumber} (-{myNumber - currentNumber})")
    if currentNumber < myNumber :
        string = timeFormat(timeLeft)
        string2 = str(timeFormat((int(end - start))))
        print("ETA: " + string )
        print ("wait: " + string2)
    else:
        print("Your turn! total wait:", str(timeFormat((int(end - start)))))
        quit()
