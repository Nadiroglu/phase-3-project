def bye():
    print("Have a nice day!")
    quit()

def start():
    name = input("Welcome to your game, please type in your name: \n")
    initial = input("It will be a tough game LMK if you want to practice more. Type yes to leave or press enter!\n")
    if initial.lower() == "yes":
        bye()
    elif initial == "":
        print(f"Hey {name}! Imagine a game where we tackle questions, find surprises, and face off against competitors. It's gonna be epic!")
        print("Let's get started...")
    else:
        print("Type something valid!!!")

def question4(treasure, health, ada):
    answer = input("What kind of thing is a cup?\n")  
    if answer.lower() == "to drink water":
        print("Wohaa you got it!")
        health += 1
        ada -=1
    else:
        print("Hmm, I think you got a treasure. Would you like to use that?")
        chance = input("Type 'YES' to get a new chance in this question else let's start over\n")
        if chance.lower() == "yes":
            print("As you spend one of your treasure you got a chance for answering this question again")
            print("Here we go")
            question4(treasure - 1, health, ada)
        else:
            question1(treasure, health, ada)

def question3(treasure, health, ada):
    answer = input("What kind of thing is a pen?\n")  
    if answer.lower() == "pen station":
        print("Wohaa you got it!")
        print("🎉🎉🎉 You got a treasure. You can keep it for now and use it later. Or use It now.")
        health += 1
        ada-= 1
        treasure_ques = input("Press 'ENTER' to save it or type 'OPEN' to open it\n")
        if treasure_ques.lower() == "":
            print("Saving things worth sometimes. Here is your next question!")
            question4(treasure + 1, health, ada)
        elif treasure_ques.lower() == "open":
            if health <= 5 and ada <= 5:
                health += 1
                ada += 1
                print(f"You got {health} point. Life is not fair, but let's make a deal. If you got 1 I'll get 1. Ada: {ada} point")
            else:
                health += 0
                ada += 0
                treasure += 1
                print("Oh wow you have a prize for later")
            question4(treasure, health, ada)
    else:
        print("Hmm, I didn't expect that from you, let's try again")
        health -= 1
        ada += 0
        print(f"You: {health} -- Ada {ada}")
        question1(treasure, health, ada)

def question2(treasure, health, ada):
    answer = input("What kind of thing is an apple?\n")  
    if answer.lower() == "apple pie":
        print("Wohaa you got it!")
        health += 0
        ada -= 1
        question3(treasure, health, ada)
    else:
        print("Hmm, I didn't expect that from you, let's try again")
        question1(treasure, health, ada)
        ada += 0
        health -= 1

def question1(treasure, health, ada):
    answer = input("What kind of thing is a pen?\n")  
    if answer.lower() == "pen station":
        print("Wohaa you got it!")
        health += 0
        ada -= 1
        question2(treasure, health, ada)
    else:
        print("Hmm, I didn't expect that from you, let's try again")
        question1(treasure, health, ada)
        health -= 1
        ada += 0

def main():
    start()
    treasure, health, ada = 0, 5, 5
    question1(treasure, health, ada)
    print(f"Final status: Treasure: {treasure}, Health: {health}, Ada: {ada}")

if __name__ == "__main__":
    main()
