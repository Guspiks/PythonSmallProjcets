import random
RPS_Array=["rock","paper","scissors"]
cpu_win=0
player_win=0
game_end=0
while game_end==0:
    Rand_Value=random.randint(0,2)
    RPS_input=input("Co wybierasz?, Wpisz 'rock', 'paper' lub 'scissors': ")
    RPS_Value=RPS_Array[Rand_Value]
    if RPS_input==RPS_Value:
        print(RPS_input+"="+RPS_Value)
        print("Remis gramy dalej")
        print("Wynik \nPlayer: "+str(player_win)+"\n CPU: "+str(cpu_win))
    elif RPS_Value=="rock" and RPS_input=="paper":
        print(RPS_input+">"+RPS_Value)
        print("Gratulacje zdobyłeś punkt")
        player_win+=1
        print("Wynik \nPlayer: "+str(player_win)+"\n CPU: "+str(cpu_win))
    elif RPS_Value=="rock" and RPS_input=="scissors":
        print(RPS_input+"<"+RPS_Value)
        print("CPU zdobyło punkt")
        cpu_win+=1 
        print("Wynik \nPlayer: "+str(player_win)+"\n CPU: "+str(cpu_win))
    elif RPS_Value=="paper" and RPS_input=="rock":
        print(RPS_input+"<"+RPS_Value)
        print("CPU zdobyło punkt")
        cpu_win+=1 
        print("Wynik \nPlayer: "+str(player_win)+"\n CPU: "+str(cpu_win))
    elif RPS_Value=="paper" and RPS_input=="scissors":
        print(RPS_input+">"+RPS_Value)
        print("Gratulacje zdobyłeś punkt")
        player_win+=1
        print("Wynik \nPlayer: "+str(player_win)+"\n CPU: "+str(cpu_win))
    elif RPS_Value=="scissors" and RPS_input=="rock":
        print(RPS_input+">"+RPS_Value)
        print("Gratulacje zdobyłeś punkt")
        player_win+=1
        print("Wynik \nPlayer: "+str(player_win)+"\n CPU: "+str(cpu_win))
    elif RPS_Value=="scissors" and RPS_input=="paper":
        print(RPS_input+"<"+RPS_Value)
        print("CPU zdobyło punkt")
        cpu_win+=1
        print("Wynik \nPlayer: "+str(player_win)+"\n CPU: "+str(cpu_win))
    else:
        print("Błąd w podanych wartościach")
    if cpu_win==3 or player_win==3:
        game_end=1
    else:
        game_end=0
if cpu_win==3:
    print("Wynik \nPlayer: "+str(player_win)+"\n CPU: "+str(cpu_win))
    print("Przegrałeś spróbuj ponownie")
elif player_win==3:
    print("Wynik \nPlayer: "+str(player_win)+"\n CPU: "+str(cpu_win))
    print("Wygrałeś gratulacje")
else:
    print("Coś poszło nie tak")



