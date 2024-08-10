import random
word=["euphoria","canvass","console","drawl",
                 "fleet","extenuate","inveterate","pedestrian",
                 "trifling","paradigm","commodious",
           "capricious","Netherlands","Kosovo","Chile","Albanian","fascist",
           "Venezuela","Castile","propelled"]

def randomword():
    a=random.choice(word)
    randomchoice=a.upper()
    return randomchoice
def user():
    name=input("enter your name:")
    print("welcome",name)
    print("you will have 20 chances")
    print("you will have 7 life")
def userchoice():
    x=len(randomword)
    a="_,"*x
    b=a.split(',')
    b.pop()
    guessword=b
    chance=0
    check=1
    repeat=[]
    for i in range(1,20):
        if check == x+1:
            print("YOU WON")
            break
        else:
            get=str(input("guess a word or a letter:"))
            userchoice=get.upper()
            if len(userchoice)>1:
                if userchoice == randomword:
                    print("your guess is correct")
                    print("YOU WON")
                    break
                else:
                    if userchoice != randomword:
                        print("your guess is wrong")
                        print("try again")
                        chance+=1
            elif len(userchoice) == 1:
                if userchoice in repeat:
                    string=''
                    for element in guessword:
                        string+=element
                    print(string)
                else:
                    for j in range(0,x):
                        letter=randomword[j]
                        if userchoice not in randomword:
                            print("your guess is wrong")
                            print("try again")
                            chance+=1
                            break
                        else:
                            if userchoice == letter:
                                guessword[j]=userchoice
                                check=check+1
                                repeat.append(userchoice)
                                string=''
                                for element in guessword:
                                    string+=element
                                print(string)
            life=7-chance
            print("life",life)
            if chance == 1:
                print('''
--------
|       |
|
|
|
|''')
            elif chance==2:
                print('''
--------
|       |
|       0
|
|
|''')
            elif chance==3:
                print('''
--------
|       |
|       0
|       |
|
|''')
            elif chance==4:
                print('''
--------
|       |
|       0
|       |\   
|
|''')
            elif chance==5:
                print('''
--------
|       |
|       0
|      /|\   
|
|''')
            elif chance==6:
                print('''
--------
|       |
|       0
|      /|\    
|        \   
|''')
            elif chance==7:
                print('''
--------
|       |
|       0
|      /|\     
|      / \    
|''')
                print("GAME OVER")
                print("YOU LOST")
                print("the given word is",randomword)
                print("BETTER LUCK NEXT TIME")
                break
            else:
                continue
randomword=randomword()
user()
userchoice()





















































