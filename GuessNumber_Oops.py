'''
    AUTHOR : RGV SIVA
    DATE   : 12-07-19
    THEME  : GUESS A NUMBER GAME
'''
from random import *
#---------------------------------------------
class GuessNumber:
    def __init__(self):
        self.ran_num=[]
        self.randnum()
        self.ran_num.sort()
    def randnum(self):
        while len(self.ran_num)<10:
            n=randrange(1,50,1)
            if n not in self.ran_num:
                self.ran_num.append(n)
    #----------------------------------------------
    def check(self,ask):
        pos=0
        for i in self.ran_num:
            if ask > i:
                pos = pos + 1
            else:
                break
        return pos
    #---------------------------------------
    def won(self):
        print("*****************************************\n"
              "****Yurekhaa...You won 1 crore laddus****\n"
              '*****************************************')
    #------------------------------------------
    def guess(self,chance=1):
        #print(self.ran_num)
        if chance<=4:
            print("Attempt No::",chance)
            ask = int(input("Guess A number::"))
            if ask in self.ran_num:
                self.won()
                print(self.ran_num)
            else:
                pos=self.check(ask)
                print('you have ',len(self.ran_num[:pos]),'numbers less than and ',len(self.ran_num[pos:]),'numbers greater than that of your previous guess(',ask,')')
                self.guess(chance+1)
        elif chance==5:
            print('Attempt No::',chance)
            ask = int(input("Guess A number::"))
            if ask in self.ran_num:
                self.won()
                print(self.ran_num)
            else:
                print('*****you are out of chances---You lost the game*****')
                print(self.ran_num)
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
guess=GuessNumber()
guess.guess()
#-------------------------------------------------------------------------------