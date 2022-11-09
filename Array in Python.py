#Array in Python 

#We can Import array in Python using 3 ways - 
#import array
#import array as arr
#from array import *

import array as arr

a = arr.array('i',[1,2,3,4])   #'i' is used to define the type of array which is an integer and [1,2,3,4] is the length of the array
print("The newly created array is: ", end="")
for i in range(4):
    print(a[i], end="")
print()

#adding an integer to the array
x = int(input("Enter the value to want to add in the array: "))
a.append(x)
print("After adding the number the final array is: ", end="")
print(a)


#Reversing an array 

a.reverse()
print(a)