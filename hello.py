print("first python project")
import random
'''
1 for snake
-1 for water
0 for gun
'''

comp=random.choice([-1,0,1])
player=(input("enter "))
dic={"s":1,"w":-1,"g":0}
reversedict={1:"snake",-1:"water",0:"gun"}

you=dic[player]
print("comp choose",reversedict[comp])


if (comp==you):
    print('draw')
else:
    if (comp==-1 and you==1):
        print("you win")
    elif (comp==-1 and you==0):
        print("you lose")
    elif (comp==1 and you==-1):
        print("you lose")
    elif (comp==1 and you==0):
        print("you win")
    elif (comp==0 and you==-1):
        print("you lose")
    elif (comp==0 and you==1):
        print("you win")
    else:
        print("error")
    

