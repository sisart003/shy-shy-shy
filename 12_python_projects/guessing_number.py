import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a Number Between 1 up to {x}: '))
        if guess < random_number:
            print('A little bit More!')
        elif guess > random_number:
            print('Too high')
    
    
    print(f'Congrats, you guessed it {random_number} is Correct! FIGHTING!')

numb = input("Max Number")

guess(int(numb))