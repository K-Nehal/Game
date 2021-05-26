#!/usr/bin/env python
# coding: utf-8

# # Snake water gun Game
Following  are  the  rules  of  the  game: 

1. Snake vs. Water: Snake drinks the water hence wins.
2. Water vs. Gun: The gun will drown in water, hence a point for water. 
3. Gun vs. Snake: Gun will kill the snake and win. 
# In[1]:


def snakeWaterGun (comp,player):
    if comp == player:
        return None
    elif comp == 's':
        if player == 'w':
            return False
        elif player == 'g':
            return True
    elif comp =='w':
        if player == 's':
            return True
        elif player =='g':
            return False
    elif comp == 'g':
        if player == 's':
            return False
        elif player == 'w':
            return True      


# In[3]:


import random

comp = print ('comp Turn: Snake(s) Water(w) or Gun(g)?')
randNo = random.randint(1,3)
if randNo ==1 : 
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
player = input ('your Turn : Snake(s) Water(w) Gun(g) \t')
a = snakeWaterGun (comp, player)
print(f'Computer chose {comp}')
print(f"You chose {player}")


if a == None:
    print('The game is a tie.')
elif a:
    print('You Win!')
else:
    print('You lose!')


# In[ ]:




