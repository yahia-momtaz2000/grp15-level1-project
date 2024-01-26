# this will show how to use datetime in python
import calendar
from datetime import datetime # from module datetime import datetime class
from dateutil import relativedelta # from module dateutil import relativedelta class

print('---- get today datetime -----')
today = datetime.now()
print(today)

print('----- get date or time, or day or month or year or hours or minutes or seconds ---')
print(today.date())
print(today.date().day)
print(today.date().month)
print(today.date().year)

print(today.time())
print(today.time().hour)
print(today.time().minute)
print(today.time().second)

print('-- Formatting dates, Convert from datetime to str, using function strftime() function  ------------')
print(type(today))
print(today.strftime('%d-%m-%y-%Y'))
print(today.strftime('%b-%B'))
print(today.strftime('%a-%A'))
print(today.strftime('%H-%M-%S')) # time in 24 formats
print(today.strftime('%I-%M-%S %p')) # time in 24 formats

print('-----------  To get Custom date -  24 May 2023 -------')
print('--- 1. way : using datetime class object  ---')
custom_date = datetime(2021, 5, 24)
print(custom_date)

print('---- 2. way : using date as str variable, '
      'convert from str to datetime, using function strptime() ----')
new_custom_date = '24-5-2023'
print(type(new_custom_date))
new_custom_date = datetime.strptime(new_custom_date, '%d-%m-%Y')
print(new_custom_date)
print(type(new_custom_date))

print('--------------- Comparison between dates --------------------')
print(today.date(), custom_date.date())
if today > custom_date:
    print('Today is newer than custom date')
elif today < custom_date:
    print('Today is older than custom date')
else:
    print('date are equal')


print('-------- Get the difference between 2 dates in days as a total -------')
days_difference = today - custom_date
print('Difference between 2 dates = ',days_difference.days)

print('------- Get the difference between 2 dates in year, months ,days, .. ho.')
print(today.date(), custom_date.date())
differece = relativedelta.relativedelta(today, custom_date)
print(differece)
print('years = ', differece.years,' months = ',differece.months, ', days = ',differece.days)

print('-------  Adding or Subtracting 2 years, 4 months, 10 days on a date ----------------')
print(today)
new_date = today + relativedelta.relativedelta(years = 2, months= 4, days=10)
print(new_date)

print('---------- Get the first day | last day of the Current Month-----')
first_day = today + relativedelta.relativedelta(day = 1)
last_day = today + relativedelta.relativedelta(day = 31)
print(first_day)
print(last_day)

print('----- Find the nearest Sunday from today -------')
nearest_sunday = today + relativedelta.relativedelta(weekday = calendar.SUNDAY)
print(nearest_sunday)

print('----- Find the nearest 2nd Sunday from today -------')
nearest_2ndsunday = today + relativedelta.relativedelta(weekday = calendar.SUNDAY, weeks=1)
print(nearest_2ndsunday)

print('----------- Find the first sunday from the beginning of the current month ------ ')
nearest_currmonth_sunday = today + relativedelta.relativedelta(day = 1, weekday=calendar.SUNDAY)
print(nearest_currmonth_sunday)


print('----------- Find the first sunday from the beginning of the next month ------ ')
nearest_nextmonth_sunday = today + relativedelta.relativedelta(months=1, day=1,  weekday=calendar.SUNDAY)
print(nearest_nextmonth_sunday)

print('----------Find the first sunday from the begining of the current year -----')
current_year_sun = today + relativedelta.relativedelta(weekday=calendar.SUNDAY, month=1,day=1 )
print(current_year_sun)

print('----------Find the first sunday from the begining of the next year -----')
next_year_sun = today + relativedelta.relativedelta(weekday=calendar.SUNDAY, years=1, month=1, day=1)
print(next_year_sun)
