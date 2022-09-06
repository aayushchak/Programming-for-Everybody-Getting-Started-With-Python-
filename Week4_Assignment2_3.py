'''Write a program to prompt the user for hours and rate per hour using input to compute gross pay.'''

hr = float(input('Enter Hours: '))
r = float(input('Enter rate per hour: '))

#compute gross pay
gross_pay = hr*r
print('Pay: ',gross_pay)

