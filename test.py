#test
from ctypes.wintypes import PINT
import time

int = 10

#proper setup for a try&except in a loop
while True: 
    num = input('pick a number \n')
    try:
        if(float(num) == 1):
            print('cool')
            break
    except:
        print('i said a number dummy :3')


#0 in the minimum and 55 is max, it will add the -5 to i every loop and will only run the code when i is in that range
for i in range(0,55,5):
    print(i)
