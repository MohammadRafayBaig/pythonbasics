# import random

# jackpot=random.randint(1,100)

# guess=int(input("Enter the guess"))
# counter=1

# while guess!=jackpot:
#     if guess < jackpot:
#         print("Guess higher")
#     else:
#         print("guess lower")
    
#     guess=int(input("Enter the guess again"))
#     counter+=1
# print("Correct ans")
# print("total guess",counter)

import random

jackpot=random.randint(1,100)
guess=int(input("Guess kar bhai="))

counter=1

while guess!=jackpot:
    if guess < jackpot:
        print("Guess higher")
    else:
        print("Guess lower")
        
    guess=int(input("Guess again="))
    counter+=1
print("Correct guess")
print("Guess Count",counter)