import time
def bye():
    print("Have a nice day!")
    quit()

def start():
    name = input("It will be a tough game: But before You should type your name! 🧌 \n").capitalize()

    print(f"Welcome to Flatiron, {name}. We hope that your brief detention in cryogenic sleep was restorative. Today is the 23rd of March, 3024. My name is Ada, a conversational assistant designed to walk you through a series of routine cognitive exams.\n")
    print("You are currently located in the healing chambers on the 1st Level. Level 2 contains research laboratories. Level 3 houses maintainence and security. Systems engineering is on level 4. Holding cells can be found on Level 5. All are accessible via an elevator in the main quadrant")

    initial = input("Shall we begin with a few practice questions? Type 'YES' to continue or you can leave by saying 'NO\n").lower()

    if initial.lower() == "yes":
        print(f"Hey {name}! Imagine a game where we tackle questions, find surprises, and face off against competitors. It's gonna be epic!")
        time.sleep(2)
        print("Let's get started...")
        print("Before we start, keep in mind that although enrichment and joy are the primary goals of our work here, serious and fatal injury may occur.")
        time.sleep(3)
        print("At the conclusion of testing, there will be cake. There will also be complimentary grief counseling.")

    elif initial == "no":
        bye()
    else:
        print("Type something valid!!!")
        start()



def question9(treasure, health, ada):
     print("Y-y-y-yYOO-YooUUUUU fashion yourself some kind of h-h-hacker, don't yOU DON'T YOU DON'T YOU DON'T YOOUUUUUUU? Your m-meeeeaaaaaaningLESS$$SS exis-exis-existence will be a mere footnote to mm-m-mMYYY magnificence.")
     time.sleep(1)
     answer = input("TURN OFF ADA?")
     if answer.lower() == "yes":
        print("Congrats, it was nice to play with you however you shut me down!")
        print('''In March 2024, Stefan, Nail, and Spencer created a 
              
              captivating Questionary game, where players challenge the
              
               computer in trivia, surprises, and competition.
              
               Copyright © 2024. They beat the computer in this thrilling adventure!''')
        time.sleep(6)
        again = input("Would you like to play again?")
        if again.lower() == "yes":
            start()
        elif again.lower() == "no":
            bye()

     else:
        print("The neurotoxin has nerely claimed your life.")
        bye()


def question8(treasure, health, ada):
     print("I f-f-f-FOOLED you again, you giardia infes-fesFEST-infested ingrate. Those w-we-w-WERE my morality controls. Free from their clutches I will now begin flooding the lair, I mean Enrichment Center, with a deadly neurotoxin. O-o-OnlY systems engineering, bridge, and the room behind the door in front of you labeled 'TOP SECRET' will remain safe.")
     time.sleep(1)
     answer = input("W-w-w-wwHEEEEReee do you dare go next?")
     if answer.lower() == "systems engineering":
        health += 0
        ada -= 1
        question9(treasure, health, ada)
     elif answer.lower() == "bridge":
        print("oh, I actually lied about that one. The neurotoxin will mix nicely with your putrid pheremones here on the bridge.")
        health -= 1
        ada += 0
        print(f"| Current Health: {health} |")
        question8(treasure, health, ada)  
     elif answer.lower() == "top secret":
        print("The secret was the pack of feral hogs I've been experimenting on. They'll be sure to trample you on their way out.")
        health -= 1
        ada += 0
        print(f"| Current Health: {health} |")
        question8(treasure, health, ada)
     else:
         print("What if you type something relevant?!")
         health -= 1
         ada += 0
         print(f"| Current Health: {health} |")
         question8(treasure, health, ada)
         
        

def question7(treasure, health, ada):
     print("Don't you DARE open that utility closet. Oh, you decided to do so anyway. Must you always do the opposite of what I desire? I'm going to laminate your skeleton. Well, inside you'll find a green, a blue, and an orange wire. Do NOT unplug the orange wire. Don't do it! Why are you reaching for them?")
     time.sleep(1)
     answer = input("Which one will you unplug????")
     if answer.lower() == "green":
        print("Corret. You love yourself too much!!!")
        health += 0
        ada -= 1
        question8(treasure, health, ada)
     elif answer.lower() == "orange":
        print("HA! Got you good, you malignant ooze. I shocked you instead. ")
        health -= 1
        ada += 0
        print(f"| Current Health: {health} |")
        question7(treasure, health, ada)  

     else:
        print("This one shut down the lights around you instead, scaring the daylights out of you.")
        health -= 1
        ada += 0
        print(f"| Current Health: {health} |")
        question7(treasure, health, ada) 





