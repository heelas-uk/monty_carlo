import random as rand 
import time
room = 'starting'
coins = 0
game_running = True
bal = 100
print("__________________________\n\n NEW GAME \n __________________________")
while game_running == True and bal >= 0:
    if room == "starting":
        choicea = int(input("You are faced with a choice games of skill (1), or of luck (2)  "))
        if choicea == 1:
            room="skill"
        elif choicea == 2:
            room = "chance"
        else:
            print("Silly")
            room = "staring"
    elif room == "skill":
        choiceb = input("You can chose between a higher or lower game (1), a time estimation game (2), trivea (3), or go back (4)  ")
        if choiceb == "1":
            room = "hl"
        elif choiceb == "2":
            room = "time"
        elif choiceb == "3":
            room = "quiz"
        else:
            room = "starting"
    elif room == "chance":
        choicec = input("You can chose between Roulette (1), Slots (2), Lottery (3), or go back (4)")
        if choicec == "1":
            print("")
        else: 
            room = "starting"
    elif room == "hl":
        print("You have 5 guesses to guess my number between 1-100. Pays 2:1")
        wager = int(input(f"How much do you want to wager? You currently have {bal}, if you go into negative the mafia will not be pleased. "))
        if wager > bal:
            bal = -1000
            print("You're in debt with the Mafia and can no longer play")
            quit(-10)
        guessed = False
        guess = 0
        num = rand.randint(1, 100) 
        print(num)
        while guess <=5 and guessed==False:
            
            uguess = int(input("You're guess please "))
            if uguess > num:
                print("My number is smaller")
                guess += 1
            elif uguess<num:
                print("My number is bigger")
                guess += 1
            else:
                print("A very well done, you're correct")
                bal = bal +wager 
                print(f"Your balence is now {bal} because you gained {wager}")
                guessed = True
                 
        if guessed == False:
            print("You lost")
            bal = bal - wager 
            room = "skill"
            
        else:
            room="skill"
    elif room =="time":
        print("You must input anything in exactly the time stated no more no less. Pays 5:1")
        wager = int(input(f"How much do you want to wager? You currently have {bal}, if you go into negative the mafia will not be pleased. "))
        if wager > bal:
            bal = -1000
            print("You're in debt with the Mafia and can no longer play")
            quit(-10)       
        stoptime = rand.randint(3,10)
        print(f"You must enter something in {stoptime}s Ready, Set")
        time.sleep(2)
        print("GO!")
        t0= time.perf_counter()
        input("Enter anyhting ")
        t1 = time.perf_counter()
        t2 = round(t1-t0)
        print(t2)
        if t2 == stoptime:
            bal = bal + wager*5
            print(f"You won yay, balence: {bal}")
            room="skill"
        else:
            bal = bal -wager 
            print("You lost :(")
            room="skill"
        


            

                



