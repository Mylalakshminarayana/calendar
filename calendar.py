import calendar
n=int(input("enter the year-"))
m=1
cal=calendar.TextCalendar(calendar.SUNDAY)
i=1
while i<=12:
  cal.prmonth(n,i)
  i=i+1