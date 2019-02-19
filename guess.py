import random
play = True
while play:
    y=random.randrange(1,21)
    x=int(input("enter a no. between 1 & 20: "))
    loop = True
    while loop:
        if x<y:
            x=int(input("higher number...enter another number: "))
        if x>y:
            x=int(input("lower number...enter another number: "))
        if x==y:
            print("YOU GOT IT...")
            loop=False
    if input("play again?")=="no":
        play=False
