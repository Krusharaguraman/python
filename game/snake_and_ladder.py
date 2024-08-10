import random
dice=random.randint(1,6)
userpoints=0
randompoints=0
for i in range (1,52):
    if i==51:
        print("chance over no one wins")
        break
    randomdice=random.randint(1,6)
    userdice=random.randint(1,6)
    randomchoice=randomdice
    print("computer:",randomchoice)
    chance=int(input("continue:yes=1/no=0"))
    if chance==1:
        userchoice=userdice
        userpoints+=userchoice
        randompoints+=randomchoice
        if randompoints>50 or userpoints>50:
            if userpoints>50:
                userpoints-=userchoice
            elif randompoints>50:
                randompoints-=randomchoice
            print("you:",userchoice)
        else:
            print("you:",userchoice)
    else:
        randompoints+=randomchoice
        if randompoints>50:
            userpoints+=0
            randompoints-=randomchoice
    if randompoints==50:
        print("COMPUTER WON")
        break
    elif userpoints==50:
        print("YOU WON")
        break
    else:
        if userpoints==2 or randompoints==2:
            if userpoints==2:
                print("you on Ladder")
                userpoints=17
            else:
                print("computer on Ladder")
                randompoints=17
        elif userpoints==9 or randompoints==9:
            if userpoints==9:
                print(" you on Ladder")
                userpoints=24
            else:
                print("computer on Ladder")
                randompoints=24
        elif userpoints==15 or randompoints==15:
            if userpoints==15:
                print("you on Ladder")
                userpoints=29
            else:
                print("computer on Ladder")
                randompoints=29
        elif userpoints==30 or randompoints==30:
            if userpoints==30:
                print("you on Ladder")
                userpoints=43
            else:
                randompoints=43
                print("computer on Ladder")
        elif userpoints==26 or randompoints==26:
            if userpoints==26:
                print("snake bites you")
                userpoints=5
            else:
                print("snake bites computer")
                randompoints=5
        elif userpoints==35 or randompoints==35:
            if userpoints==35:
                print("snake bites you")
                userpoints=8
            else:
                print("snake bites computer")
                randompoints=8
        elif userpoints==45 or randompoints==45:
            if userpoints==45:
                print("snake bites you")
                userpoints=27
            else:
                print("snake bites computer")
                randompoints=27
        elif userpoints==48 or randompoints==48:
            if userpoints==48:
                print("snake bites you")
                userpoints=25
            else:
                print("snake bites computer")
                randompoints=25
        else:
             pass
    print("your place:",userpoints,"computer place:",randompoints)






















    
