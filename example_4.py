#题目：输入某年某月某日，判断这一天是这一年的第几天？

year = int(input('year: '))
month = int(input('month: '))
day = int(input('day: '))

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 0 < month <= 12:
    days = months[month - 1]
else:
    print('Month error!')
days += day
leap = 0
if year % 4 == 0:
    leap = 1
if (leap == 1) and (month > 2):
    days += 1
print('it is the %dth day in %d' % (days, year))
