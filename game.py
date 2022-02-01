import random
n=3
i=0
computer=0
gamer=0
option=["snake","water","gun"]
print("SNAKE WATER GUN GAME.........")
print(option)
for i in range(n):
    choice=random.choice(option)
    print("enter ur turm")
    turn=input()
    if choice==turn:
        print("tie","computer's choice was",choice)
    elif choice==(option[0]):
        if turn==option[1]:
            computer=computer+1
            print("you lose this round","computer's choice was",choice)
        else:
            gamer=gamer+1
            print("you won this round","computer's choice was",choice)
    elif choice==option[1]:
        if turn==option[2]:
            computer=computer+1
            print("you lose this round","computer's choice was",choice)
        else:
            gamer=gamer+1
            print("you won this round","computer's choice was",choice)
    else:
        if turn==option[1]:
            computer=computer+1
            print("you lose this round","computer's choice was",choice)
        else:
            gamer=gamer+1
            print("you won this round","computer's choice was",choice)
if computer==gamer:
    print("its a tie","ur score",gamer,"computer score",computer)
elif computer>gamer:
    print("u loose","ur score",gamer,"computer score",computer)
else:
    print("congrats u won","ur score",gamer,"computer score",computer)
