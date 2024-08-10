import random
rock='r'
paper='p'
scissor='s'
print("rock",rock)
print("paper",paper)
print("scissor",scissor)
objects=(rock,paper,scissor)
computer=0
user=0
for i in range (0,5):
    randomchoice=random.choice(objects)
    choice=input("choose your choice")
    userchoice=choice.lower()
    if randomchoice==userchoice:
        computer+=0
        user+=0
    elif randomchoice=='r' and userchoice=='s':
        computer+=1
    elif randomchoice=='p' and userchoice=='r':
        computer+=1
    elif randomchoice=='s' and userchoice=='p':
        computer+=1
    elif randomchoice=='s' and userchoice=='r':
        user+=1
    elif randomchoice=='r' and userchoice=='p':
        user+=1
    elif randomchoice=='p' and userchoice=='s':
        user+=1
    else:
        print("your choice is not available")
        computer+=1
    print("computer choice",randomchoice,"user choice",userchoice)
    print("computer points",computer,"user points" ,user)
if computer>user:
    print("computer won")
elif computer<user:
    print("user won")
else:
    print("match draw")
