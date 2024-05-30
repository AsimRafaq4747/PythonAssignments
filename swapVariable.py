val1 = int(input('Please enter your 1st number: '))
val2 = int(input('Please enter your 2nd number: '))

val3 = val1
val1 = val2
val2 = val3

print('We have swapped you values 1st: {0} and 2nd: {1}'.format(val1,val2))