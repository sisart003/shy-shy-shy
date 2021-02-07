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

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could also be high bc low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or Correct (C)').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'Yay!, {guess} is Correct!!')


#numb = input("Max Number")

#guess(int(numb))

computer_guess(10)