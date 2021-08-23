import os.path      # used for saving and loading data
import sys          # imports the sys library
import time         # imports the time library
import pygame       # imports the pygame library


pygame.mixer.init() #This initializes the mixer for the audio that will be playing in the game.

file_exists = os.path.isfile("saveData.txt") #This is a variable where it checks for the save data to load in the game.

timeDelayOne = 2 #These are times used for effect on the dialogue and to simulate a loading screen.
timeDelayTwo = 0.1

title_music = pygame.mixer.Sound('Pestilence.wav')  #This is a variable for the music in the title screen
music_one = pygame.mixer.Sound('room.wav')          #This is a variable for the music in the game
music_two = pygame.mixer.Sound('dystopiacity.wav')  #This is a variable for the music in the game
music_three = pygame.mixer.Sound('lab.wav')         #This is a variable for the music in the game

title_music.stop()      #this stops the title music to prevent the sound from overlapping when you're trying to restart the game
title_music.play(-1)    #this plays the title music.

#UserChoices
option_A = ["A", "a"]
option_B = ["B", "b"]
option_C = ["C", "c"]
option_D = ["D", "d"]
option_E = ["E", "e"]
option_F = ["F", "f"]
option_G = ["G", "g"]
option_H = ["H", "h"]

option_0 = "0"
option_1 = "1"
option_2 = "2"
option_3 = "3"
option_4 = "4"
option_5 = "5"

inventory = []      #This is the list that holds the inventory.


mandatory = "You have to pick something!"

#Sets character name
user_name = input("Set a name for your character: ")
characterName = user_name + ":"

#It sets a class for the items in the game.
class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

#This is the definition for the title screen.
def title_screen():
    time.sleep(timeDelayOne)
    print("Welcome to Pestilence:")
    print("a.) New Game")
    print("b.) Load Game")
    print("c.) Quit Game")
    titleOption = input("Input your choice: ")

    if titleOption in option_A:
        chapterOne()
    elif titleOption in option_B:
        print("Loading.....")
        load()
    elif titleOption in option_C:
        print("Exiting.....")
        sys.exit()
    else:
        print(mandatory)
        title_screen()

#This is the definition for the options menu.
def options():
    print("Options")
    print("a.) Back to menu")
    userOption = input("Select an option: ")

    if userOption in option_A:
        title_screen()


#This is the definition for the loading system of the game
def load():
    if file_exists:
        deleteData = input("Do you want to go back to the start? (Yes or No) ")
        if deleteData.lower() == "yes":
            os.remove("saveData.txt")
            chapterOne()
        elif deleteData.lower() == "no":
            file = open("saveData.txt", "r")
            choice = file.read()
            file.close()
            saveState(choice)
    else:
        chapterOne()

#This is the definition for the save system of the game
def save(s):
    file=open("saveData.txt","w")
    file.write(s)
    file.close()


#This is the definition for the game to check on which point in the game did you perform the save.

def saveState(choice):
    if choice == "gameStart":
        chapterOne()
    if choice == "dystopiaCity":
        chapterOneTwo()
    if choice == "christina":
        chapterOneThree()
    if choice == "laboratory":
        chapterOneFour()


# Code for Chapter 1 of the Game

def getItem(Item):      #This picks up the items in the game.
    inventory.append(Item)

def dropItem(Item):     #This drops the items in the game.
    inventory.remove(Item)

def chapterOne():

    title_music.stop()
    music_one.play(-1)
    time.sleep(timeDelayTwo)
    print("                                                                                                         CHAPTER 1")
    print()
    print("                                                                                                         Your Room")
    print("                                                                                                        October 2031")
    time.sleep(timeDelayOne)
    print(characterName)
    time.sleep(timeDelayOne)
    print("Since this pandemic broke out 10 years ago, this world hasn't seen much of the outside.")
    time.sleep(timeDelayOne)
    print("Despite being advanced in every kind of technology possible, we're still stuck in this loop trying to find out what made his whole thing worse.")
    time.sleep(timeDelayOne)
    print("This whole thing became a curse, a Pestilence that mankind was forced to carry on their shoulders.")
    time.sleep(timeDelayOne)
    print("I haven't got much sleep these past 10 years, despite our society being able to cope with it, it's still a pain in the ass how people are just fine with how things are.")
    time.sleep(timeDelayOne)
    print("I'm still stuck in the lab most of these days, trying to find out still how to solve this thing but I kept under wraps, especially since the higher ups don't want us meddling with these affairs.")
    time.sleep(timeDelayOne)
    print("Anyway, I need to get to work. But first I need to get a few things before I leave.")
    time.sleep(timeDelayOne)
    print()
    choiceOne()     #prints out the definition for the first choice in the game.

