# Building a simple game where a user take a guess 6 times for the right number.

import random

print('Hello Player. I am thinking of a number between 1 & 20 ')
name = input('What is your name? >> ')

secretNo = random.randint(1, 20)


#User will guess a number 6 times
for trials in range(1, 7):
    print(f'Welcome {name}, please take a guess ')
    guess = int(input("> "))

    if guess < secretNo:
        print('Your guess is too low.')
    elif guess > secretNo:
        print('Your guess is too high')
    else:
        break
if guess == secretNo:
    print(f'Good job {name}! You guessed the right no: {guess}')
else:
    print(f'The number was {secretNo}')

