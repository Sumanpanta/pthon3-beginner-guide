#this is just a simple practise of all the loops we have learned 
#let's take a random number between 1-30
#User is given 4 attempts to guess the number 
#If the user is able to guess, they win 
#else they loose

import random

random_number = random.randint(1,30)                #randint,randbool etc is the function inside random
MAX_ATTEMPTS = 4
current_attempts = 0

while current_attempts < MAX_ATTEMPTS:
    user_guess = int(input(f"Guess the number: \n ~$"))
    if user_guess == random_number:
        print("Hurrey! You won!!")
        break
    else:
        current_attempts +=1
        
else:
    print("You have no attempt left \n Please try again later!!!")
    
    
##this is also just too simple, you can add as more complexity as possible

    