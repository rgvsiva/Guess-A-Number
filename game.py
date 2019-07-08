from random import *
#----------------------------------------------
def randnum():
    num=[]
    while len(num)<10:
        n=randrange(1,50,1)
        if n not in num:
            num.append(n)
    return num
#----------------------------------------------
def check(l,ask):
    pos = 0
    for i in l:
        if ask > i:
            pos = pos + 1
        else:
            break
    return pos
#------------------------------------------------------------
print('**********************Guess A Number*********************')
print('***********************Instructions**********************')
print('-------------Guess any number between 1 & 50------------\n'
      '---we will give you 10 random nummbers between 1 & 50---\n'
      '-----we will display those 10 by the end of the game-----\n'
      '--------------------You have 5 chances-------------------\n'
      '----We will give you "Hints" according to your guess-----\n'
      '*********************************************************\n'
      '*****************-----Get Ready folks-----***************\n'
      '*********************************************************'
      '')

