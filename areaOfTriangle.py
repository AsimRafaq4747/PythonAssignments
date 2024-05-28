a = float(input('Please enter first side of triangle: '))
b = float(input('Please enter Second side of triangle: '))
c = float(input('Please enter Third side of triangle: '))

s = (a + b + c) / 2

areaTriangle = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print('The area of triangle is: {0}' .format(areaTriangle))