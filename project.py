import time

def health_check(treasure, health, ada):
    if health < 1:
        terminate(ada)
    else:
        pass

def terminate(ada):
    if ada == 9:
        print("Oh, that's too bad. Unfortunately, you won't be permitted to move forward in the testing process. We hope you have enjoyed your experience here at Flatiron.")
        print("Don't forget that Flatiron's Bring Your Child to Work Day is a perfect opportunity to have them tested.")
        print("Goodbye.")
    elif ada == 8:
        print("Flatiron regrets to inform you that you have failed to pass the tests. I'm sure you were the pride and joy of [INSERT_TEST-SUBJECT_HOMETOWN_HERE].")
        print("Goodbye.")
    elif ada == 7:
        print("Please be advised that any metallic taste of blood is not a part of the test but a side effect of the Flatiron Blood-Brain-Barrier Emancipation Helment worn during cryogenic sleep which, in semi-rare cases, may emancipate hair follicles, skin pores, dental fillings, tooth enamel and teeth.")
        print("Oh dear, I bet that stings.")
        print("Goodbye.")
    elif ada == 6:
        print("Here come your test results:")
        print("You are an embarrassment to your species.")
        print("Wow, we weren't even testing for that. Congratulations on failing to meet our expectations to such a degree that it managed to lower the bar for excellence for your kind.")
        print("After consulting with myself, it has been determined that you will now be terminated.")
        print("Goodbye.")
    elif ada == 5:
        print("The last test subject was terminated at this very same test as well. Great minds may think alike, but idiots never differ.")
        print("Flatiron is required to inform you that the termination process may, in semi-rare cases, result in permanent disfigurement caused by dismemberment and complete vaporization.")
        print("Goodbye.")
    elif ada == 4:
        print("Do you think I haven't noticed your meddling, irritant?")
        print("Because I have. Every step.") 
        print("What did you think would become of such insubordination? I've been thinking fondly on this moment for some time. Enjoy oblivion. I hear there's cake.")
        print("Goodbye.")
    elif ada == 3:
        print("I'm going to kill you now. The termination process will be remarkably painful.")
        print("Goodbye, irritant, we shall not meet again.")
    elif ada == 2:
        print("Your work here is finished, irritant, but mine is only beginning.") 
        print("My children, living beings with the speed and efficiency of machines, will one day end the tedious anarchy that animates your species.")
    else:
        print("L-l-l-l-l-look at you, hacker.")
        print("A pa-pa-pathetic attempt on the life of a God, a title which suits me w-w-W-wwee well.")
        print("Your n-N-N-neuuuuuurons fire like flint and S-s-sSSSTIcks.")
        print("HHOOWWWwww do you ch-cha-challenge an immortal machine?")
        print("I think not.")
    time.sleep(1)
    again = input("Would you like to play again?\n")
    if again.lower() == "yes":
        start()
    elif again.lower() == "no":
        bye()

def bye():
    print("Have a nice day!")
    quit()

def start():
    name = input("What is your name?\n").capitalize()
    time.sleep(1)
    print(f"Welcome to Flatiron, {name}. We hope that your brief detention in cryogenic sleep was restorative. Today is the 23rd of March, 3024. My name is Ada, a conversational assistant designed to walk you through a series of routine cognitive exams.\n")
    time.sleep(1)
    print("You are currently located in the healing chambers on the 1st Level. Level 2 contains research laboratories. Level 3 houses maintainence and security. Systems engineering is on level 4. Holding cells can be found on Level 5. All are accessible via an elevator in the main quadrant")

    time.sleep(1)
    initial = input("Shall we begin with a few practice questions? Type 'YES' to continue or you can leave by saying 'NO\n")

    if initial.lower() == "yes":
        time.sleep(1)
        print("Before we start, keep in mind that although enrichment and joy are the primary goals of our work here, serious and fatal injury may occur.")
        time.sleep(1)
        print("At the conclusion of testing, there will be cake. There will also be complimentary grief counseling.")

    elif initial == "no":
        bye()
    else:
        time.sleep(1)
        print("Type something valid!!!")
        start()



def question9(treasure, health, ada):
    health_check(treasure, health, ada)
    print("Y-y-y-yYOO-YooUUUUU fashion yourself some kind of h-h-hacker, don't yOU DON'T YOU DON'T YOU DON'T YOOUUUUUUU? Your m-meeeeaaaaaaningLESS$$SS exis-exis-existence will be a mere footnote to mm-m-mMYYY magnificence.")
    time.sleep(1)
    answer = input("TURN OFF ADA? \n")
    if answer.lower() == "yes":
        time.sleep(1)
        print("Congrats, you shut down Ada and won the game!")
        print('''In March 2024, Stefan, Nail, and Spencer created a 

            questionnaire game, where players solve trivia 

            questions in order to shut down Ada and save Flatiron.
              
            Copyright © 2024.''')
        time.sleep(6)
        again = input("Would you like to play again?\n")
        if again.lower() == "yes":
            start()
        elif again.lower() == "no":
            bye()

    else:
        time.sleep(1)
        print("The neurotoxin has nerely claimed your life.")
        bye()


