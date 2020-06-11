#!/usr/bin/env python
# coding: utf-8

@author: slowc
"""


# In[ ]:


import random

comp_list = ['Rock', 'Paper', 'Scissors']

c = 0
u = 0
print("Points at the starting are: \n Computer = ", c, "\n User = ", u)

while c < 3 and u < 3:
    comp = random.choice(comp_list)
    user = input("Enter your choice: ")
    if comp == 'Rock' and user == 'Paper':
        u += 1
        print("Computer chose: ", comp," \nYou gained a point!")
        print("New score is:\n Computer = ", c, "\n User = ", u)
    elif comp == 'Rock' and user == 'Scissors':
        c += 1
        print("Computer chose: ", comp, " \nComputer gained a point!")
        print("New score is:\n Computer = ", c, "\n User = ", u)
    elif comp == 'Paper' and user == 'Scissors':
        u += 1
        print("Computer chose: ", comp, " \nYou gained a point!")
        print("New score is:\n Computer = ", c, "\n User = ", u)
    elif comp == 'Paper' and user == 'Rock':
        c += 1
        print("Computer chose: ", comp, " \nComputer gained a point!")
        print("New score is:\n Computer = ", c, "\n User = ", u)
    elif comp == 'Scissors' and user == 'Rock':
        u += 1
        print("Computer chose: ", comp, " \nYou gained a point!")
        print("New score is:\n Computer = ", c, "\n User = ", u)
    elif comp == 'Scissors' and user == 'Paper':
        c += 1
        print("Computer chose: ", comp, " \nComputer gained a point!")
        print("New score is:\n Computer = ", c, "\n User = ", u)
    else:
        print("It's a clash! No one gains any point.")

if u >= 3:
    print("You defeated the computer.!!!!! :)")
elif c >= 3:
    print("You just got defeated. :(")
else:
    print("Wait. Something is not right.")


# In[ ]:




