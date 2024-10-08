import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print(f"Sorry, the correct number is higher than {guess}")
        elif guess > random_number:
            print(f"Sorry, the correct number is lower than {guess}")
    print(f"Congrats! {guess} is the correct number!")
    
    
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback =input(f"Is {guess} to High (h), too low (l), or correct (c)? ")
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"Good job Computer, it was {guess}!")
    

#guess(1000)
computer_guess(1000)