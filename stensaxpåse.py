import random

points = 0

choises=["sten","sax","påse"]
print("stensaxpåse")


while True:
    print(points)
    player_choise= input()
    bot_chose = random.choice(choises)
    



    if player_choise =="sten"and bot_chose== "sax":
        print("you win")
        points += 1

    if player_choise =="sax"and bot_chose== "påse":
        print("you win")
        points += 1

    if player_choise =="påse"and bot_chose=="sten":
        print("you win")
        points += 1

    if player_choise =="sten"and bot_chose== "påse":
        print("you lose")

        
        

    if player_choise =="påse"and bot_chose== "sax":
        print("you lose")
        points = 0
        

    if player_choise =="sax"and bot_chose== "sten":
        print("you lose")
        points = 0
        
        
        

    if player_choise == bot_chose:
        print("It's a draw")
        points = 0
        
    
    
    









