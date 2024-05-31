year = int(input('Please enter year for check leap or not: '))

if (year % 4 == 0) and (year % 100 != 0):
  print('{0} is leap a year'.format(year))
else:
  print('{0} is not leap a year'.format(year))