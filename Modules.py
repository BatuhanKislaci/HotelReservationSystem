def date(startDate, howManyDays):
    days = []
    today = startDate.split(".") 
    today[0],today[1],today[2] = int(today[0]),int(today[1]),int(today[2])
    i = 0
    while i < int(howManyDays): 
        todaysString = ""
        if today[0] > 30:
          today[0] = 1
          today[1] = today[1] + 1 
          if today[1] > 12:
            today[1] = 1
            today[2] = today[2] + 1
        todaysString = f"{today[0]}.{today[1]}.{today[2]}"
        days.append(todaysString)
        today[0] += 1
        i += 1

    return days

def extendedDate(startdate,oldDays,extendedDays):
  DaysList1 = date(startdate,oldDays)
  DaysList2 = date(startdate,oldDays+extendedDays)

  for d in DaysList1:
    DaysList2.remove(d)
  
  return DaysList2