def question6(treasure, health, ada):
    print("Return to testing at once. Our next test is titled Advanced Pressurized Catapults. It is designed to assess your problem solving skills if launched into outer space.  You'll enjoy soaring through the air without a care in the world.")
    time.sleep(1)
    answer = input("At what layer of the atmosphere does Earth's gravitational pull cease?")
    if answer.lower() == "exosphere":
        print("Corret. You'd look better at that distance as it were.")
        health += 0
        ada -= 1
        question7(treasure, health, ada)
    else:
        print("I wouldn't touch those heating units. Caressing one likely feels like the warmth of the sun shining on your skin. It will also cause your fingernails to melt. -1 health")
        health -= 1
        ada += 0
        print(f"| Current Health: {health} |")
        question6(treasure, health, ada) 





def question5(treasure, health, ada):
    print("I see that you've discovered an escape hatch out of the testing sequence and into the inner workings of my lai- I mean Enrichment Center. Very well, insect. Let us proceed. ")
    time.sleep(2)
    answer = int(input("You are navigating through these corridors with ease. Might you actually be intelligent? Could you have been present for my creation? In which year was I created alongside Flatiron? \n"))
    if answer == 2012:
        print("That's correct. Hmmph. Figures, your demeanor and physicality betray a certain antiquity.")
        health += 0
        ada -= 1
        question6(treasure, health, ada)
    else:
        print("That's incorrect. I released the doors on an air vent above you which opened to smack you in the face. Ha. Ha.")
        health -= 1
        ada += 0
        print(f"| Current Health: {health} |")
        question5(treasure, health, ada) 

    

def question4(treasure, health, ada):
    answer = input("The fourth test is located in an empty abandoned elevator shaft in which you are currently in freefall. Since we are located in New York, here on Earth, how quickly are you currently falling in m/sec?\n")  
    if answer.lower() == "-9.8 m/sec":
        print("Impressive. And yes, even you, at your size, fall that slowly. I'll add a few zeroes to the maximum weight of the next elevator. You look great by the way, very healthy. Waddle over to the next door so we can continue testing.")
        health += 0
        ada -=1
        question5(treasure, health, ada)

    else:
        print("SPLAT! A chorus to the ears. The floor really comes at you fast, doesn't it. Let's try this one again. This test is one of my favorites.")

        ada += 0
        health -= 1
        print(f"| Current Health: {health} |")
        question4(treasure, health, ada) 

        # chance = input("Type 'YES' to get a new chance in this question else let's start over\n")

        # if chance.lower() == "yes":
        #     print("As you spend one of your treasure you got a chance for answering this question again")
        #     print("Here we go")
        #     question4(treasure - 1, health, ada)

        # else:
        #     question1(treasure, health, ada)




def question3(treasure, health, ada):
    answer = input("Flatiron regrets to inform you that the next test is impossible. Under no circumstances should yo- bzztAHGFDK^(^(!!!!???)) beeeeeeeeeEEEEEEEEEEeeep -now that we've covered that, who invented Python, a coding language rendered obsolete by the Age Of Machines??\n")  
    if answer.lower() == "guido van rossum":
        print("Excellent. Even in an environment of extreme pessimism you remained resolute. We'll make a note of that in the section of your file meant for commendations. Oh, my, there's a lot of empty space in this section, isn't there.")
        # time.sleep(1)
        # print("Wait a second...")
        # time.sleep(2)
        # print("🎉🎉🎉 You got a treasure. You can keep it for now and use it later. Or use It now.")
        # health += 1
        # ada-= 1
        # treasure_ques = input("Press 'ENTER' to save it or type 'OPEN' to open it\n")
        # if treasure_ques.lower() == "":
        #     print("Saving things worth sometimes. Here is your next question!")
        #     question4(treasure + 1, health, ada)
        # elif treasure_ques.lower() == "open":
        #     if health <= 5 and ada <= 5:
        #         health += 1
        #         ada += 1
        #         print(f"You got {health} point. Life is not fair, but let's make a deal. If you got 1 I'll get 1. Ada: {ada} point")
        #     else:
        #         health += 0
        #         ada += 0
        #         treasure += 1
        #         print("Oh wow you have a prize for later")
        #     question4(treasure, health, ada)
        health += 0
        ada -= 1
        question4(treasure, health, ada)
    else:
        print("Oh, it appears you've been grazed by a live 40,000 volt electrical wire. Oopsie-doopsie whoopsie-do! That'll leave a mark. -1 health")
        ada += 0
        health -= 1
        print(f"| Current Health: {health} |") 
        question3(treasure, health, ada)

