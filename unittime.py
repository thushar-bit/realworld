day = int(input('enter the number of days'))
hours = int(input('enter the number of hours'))
minutes = int(input('enter the number of min '))
seconds = int(input('enter the number of seconds'))
days = 24 * 3600 * day
hour = 3600 * hours
minute = 60 * minutes
total = days + hour + minute + seconds
print(total, 'seconds')