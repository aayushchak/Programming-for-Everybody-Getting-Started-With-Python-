'''Write a program to prompt the user for hours and rate per hour input to compute gross pay.
Pay should be the normal rate upto 40 hours and time-and-a-half for the hourly rate for all hours worked above 40 hours
Use function.'''

#definr function computepay that will calculate the gross pay
def computepay(h,r):
    if h>40:
        pay = (40*r)+((h-40.0)*r*1.5)
    else:
        pay = h*r

    return pay

#take inputs
hrs = input('Enter hours: ')
rate = input('Enter hourly pay: ')

#chck if the inputs are correct
try:
    vhrs = float(hrs)
    vrate = float(rate)
except:
    print('Hour and Rate must be numeric values.')
    quit()

#return gross pay
gross = computepay(vhrs,vrate)
print(gross)
