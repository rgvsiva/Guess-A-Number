'''
    AUTHOR : RGV SIVA
    DATE   : 10-07-19
    THEME  : GUESS A NUMBER GAME
'''
from random import *
#----------------------------------------------
def randnum():
    num=[]
    while len(num)<10:
        n=randrange(1,50,1)
        if n not in num:
            num.append(n)
    num.sort()
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
#---------------------------------------
def won():
    print("*****************************************\n"
          "****Yurekhaa...You won 1 crore laddus****\n"
          '*****************************************')
#------------------------------------------
def guess(l=randnum(),ch=1):
    print(l)
    if ch<=4:
        print("Attempt No::",ch)
        ask = int(input("Guess A number::"))
        if ask in l:
            won()
            print(l)
        else:
            pos=check(l,ask)
            print('you have ',len(l[:pos]),'numbers less than and ',len(l[pos:]),'numbers greater than that of your previous number(',ask,')')
            guess(l,ch+1)
    elif ch==5:
        print('Attempt No::',ch)
        ask = int(input("Guess A number::"))
        if ask in l:
            won()
            print(l)
        else:
            print('*****you are out of chances---You lost the game*****')
            print(l)
#------------------------------------------------------------
print('**********************Guess A Number********************\n'
      '***********************Instructions*********************\n'
      '-------------Guess any number between 1 & 50------------\n'
      '---we will give you 10 random nummbers between 1 & 50---\n'
      '-----we will display those 10 by the end of the game-----\n'
      '--------------------You have 5 chances-------------------\n'
      '----We will give you "Hints" according to your guess-----\n'
      '*********************************************************\n'
      '*****************-----Get Ready folks-----***************\n'
      '*********************************************************')
guess()
#-------------------------------------------------------------------------------

