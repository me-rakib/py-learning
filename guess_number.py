from random import randint


def guess(x):
    random_number = randint(1, x)
    guess_num = 0
    while(guess_num != random_number):
        guess_num = int(input("Guess Number: "))
        if(guess_num < random_number):
            print("Too low from actual number")
        elif (guess_num > random_number):
            print("Too high from actual number")
    print(f"Your guess is correct. It's {random_number}")

x = int(input("Select range. From 1 to: "))
guess(x)