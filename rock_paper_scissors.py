import random

def play():
    user = input("ROCK! PAPER! SCISSORS! SHOOT! \n'r' for rock, 'p' for paper or 's' for scissors:\n")
    computer = random.choice(["r", "p", "s"])
    
    if user == computer:
        return "It's a tie"
    
    if user_win(user, computer):
        return "You Win!"
    
    return "You LOST!"

def user_win(user, computer):
    if (user == "r" and computer == "s") or (user == "s" and computer == "p") or (user == "p" and computer == "r"):
        return True

print(play())