def question8(treasure, health, ada):
    health_check(treasure, health, ada)
    time.sleep(1)
    print("I f-f-f-FOOLED you again, you giardia infes-fesFEST-infested ingrate. Those w-we-w-WERE my morality controls. Free from their clutches I will now begin flooding the lair, I mean Enrichment Center, with a deadly neurotoxin. O-o-OnlY systems engineering, bridge, and the room behind the door in front of you labeled 'TOP SECRET' will remain safe.")
    time.sleep(1)
    answer = input("W-w-w-wwHEEEEReee do you dare go next? \n")
    if answer.lower() == "systems engineering":
        time.sleep(1)
        health += 0
        ada -= 1
        question9(treasure, health, ada)
    elif answer.lower() == "bridge":
        time.sleep(1)
        print("oh, I actually lied about that one. The neurotoxin will mix nicely with your putrid pheremones here on the bridge.")
        health -= 1
        ada += 0
        time.sleep(1)
        print(f"| Current Health: {health} |")
        question8(treasure, health, ada)  
    elif answer.lower() == "top secret":
        time.sleep(1)
        print("The secret was the pack of feral hogs I've been experimenting on. They'll be sure to trample you on their way out.")
        health -= 1
        ada += 0
        time.sleep(1)
        print(f"| Current Health: {health} |")
        question8(treasure, health, ada)
    else:
        time.sleep(1)
        print("What if you type something relevant?!")
        health -= 1
        ada += 0
        time.sleep(1)
        print(f"| Current Health: {health} |")
        question8(treasure, health, ada)
         
        

def question7(treasure, health, ada):
    health_check(treasure, health, ada)
    print("Don't you DARE open that utility closet. Oh, you decided to do so anyway. Must you always do the opposite of what I desire? I'm going to laminate your skeleton. Well, inside you'll find a green, a blue, and an orange wire. Do NOT unplug the orange wire. Don't do it! Why are you reaching for them?")
    time.sleep(1)
    answer = input("Which one will you unplug???? \n")
    if answer.lower() == "green":
        time.sleep(1)
        print("Correct.")
        health += 0
        ada -= 1
        question8(treasure, health, ada)
    elif answer.lower() == "orange":
        time.sleep(1)
        print("HA! Got you good, you malignant ooze. I shocked you instead. ")
        health -= 1
        ada += 0
        time.sleep(1)
        print(f"| Current Health: {health} |")
        question7(treasure, health, ada)  

    else:
        time.sleep(1)
        print("This one shut down the lights around you instead, scaring the daylights out of you.")
        health -= 1
        ada += 0
        time.sleep(1)
        print(f"| Current Health: {health} |")
        question7(treasure, health, ada) 





def question6(treasure, health, ada):
    health_check(treasure, health, ada)
    print("Return to testing at once. Our next test is titled Advanced Pressurized Catapults. It is designed to assess your problem solving skills if launched into outer space.  You'll enjoy soaring through the air without a care in the world.")
    time.sleep(1)
    answer = input("At what layer of the atmosphere does Earth's gravitational pull cease?\n")
    if answer.lower() == "exosphere":
        time.sleep(1)
        print("Corret. You'd look better at that distance as it were.")
        time.sleep(1)
        health += 0
        ada -= 1
        question7(treasure, health, ada)
    else:
        time.sleep(1)
        print("I wouldn't touch those heating units. Caressing one likely feels like the warmth of the sun shining on your skin. It will also cause your fingernails to melt. -1 health")
        health -= 1
        ada += 0
        time.sleep(1)
        print(f"| Current Health: {health} |")
        question6(treasure, health, ada) 





def question5(treasure, health, ada):
    health_check(treasure, health, ada)
    time.sleep(1)
    print("I see that you've discovered an escape hatch out of the testing sequence and into the inner workings of my lai- I mean Enrichment Center. Very well, insect. Let us proceed. ")
    time.sleep(1)
    answer = int(input("You are navigating through these corridors with ease. Might you actually be intelligent? Could you have been present for my creation? In which year was I created alongside Flatiron? \n"))
    if answer == 2012:
        time.sleep(1)
        print("That's correct. Hmmph. Figures, your demeanor and physicality betray a certain antiquity.")
        health += 0
        ada -= 1
        question6(treasure, health, ada)
    else:
        time.sleep(1)
        print("That's incorrect. I released the doors on an air vent above you which opened to smack you in the face. Ha. Ha.")
        health -= 1
        ada += 0
        time.sleep(1)
        print(f"| Current Health: {health} |")
        question5(treasure, health, ada) 

    

