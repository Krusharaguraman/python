import random
lower=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbol=['~','`','!','@','#','$','%','^','&','*','(',')','[',']','{','}',';','\'',':','.','<','\ ','/','?',]
number=['1','2','3','4','5','6','7','8','9','0']
All=[]
password=''
for i in range(1,3):
    a=random.choice(lower)
    b=random.choice(upper)
    c=random.choice(symbol)
    d=random.choice(number)
    All.append(a)
    All.append(b)
    All.append(c)
    All.append(d)
#print(password)
for element in All:
    password+=element
print('the generated password is',password)    
