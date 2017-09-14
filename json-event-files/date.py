from datetime import timedelta, date
import json

def daterange(start_date, end_date):
    count = 0
    monthVar = start_date.month
    yearVar = start_date.year
    for n in range(int ((end_date - start_date).days)):
        singleday = start_date + timedelta(n)
        if (singleday.weekday() == 1) and (singleday.month == monthVar) and (singleday.year == yearVar):
            count += 1
            if (count == 1) or (count == 3):
                yield singleday
                if count == 3:
                    if monthVar < 12:
                        monthVar += 1
                        count = 0
                    else: 
                        yearVar += 1
                        monthVar = 1
                        count = 0

data = {
        "eventDate":"",
        "eventNum":"",
        "eventName":"",
        "eventFbLink":"",
        "eventInfo":"",
        "eventSlides":"",
        "eventVideos":"",
        "eventGits":"",
        "speakerNames":[""]
    }

for i in daterange(date(2016, 4, 5), date(2017, 3, 8)):
    with open(str(i) + '.json', 'w') as outfile:
        json.dump(data, outfile)

