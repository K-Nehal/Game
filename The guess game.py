#!/usr/bin/env python
# coding: utf-8

# # The guess game
We are going to write a program that generates a random number and asks the user to guess it.

If the players guess is higher than the actual number, the program displays,"Lower number please",

similarly if the users guess it to low, the program prints, "Highr number please"

When the user's guess is the correct number, the program displays the number of guesses the player used to arrive at the number.

Hint :
Use the random module.
# In[19]:


import random
randNumber= random.randint(1,100)

userGuess = None 
guesses = 0
while(userGuess != randNumber):
    userGuess = int(input("Enter your guess:"))
    guesses +=1
    if(userGuess==randNumber):
        print("you guessed it right!")
    else:
        if(userGuess>randNumber):
            print("you guessed it wrong! Enter a smaller number")
        else:
            print("you guessed it wrong! Enter a larger number")
            
print(f"You gussesed the number in {guesses} guesses")

print('The random number is \t',randNumber)


# In[ ]:




