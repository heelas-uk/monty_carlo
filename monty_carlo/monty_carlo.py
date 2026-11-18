import random as rand 
room = 'starting'
coins = 0
game_running = True
bal = 100

while game_running == True:
    if room == "starting":
        choicea = input("You are faced with a choice games of skill (1), or of luck (2)")
        if choicea == 1:
            room="skill"
        elif choicea = 2:
            room = "chance"
        else:
            print("Silly")
            room = "staring"
    elif room == "skill":
