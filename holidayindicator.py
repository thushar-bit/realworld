months =  input('enter the month and the day')
month = months[2:]
day = int(months[0:2])
New_year = 'january'
canada = 'july'
christmas = 'december'
if month == New_year:
    if day == 1:
        print('New year')
elif month == canada:
    if day == 1:
        print('cannada day')
elif month == christmas:
    if day == 25:
        print('christmas day')
else:
    print('you have entered wrong day')