def choiceOne():

    counter = 0 #Used a counter to keep the loop going.
    while (counter < 1):
        print("0 - Get your stuff and leave.")
        print("1 - Get some breakfast.")
        print("2 - Clean yourself up.")
        print("3 - Just stay in bed")
        print("4 - Save Progress")
        print("5 - Exit game")

        inputCommand = input("Command: ") #asks for input from the user

        if inputCommand == option_0:
            time.sleep(timeDelayTwo)
            print("**Grabbed keys**")
            getItem("Keys")
            time.sleep(timeDelayTwo)
            print("**Grabbed wallet**")
            getItem("Wallet")
            time.sleep(timeDelayTwo)
            print("**Grabbed phone**")
            getItem("Phone")
            counter += 1
            chapterOneTwo()

        elif inputCommand == option_1:
            time.sleep(timeDelayTwo)
            print("I don't feel hungry honestly. But maybe I'll have some waffles.")
            print()

        elif inputCommand == option_2:
            time.sleep(timeDelayTwo)
            print("Should I really? Just kidding, I really want to take a shower.")
            print()

        elif inputCommand == option_3:
            time.sleep(timeDelayOne)
            print("I'm kinda tired, I'll just call in sick.")
            time.sleep(timeDelayOne)
            print("LAZY ENDING")
            counter += 1

        elif inputCommand == option_4:
            s = "gameStart"
            save(s)
            time.sleep(timeDelayOne)
            print("Game saved.")

        elif inputCommand == option_5:
            print("Game terminated")
            sys.exit()


        else:
            print("I don't understand what you're trying to tell me.")
            print()

def chapterOneTwo():
    title_music.stop()
    music_one.stop()
    music_two.play(-1)
    time.sleep(timeDelayOne)
    print()
    print("                                                                                                 Dystopia City ")
    print("                                                                                                 October 2031 ")
    time.sleep(timeDelayOne)
    print(characterName)
    print("Half of the world is covered in this bubble, despite this, you still have to wear these high-powered masks when trying to walk around.")
    time.sleep(timeDelayOne)
    print("Trying to walk around without these guarantees your death in seconds if you continue to breathe in the virus.")
    time.sleep(timeDelayOne)
    print("It's most of a pain in the ass now, but someday, I'll find the cure for this.")
    time.sleep(timeDelayOne)
    print("")
    choiceTwo()

def choiceTwo():
    counter = 0
    while (counter < 1):
        print("0 - Look around")
        print("1 - Beep your horn")
        print("2 - Wait for the traffic to move")
        print("3 - Save Progress")
        print("4 - Exit game")

        inputCommand = input("Command: ")

        if inputCommand == option_0:
            time.sleep(timeDelayTwo)
            print("A huge line of cars clog the road, this is getting boring.")
            print()

        elif inputCommand == option_1:
            time.sleep(timeDelayOne)
            print("***BEEEEPPPPPPP!!!!!***")
            time.sleep(timeDelayOne)
            print("***BEEEEPPPPPPP!!!!!***")
            time.sleep(timeDelayOne)
            print("***BEEEEPPPPPPP!!!!!***")
            time.sleep(timeDelayOne)
            print("The other cars started beeping, I feel like an asshole.")
            print()

        elif inputCommand == option_2:
            print(" ")
            time.sleep(timeDelayTwo)
            print("Damn, this is taking a while.......")
            time.sleep(timeDelayTwo)
            print("Finally! It's moving.")
            time.sleep(timeDelayTwo)
            counter += 1
            chapterOneThree()

        elif inputCommand == option_3:
            s = "dystopiaCity"
            save(s)
            time.sleep(timeDelayOne)
            print("Game saved.")
            print()

        elif inputCommand == option_4:
            print("Game terminated")
            sys.exit()

