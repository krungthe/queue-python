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
startNumber = ""
myNumber = ""
firstQuestion = "Current number? "
secondQuestion = "Your number? "

while startNumber.isdigit() == False:
    startNumber = input(firstQuestion)
    firstQuestion = "Current NUMBER? "

startNumber = int(startNumber)
start = time.perf_counter()

while myNumber.isdigit() == False:
    myNumber = input(secondQuestion)
    secondQuestion = "Your NUMBER? "

myNumber = int(myNumber)
nextNumber = 1
currentNumber = startNumber
while nextNumber != "q":
    nextNumber = input ("Enter when next number is called; q to exit\n")
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
