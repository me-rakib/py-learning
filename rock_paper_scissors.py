from random import choice

def lets_play():
    user = input("Whats your choice? 'r' for rock, 'p for paper, 's' for scissors\n -> ").lower()
    computer = choice(['r', 'p', 's'])

    if (user == computer):
        return "It's a tie."
    elif is_win(user, computer):
        return "You win!"
    else:
        return "You lost!"

def is_win(player, opponent):
    # r>s, s>p, p>r any of these true, return true
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

res = lets_play()
print(res)