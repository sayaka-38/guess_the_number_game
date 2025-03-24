import sys
import random

n = int(input('Please enter the smallest number\n'))
m = int(input('Please enter the largest number\n'))

if n > m:
    print('Error! Minimum value is greater than maximum value.')
    sys.exit()

random_number = random.randint(n, m)
count = m - n

print('Game start.')
print(f'Guess the number within {count} tries!')
print('Please enter your guess:')

for i in range(count):
    user_input = int(input())
    if user_input == random_number:
        print('Congratulations! You guessed it right!')
        sys.exit()
    else:
        print('Try again.')

print(f'Defeat... The correct number was {random_number}.')