def chapterOneThree():
    title_music.stop()
    time.sleep(timeDelayOne)
    print()
    print(
        "                                                                                             Dystopia City Hospital")
    print(
        "                                                                                                 October 2031 ")

    print()
    print(characterName)
    print("I finally got here. A tad bit more and I would be late and getting an earful from my partner.")
    time.sleep(timeDelayOne)
    print("Seriously, that was some dumb traffic going around, so much for a Tuesday morning.")
    time.sleep(timeDelayOne)
    print(" ")
    time.sleep(timeDelayOne)
    print("Hey," + "" + user_name +"!")
    time.sleep(timeDelayOne)
    print()
    print(characterName)
    print("Why her so early in the morning?")
    time.sleep(timeDelayOne)
    print("Loud woman:")
    print("You're almost late already today! Don't tell me it's because of traffic again?")
    time.sleep(timeDelayOne)
    print()
    print(characterName)
    print("This woman is my boss/partner, Christina Michaels, I've been working with here for the past 10 years now and also she's been a huge help in my research too.")
    time.sleep(timeDelayOne)
    print("Crazy smart too, heck, I'm pretty smart but she's kinda floating above us with her intellect, it doesn't excuse her of being annoying sometimes.")
    time.sleep(timeDelayOne)
    print("What should I tell her for being late?")
    time.sleep(timeDelayOne)
    print()
    choiceThree()

def choiceThree():
    counter = 0
    while (counter < 1):
        print("0 - It was the traffic!")
        print("1 - I overslept!")
        print("2 - I'm not late! The clock is!")
        print("3 - Save Progress")
        print("4 - Exit game")

        inputCommand = input("Command: ")

        if inputCommand == option_0:
            print("Christina:")
            print("Really? This again, you've been always late these past few days, what a slacker.")
            time.sleep(timeDelayOne)
            print("Anyway, now you're here, I have some big news from the cure we've been making, let's go to the lab.")
            time.sleep(timeDelayOne)
            counter +=1
            chapterOneFour()
        elif inputCommand == option_1:
            print("Christina:")
            print("I'm glad you're more honest, but seriously, aren't alarm clocks a thing in your house or your phone?.")
            time.sleep(timeDelayOne)
            print("Anyway, now you're here, I have some big news from the cure we've been making, let's go to the lab.")
            time.sleep(timeDelayOne)
            counter += 1
            chapterOneFour()

        elif inputCommand == option_2:
            print("Christina:")
            print("Don't be a jackass.")
            time.sleep(timeDelayOne)
            print()
            print("Carl:")
            print("I feel a bad laser beams would start coming out of her eyes right now.")
            time.sleep(timeDelayOne)
            print("Anyway, now you're here, I have some big news from the cure we've been making, let's go to the lab.")
            time.sleep(timeDelayOne)
            counter += 1
            chapterOneFour()

        elif inputCommand == option_3:
            s = "Christina"
            save(s)
            time.sleep(timeDelayOne)
            print("Game saved.")
            print()

        elif inputCommand == option_4:
            print("Game terminated")
            sys.exit()

