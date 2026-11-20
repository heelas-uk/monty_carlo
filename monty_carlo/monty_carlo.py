import random as rand
import time
import questionary
room = 'starting'
coins = 0
game_running = True
bal = 100
quiz = False 
print("__________________________\n\n NEW GAME \n __________________________")
def takewager():
    global wager
    global bal
    global room
    bal2 = bal
    wager = int(input(f"How much do you want to wager? You currently have {bal2}, if you go into negative the mafia will not be pleased. "))
    if wager > bal:
        bal = -1000
        print("You're in debt with the Mafia and can no longer play")
        quit(-10) 
    elif wager <= 0:
        room="staring"
        
    
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
            break
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
        choicec = input("You can chose between Roulette (1), or the Lottery (2), or go back (3) ")
        if choicec == "1":
            room = "roulette"
        elif choicec == "2":
            room = "lottery"
        else:
            room = "starting"
    elif room == "hl":
        print("You have 5 guesses to guess my number between 1-100. Pays 1:1")
        takewager()
        guessed = False
        guess = 0
        num = rand.randint(1, 100)
        while guess <=4 and guessed==False:
           
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
        print("You must input anything in exactly the time stated no more no less. Pays 2:1")
        takewager()   
        stoptime = rand.randint(3,10)
        print(f"You must enter something in {stoptime}s Ready, Set")
        time.sleep(2)
        print("GO!")
        t0= time.perf_counter()
        questionary.press_any_key_to_continue().ask()
        t1 = time.perf_counter()
        t2 = round(t1-t0)
        print(t2)
        if t2 == stoptime:
            bal = bal + wager*3
            print(f"You won yay, balence: {bal}")
            room="skill"
        else:
            bal = bal -wager
            print("You lost :(")
            room="skill"
    elif room == "quiz":
        print("Welcome to this quiz, you must get all 3 questions right, you can only play once, pays 1:1 you must answer all question in 45s")
        takewager()
        if quiz == True:
            print("You have already played too many times, your wager has been returned minus a small fee")
            total = total-1
        t0= time.perf_counter()
        a1 = questionary.select("The chemical element Lithium is named after the country of Lithuania.", choices=["True", "False"]).ask()
        a2 = questionary.select("It was once believed that injecting shark cartilage into people would prevent them from contracting cancer.", choices=["True", "False"]).ask()
        a3= questionary.select("Albert Einstein won a noble prize for his theory of relativity.", choices=["True", "False"]).ask()
        t1 = time.perf_counter()
        t2 = round(t1-t0)
        if t2 > 45:
            print("You took to long sorry :(")
            quiz = True
            bal = bal - wager 
            room = "starting"
        if a1 == "False" and a2 == "True" and a3 == "False":
            bal += wager
            print(f"Yay you won your balence is now {bal}")
            quiz = True
            room = "starting"
        else:
            print("You lost sorry.")
            bal = bal-wager
            quiz = True
            room = "starting"
    elif room == "roulette":
        tofbet = int(input("Would you like to bet on colours (1) or numbers (2)?"))
        if tofbet == 1:
            print("Payout is 1:1 bet 0 to exit")
            takewager()
            rorb = input("Red (r) or Black (b)")
            if rorb == "r":
                num = rand.randint(0,2)
                if num ==1:
                    print("RED WINS YAY")
                    bal += wager
                    room = "starting"
                else: 
                    print("You lost, sad times")
                    bal = bal-wager 
                    room = "starting"
            elif rorb == "b":
                if num ==2:
                    print("BLACK WINS YAY")
                    bal += wager
                    room = "starting"
                    
                else: 
                    print("You lost, sad times")
                    bal = bal - wager
                    room = "starting"
            else:
                print("You handed the money to the dealer who took it and ran away.")
                bal = bal - wager 
                room = "starting"
        else:
            unum = int(input("Enter a number between 0 and 36 "))
            num2 = rand.randint(0,36)
            if unum == num2:
                bal += wager *36 
                print(f"You win!! Your balence is {bal}")
                room = "starting"
            else:
                bal = bal-wager
                print(f"You lost sorry, the number was {num2}")
                room = "starting"
    elif room == "lottery":
        print("Welcome to the lottery, pays 1000000:1")
        input("What numbers do you want to bet on? ")
        takewager()
        print("Sorry you lost")
        bal = bal -wager
        time.sleep(5)
        room = "chance" 
