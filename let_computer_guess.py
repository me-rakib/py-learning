from random import randint

def guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess_num = randint(low, high)
        else:
            guess_num = low
        feedback = input(f"If {guess_num} is lower, enter 'L' for upper enter 'U', for correct enter 'C': ").lower()
        if feedback == 'l':
            low = guess_num + 1
        elif feedback == 'u':
            high = guess_num - 1
    print(f"Guessed correctly. It's {guess_num}.")

x = int(input("Your number belongs from 1 to: "))
guess(x)
        