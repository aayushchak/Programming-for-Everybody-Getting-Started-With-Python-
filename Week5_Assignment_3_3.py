'''Write a program to prompt for a score between 0.0 & 1.0.
If the score is out of range, print an error.
If the score is between 0.0 & 1.0, print the grade using the following table:
>= 0.9 Grade A
>= 0.8 Grade B
>= 0.7 Grade C
>= 0.6 Grade D
< 0.6 Garade F'''

#take input
sc = input('Enter score: ')

#check for valid input
try:
    vsc = float(sc)
except:
    print('Score must be a neumeric value between 0.0 & 1.0')
    quit()

#if input is valid, evaluate the grade
if(vsc>0.0 and vsc<0.6):
    print('F')
elif(vsc>=0.6 and vsc<0.7):
    print('D')
elif(vsc>=0.7 and vsc<0.8):
    print('C')
elif(vsc>=0.8 and vsc<0.9):
    print('B')  
elif(vsc>=0.9 and vsc<=1.0):
    print('A')
else:
    print('Score must be between 0.0 & 1.0')
