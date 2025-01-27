#guess the number
import random 
import time

number=random.randint(1, 100) 
guess=int(input("Enter your Guess: ") )
	


def intro():
	print("May I ask you for your name?")
	global name
	name = input() 
	print(name + ", we are going to play a game. I am thinking of a number between 1 and 100")
	if(number%2==0):
		x='even'
	else:
		x='odd'
	print("\nNumber is ", x)

	print("Go ahead. Guess!")

def pick():

   

		if guess<=100 and guess>=1:
		
				if guess<number:
						print("The guess of the number that you have entered is too low")
				if guess>number:
						print("The guess of the number that you have entered is too high")

				
			

		if guess>100 or guess<1: 
			print("Please enter a number between 1 and 100")
        



intro()
pick()
if guess == number:
	print('Good job! You guessed my number')

if guess != number:
	print('Nope. The number I was thinking of was ' + str(number))



        
            