def chapterOneFour():
    title_music.stop()
    music_two.stop()
    music_three.play()
    print("                                                                                         Dystopia City Hospital Laboratory")
    print( "                                                                                                 October 2031 ")
    time.sleep(timeDelayOne)
    print()
    print("Christina:")
    print("Oh crap!")
    time.sleep(timeDelayOne)
    print("AHhhhhhhh!!!!!!")
    time.sleep(timeDelayOne)
    print()
    time.sleep(timeDelayOne)
    print(characterName)
    print("What happened?")
    time.sleep(timeDelayOne)
    print("It seems like somebody found out about our little thing.")
    time.sleep(timeDelayOne)
    print("The research paper and everything gone!")
    time.sleep(timeDelayOne)
    print("Christina, I don't think we should stay here much longer.")
    time.sleep(timeDelayOne)
    print("I think we're done for at this rate.")
    time.sleep(timeDelayOne)
    print()
    print("Christina:")
    print("Okay.")
    time.sleep(timeDelayOne)
    print("Let's hurry up before someone starts looking for us")
    time.sleep(timeDelayOne)
    print()
    print("Intercom:")
    print("Will Mr.Deckard and Ms. Michaels report to the head managers' office.")
    time.sleep(timeDelayOne)
    print()
    print(characterName)
    print("Crap! There goes the neighborhood! Come on! I know a way out.")
    time.sleep(timeDelayOne)
    print()
    print("We ran towards the emergency exit where the hell should we go?")
    time.sleep(timeDelayOne)
    print()
    print("Christina:")
    print("We can't get our cars now, I'm sure those things are guarded.")
    time.sleep(timeDelayOne)
    print("Wait! I know somewhere we could go.")
    time.sleep(timeDelayOne)
    print()
    print(characterName)
    print("Really the trash compactor?")
    time.sleep(timeDelayOne)
    print()
    print("Christina:")
    print("Well you got any other bright ideas?")
    time.sleep(timeDelayOne)
    print()
    print(characterName)
    print("Okay! Okay!")
    time.sleep(timeDelayOne)
    print("Holy crap! It smells here!")
    time.sleep(timeDelayOne)
    print()
    print("Christina:")
    print("Nice observation, Sherlock")
    time.sleep(timeDelayOne)
    print("C'mon, let's get out through here.")
    time.sleep(timeDelayOne)
    print()
    print(characterName)
    print("Finally! I'm out of this hell hole.")
    time.sleep(timeDelayOne)
    print("Christina, quick, hide!")
    time.sleep(timeDelayOne)
    print("It seems like the entranced is blocked, hold on, maybe I'll find some things that'll create a diversion and we'll take this guy out.")
    time.sleep(timeDelayOne)
    music_three.stop()
    music_two.play()
    choiceFour()

def choiceFour():
    counter = 0
    while (counter < 1):
        print("0 - Pick up stick")
        print("1 - Pick up rock")
        print("2 - Save Progress")
        print("3 - Exit game")

        inputCommand = input("Command: ")

        if inputCommand == option_0:
           print("I sneak up behind the guy and......*WHAM!*")
           time.sleep(timeDelayOne)
           print("The guy is now knocked out.")
           time.sleep(timeDelayOne)
           counter +=1
           endPart()
        elif inputCommand == option_1:
            print("I threw the rock and missed.")
            time.sleep(timeDelayOne)
            print("We got found out and brought to the director and got arrested for our research.")
            time.sleep(timeDelayOne)
            counter += 1
            print()
            print("BAD ENDING")
            time.sleep(timeDelayOne)
        elif inputCommand == option_2:
            s = "finalAct"
            save(s)
            time.sleep(timeDelayOne)
            print("Game saved.")
            print()
        elif inputCommand == option_3:
            print("Game terminated")
            sys.exit()

def endPart():
    title_music.stop()
    music_two.stop()
    music_one.play()
    print("                                                                                         Dystopia City Hospital Parking Lot")
    print( "                                                                                                 October 2031 ")
    print(characterName)
    print("Christina! Let's go while this guy is out.")
    time.sleep(timeDelayOne)
    print()
    print("Christina:")
    print("Well, I hope he's fine.")
    time.sleep(timeDelayOne)
    print()
    print(characterName)
    print("He will be. Where do we go from here now? It seems like starting today, we are both on the run.")
    time.sleep(timeDelayOne)
    print()
    print("Christina:")
    print("It doesn't matter to me, I want to solve the mystery behind this Pestilence that we carry today.")
    time.sleep(timeDelayOne)
    print("It's been too long now and we don't know where to go. All I know, is that Obsidian was the one that provided everything we needed to live by this pandemic.")
    time.sleep(timeDelayOne)
    print()
    print(characterName)
    print("Well, I guess I'm stuck with you now. Someday, someday we'll find the cure for this.")
    time.sleep(timeDelayOne)
    print("Me and Christina tries to run towards the horizon, as we prepare for the tribulations that will behold us.")
    time.sleep(timeDelayOne)
    print()
    time.sleep(timeDelayOne)
    print("TO BE CONTINUED.................")

    counter = 0
    while (counter < 1):
        print("0 - Title Screen")
        print("1 - Exit Game")

        inputCommand = input("Command: ")

        if inputCommand == option_0:
            counter += 1
            title_screen()
        elif inputCommand == option_1:
            print("Game terminated")
            sys.exit()



title_screen()