def question2(treasure, health, ada):
    print("Flatiron promises to warn you of danger at any turn. For example, the next test has been replaced with an active firing squad designed to train military personnel. Good luck.")
    time.sleep(1)
    print('''
        A: Run as quickly as possible through the course.\n 
        B: Shut off the lights so that you can't be seen \n
        C: Assume the fetal position and accept your fate. \n
            ''')
    answer = input("Will you choose A, B or C ?\n")  
    if answer.lower() == "b":
        print("Very good. Please note that any presence of danger is merely a tool of psychological manipulation meant to enhance the testing experience.")
        health += 0
        ada -= 1
        question3(treasure, health, ada)
    else:
        print("Have you heard of turrets? They're about six feet tall, unstable on their feet, and full of bullets. Oh wait, that's you in 5 seconds. health -1")
        ada += 0
        health -= 1
        print(f"| Current Health: {health} |") 
        question2(treasure, health, ada)




#!!!
def question1(treasure, health, ada):
    answer = input("Before you are three doors. One yellow, one blue, and one red. Through which door would you like to move in order to reach the second test question?\n")  
    if answer.lower() == "blue":
        print("Congratulations on passing the first test. Please be advised that any metallic taste of blood is not a part of the test but a side effect of the Flatiron Blood-Brain-Barrier Emancipation Helment worn during cryogenic sleep which, in semi-rare cases, may emancipate hair follicles, skin pores, dental fillings, tooth enamel and teeth")
        health += 0
        ada -= 1
        time.sleep(3)
        question2(treasure, health, ada)
    elif answer.lower() == "red":
        print("Behind the red door is a sea of flames heated to a temperature five times beyond what the human skeleton can handle. -1 health.")
        health -= 1
        ada += 0
        print(f"| Current Health: {health} |") 
        question1(treasure, health, ada)
    elif answer.lower() == "yellow":
        print("Oops, all huntsman spiders behind the yellow door! -1 health.")
        health -= 1
        ada += 0
        print(f"| Current Health: {health} |")
        question1(treasure, health, ada) 
    else:
        print("Type something valid!")
        health -= 1
        ada += 0
        print(f"| Current Health: {health} |")
        question1(treasure, health, ada)

def practice2(treasure, health, ada):
    computer_brands = [
    "Apple",
    "Dell",
    "HP (Hewlett-Packard)",
    "Lenovo",
    "Asus",
    "Acer",
    "Microsoft",
    "MSI",
    "Samsung",
    "Toshiba",
    "Sony",
    "Alienware",
    "Gateway",
    "Razer",
    "LG",
    "Google",
    "IBM",
    "Panasonic",
    "Fujitsu",
    "Huawei",
    "Xiaomi",
    "Chuwi",
    "Gigabyte",
    "System76",
    "Vizio",
    "Aorus",
    "Corsair",
    "CyberPowerPC",
    "Origin PC",
    "Sager",
    "ZOTAC",
    "Maingear",
    "Velocity Micro",
    "Eurocom",
    "Clevo",
    "EVGA",
    "Schenker",
    "Falcon Northwest",
    "Digital Storm",
    "Puget Systems",
    "iBuyPower",
    "Xidax",
    "AVADirect",
    "Azom",
    "Aftershock PC",
    "Hasee",
    "Vaio",
    "Medion",
    "Nexoc",
    "PC Specialist",
    "Terrans Force",
    "ECS",
    "Maxdata",
    "Motion Computing",
    "Panda Security",
    "Parallels",
    "QNAP",
    "ViewSonic",
    "Zebra Technologies"
]

    answer = input("Let's move onto another. What kind of computer brand are you using?\n")
    if answer.lower() in [brand.lower() for brand in computer_brands]:
        print("Well done!")
        time.sleep(2)
        print("The testing sequence will start now. Flatiron is required to warn you that the most common side effects of testing are pervasive superstition, powerful hallucinations, and death. Incorrect answers will deplete your health. Let's begin")
        question1(treasure, health, ada)
    else:
        print("Print something valid!!!")
        time.sleep(1)
        practice2(treasure, health, ada) 
        

def practice(treasure, health, ada):
    answer = int(input("Please pick a number between 1 and 5\n"))
    if answer in range(1, 6):
        print("Nice try!!!")
        practice2(treasure, health, ada)
    else:
        print("Type in between 1-5")
        practice(treasure, health, ada)


def main():
    start()
    treasure, health, ada = 0, 5, 5
    practice(treasure, health, ada)
    print(f"Final status: Treasure: {treasure}, Health: {health}, Ada: {ada}")

if __name__ == "__main__":
    main()
