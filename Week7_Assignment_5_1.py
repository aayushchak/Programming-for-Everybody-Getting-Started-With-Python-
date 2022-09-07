'''Write a program that repeatedly prompts a user for integer numbers until the user enters done.
Once done, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid integer number,
catch it with try/except & put an appropriate message & ignoe the number.'''

largest = None
smallest = None

a = []

while True:
    num = input("Enter a number: ")
    try:
        inum = int(num)
    except:
        msg = 'Invalid input'
    if num == "done":
        break
    else:
        a.append(inum)
        
for i in a:
    if largest is None:
        largest = i
    elif i > largest:
        largest = i

for j in a:
    if smallest is None:
        smallest = j
    elif j < smallest:
        smallest = j
print(msg)
print('Maximum is',largest)
print('Minimum is',smallest)
