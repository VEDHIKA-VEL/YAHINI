def Isleapyear(year):
  if(year/4==0 and year/100!=0)or year%400==0:
    return true
year=int(input("enter the year:"))
if Isleapyear(year):
  print("{} is a leap year". format (year))
else:
  print("{} is not leap year". format (year))