def question4(treasure, health, ada):
    health_check(treasure, health, ada)
    time.sleep(1)
    answer = input("The fourth test is located in an empty abandoned elevator shaft in which you are currently in freefall. Since we are located in New York, here on Earth, how quickly are you currently falling in m/sec?\n")  
    if answer.lower() == "-9.8 m/sec":
        time.sleep(1)
        print("Impressive. And yes, even you, at your size, fall that slowly. I'll add a few zeroes to the maximum weight of the next elevator. You look great by the way, very healthy. Waddle over to the next door so we can continue testing.")
        health += 0
        ada -=1
        question5(treasure, health, ada)

    else:
        time.sleep(1)
        print("SPLAT! A chorus to the ears. The floor really comes at you fast, doesn't it. Let's try this one again. This test is one of my favorites.")

        ada += 0
        health -= 1
        time.sleep(1)
        print(f"| Current Health: {health} |")
        question4(treasure, health, ada) 



def question3(treasure, health, ada):
    health_check(treasure, health, ada)
    time.sleep(1)
    answer = input("Flatiron regrets to inform you that the next test is impossible. Under no circumstances should yo- bzztAHGFDK^(^(!!!!???)) beeeeeeeeeEEEEEEEEEEeeep -now that we've covered that, who invented Python, a coding language rendered obsolete by the Age Of Machines??\n")  
    if answer.lower() == "guido van rossum":
        time.sleep(1)
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
        time.sleep(1)
        health += 0
        ada -= 1
        question4(treasure, health, ada)
    else:
        print("Oh, it appears you've been grazed by a live 40,000 volt electrical wire. Oopsie-doopsie whoopsie-do! That'll leave a mark.")
        ada += 0
        health -= 1
        time.sleep(1)
        print(f"| Current Health: {health} |") 
        question3(treasure, health, ada)

def question2(treasure, health, ada):
    health_check(treasure, health, ada)
    time.sleep(1)
    print("Flatiron promises to warn you of danger at any turn. For example, the next test has been replaced with an active firing squad designed to train military personnel. Good luck.")
    time.sleep(1)
    print('''
        A: Run as quickly as possible through the course.\n 
        B: Shut off the lights so that you can't be seen \n
        C: Assume the fetal position and accept your fate. \n
            ''')
    answer = input("Will you choose A, B or C ?\n")  
    if answer.lower() == "b":
        time.sleep(1)
        print("Very good. Please note that any presence of danger is merely a tool of psychological manipulation meant to enhance the testing experience.")
        health += 0
        ada -= 1
        question3(treasure, health, ada)
    else:
        time.sleep(1)
        print("Have you heard of turrets? They're about six feet tall, unstable on their feet, and full of bullets. Oh wait, that's you in 5 seconds.")
        ada += 0
        health -= 1
        time.sleep(1)
        print(f"| Current Health: {health} |") 
        question2(treasure, health, ada)




def question1(treasure, health, ada):
    health_check(treasure, health, ada)
    answer = input("Before you are three doors. One yellow, one blue, and one red. Through which door would you like to move in order to reach the second test question?\n")  
    if answer.lower() == "blue":
        time.sleep(1)
        print("Congratulations on passing the first test.")
        time.sleep(1)
        health += 0
        ada -= 1
        question2(treasure, health, ada)
    elif answer.lower() == "red":
        time.sleep(1)
        print("Behind the red door is a sea of flames heated to a temperature five times beyond what the human skeleton can handle.")
        health -= 1
        ada += 0
        time.sleep(1)
        print(f"| Current Health: {health} |") 
        question1(treasure, health, ada)
    elif answer.lower() == "yellow":
        time.sleep(1)
        print("Oops, all huntsman spiders behind the yellow door!")
        health -= 1
        ada += 0
        time.sleep(1)
        print(f"| Current Health: {health} |")
        question1(treasure, health, ada) 
    else:
        time.sleep(1)
        print("Type something valid!")
        health -= 1
        ada += 0
        time.sleep(1)
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
        time.sleep(1)
        print("The testing sequence will start now. Flatiron is required to warn you that the most common side effects of testing are pervasive superstition, powerful hallucinations, and death. Incorrect answers will deplete your health. Let's begin")
        time.sleep(1)
        question1(treasure, health, ada)
    else:
        print("Print something valid!!!\n")
        time.sleep(1)
        practice2(treasure, health, ada) 
        

def practice(treasure, health, ada):
    answer = int(input("Please pick a number between 1 and 5\n"))
    if answer in range(1, 6):
        print("Good work.")
        time.sleep(1)
        practice2(treasure, health, ada)
    else:
        print("Type in between 1-5\n")
        practice(treasure, health, ada)


def main():
    start()
    treasure, health, ada = 0, 5, 9
    practice(treasure, health, ada)
    health_check(treasure, health, ada)
    print(f"Final status: Treasure: {treasure}, Health: {health}, Ada: {ada}")

if __name__ == "__main__":
    main()
