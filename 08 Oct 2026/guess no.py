# guess the number from 1 to 10 using random function,
#if the number is guessed correctly, print "You guessed it right!",
#else print "Try again!".
import random

number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("You guessed it right!")
else:
    print("Try again!")