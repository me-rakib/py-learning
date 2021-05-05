 # here logic is if r>s || s>p || p>r 
 
import random
def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper and 's' for sessors-\n").lower()
    computer = random.choice(['r','p','s'])
    if user == computer:
        return "It's a tie!"
    if is_win(user, computer):
        return "You won!"
    return "You've lost!"

def is_win(player, opponent):
    if (player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' or opponent=='r'):
        return True 

print(play())