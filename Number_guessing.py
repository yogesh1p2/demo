#!/usr/bin/python
#Code to guess a number
import random

def get_an_integer():
    while True:
        try:
	    x = int(input("Enter a number : "))
	    print(x)
	    False
	    return x
	except:
	    print("Please enter an integer")

x = random.randint(1,20) 
li = []
print("Guess the number between the range 1 to 20")

while True:
    y = get_an_integer()
    li.append(y)
    if y == x:
        print("You got it!")
	print("The correct number is : ",y)
	print("Number of tries you made")
	print(li)
	break
    elif y > x:
        print("Incorrect! try again")
	print("Number is smaller than ",y)
    else:
        print("Incorrect! try again")
	print("Number is greater than ",y)
