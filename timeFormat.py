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

seconds = int(input("How many seconds? "))
string = timeFormat(seconds)
print(string)