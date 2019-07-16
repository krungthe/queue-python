def timeFormat(secs):
    if secs < 60:
        return secs
    elif secs<3600:
        minutes = secs//60
        rest = secs % 60
        string =str(minutes) + ":" + str(rest)
        return string
    else:
        hours = secs // 3600
        minutes = (secs - (hours * 3600)) // 60
        rest = secs -(hours * 3600) - (minutes * 60)
        string = str(hours) + ":" + str(minutes) + ":" + str(rest)
        return string

seconds = int(input("How many seconds? "))
string = timeFormat(seconds)
print(string)