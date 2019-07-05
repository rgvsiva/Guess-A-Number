from game import *
l=randnum()
l.sort()
#print(l)
#---------------------------------------

def guess(l,ch):
    if ch<=4:
        print("Attempt No::",ch)
        ch=ch+1
        ask = int(input("Guess A number::"))
        if ask in l:
            print("****Yurekhaa...You won 1 crore laddus****")
            #break
        else:
            po=check(l,ask)
            l1=l[:po]
            l2=l[po:]
            #print(l1)
            #print(l2)
            print('you have ',len(l1),'numbers less than and ',len(l2),'numbers greater than that of your previous number(',ask,')')
            guess(l,ch)
    elif ch==5:
        print('Attempt No::',ch)
        ask = int(input("Guess A number::"))
        if ask in l:
            print("*****************************************\n"
                  "****Yurekhaa...You won 1 crore laddus****\n"
                  '*****************************************')
        else:
            print('*****you are out of chances---You lost the game*****')

ch=1
guess(l,ch)