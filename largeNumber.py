num1 = int(input('Please enter first number: '))
num2 = int(input('Please enter 2nd number: '))
num3 = int(input('Please enter 3rd number: '))

if (num1 > num2) and (num1 > num3):
  print('{0} is greater number'.format(num1))
elif (num2 > num1) and (num2 > num3):
  print('{0} is greater number'.format(num2))
else:
  print('{0} is greater number'.format(num3))