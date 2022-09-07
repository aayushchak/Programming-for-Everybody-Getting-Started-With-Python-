'''Write a program to prompt the user for hours and rate per hour to compute the gross pay.
If hour is more than 40, the rate becomes 1.5 times the initial rate.
Use try/except to catch errors.'''

#take input
hrs = input('Enter hours: ')
rate = input('Enter hourly rate: ')

#catch errors if any
try:
    vhrs = float(hrs)
    vrate = float(rate)
except:
    vhrs = -1
    vrate = -1

#calculate gross pay if the values are correct or else diaplay appropriate message
if (vhrs>0 and vrate>0):
    if(vhrs>40):
        pay = (40*vrate)+((vhrs-40.0)*vrate*1.5)
    else:
        pay = vhrs*vrate

    print(pay)
else:
    print('Hour and rate must be numbers')
