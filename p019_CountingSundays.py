import datetime
from datetime import timedelta

firstDay = datetime.date(1901, 1, 1)
secondDay = datetime.date(2000, 12, 31)
oneDay = timedelta(1)

sum = 0
while (firstDay <= secondDay):
    if (firstDay.weekday() == 6 and firstDay.day == 1):
        sum += 1
        print firstDay
    firstDay += oneDay

print sum