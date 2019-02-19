#  hangman game capable of: multiple rounds & win/loss count, multiple repeated letters, 
#  displaying spaces in words, input validation, ignorance to input lettercase, and
#  drawing the hangman in turtles

import random
import sys
import turtle
import os
global clear
clear = lambda: os.system('cls')

wins = 0
losses = 0
def winlosscount():
    print("\n\tWins: ",wins,"   Losses:",losses)
global gamecount
gamecount = 0

hanggame = True
while hanggame:
    print("\n\n  Welcome to Hangman! Please pick a category for your word.")
    print("  The categories are: [p]laces, [o]bjects, [a]nimals, [i]nstruments, [s]ame-vowel words, and [t]oughies.")
    print("  You can also choose [r]andom, or simply hit [Enter] to quit.")
    winlosscount()

    catselect = True

    #   starts loop of player choosing category. if valid input, loop ends
    while catselect:
        category = input().lower()

        places = ["paris","pittsburgh","denmark","brazil","antarctica","philadelphia","australia","toronto","mississippi","california","madagascar","london","nashville","tennessee","spain","germany","afganistan"]

        objects = ["television","lantern","bottle","underwear","pencil","computer","boardgame","backpack","sweatshirt","camera","lightswitch","regrigerator","wheelchair","bookshelf","microphone","jacket"]

        animals = ["aardvark","flamingo","elephant","mosquito","jaguar","zebra","monkey","tiger","panda","giraffe","octopus","swordfish","dolphin","parrot","cheetah","gazelle","chicken","butterfly","eagle","hippopotamus"]
        
        samevowelwords = ["madagascar","clockwork","references","winning","banana","shepherd","diminishing","gentlemen","pepper","preteen"]
        
        instruments = ["oboe","trumpet","trombone","flute","clarinet","tambarine","violin","cello","cymbal","xylophone","accordion","harmonica","piccolo","saxophone","tuba","organ","guitar","banjo","ukulele"]
        
        toughies = ["rhythms","strengths","onyx","lackadaisical","handkerchief","extraordinary","queue","equivalence","frequency","qualm","acquisition","bassists","scissors","lossless","riffraff","interogative,","throughout","onomatopoeia"]

        listlist = [places,objects,animals,samevowelwords,instruments,toughies]
        namelist = ["Places","Objects","Animals","Same-Vowel Words","Instruments","Toughies"]
        
        testlist = ["school bus"] # <-- to test spaces. haven't implemented yet though
        
        if category == "":
            sys.exit()
        
        if category == "test":
            cat_name = "Test mode"
            wordlist = testlist
            break

        if category == "p":
            cat_name = "Places"
            wordlist = places
            break
        if category == "o":
            cat_name = "Objects"
            wordlist = objects
            break
        if category == "a":
            cat_name = "Animals"
            wordlist = animals
            break
        if category == "s":
            cat_name = "Same-Vowel Words"
            wordlist = samevowelwords
            break
        if category == "i":
            cat_name = "Instruments"
            wordlist = instruments
            break
        if category == "t":
            cat_name = "Toughies"
            wordlist = toughies
            break
        if category == "r":
            wordlist = random.choice(listlist)
            location = listlist.index(wordlist)
            cat_name = (namelist[location])
            break
        if category != "p" or "o" or "a" or "s" or "i" or "t" or "r":
            print('\n\tPlease only type "p", "o", "a", "s", "i", "t", or "r"!')

    #------------------------------------------
    # Variables

    lives = 8

    goodguess = []
    badguess = []

    startindex = -1
    newstartindex = 0

    outputbucket = []
    myset = 1
    newbucket = 1

    # randomly selects a word from given wordlist, then takes length of word.
    # creates a list to hold as many "-"s as characters in the word, then 
    # accounts for spaces and cleans it up
    word = random.choice(wordlist)
    wordlength = (len(word))

    dashies = ["_ "]*wordlength
    if " " in word:
        spaceindex = word.index(" ")
        dashies[spaceindex] = "  "
    cleandashies = " ".join(dashies)

    #-------------------------------------------
    # Letter Placement Function

    def findreplace():
        global startindex
        global outputbucket
        global dashies
        global newstartindex
        global guess
        global word
        global wordlength
        global myset
        global newbucket
        global cleandashies

        for letter in word:
            
            # run starting index for each letter as start to look for "guess"
            # in the word, then place outputs like "2" or "6" in a list
            startindex = startindex + 1
            try:
                output = (word.index(guess,startindex))
                outputbucket = outputbucket+[output]
                
            # prevents errors being thrown
            except:
                outputbucket = outputbucket
        
        # makes list unique, then makes it a list again
        # need unique because of outputs like "2,2,2,6,6,6,6"
        myset = set(outputbucket)
        newbucket = list(myset)
        
        # goes through every x in the dashes "_ _ _" and takes the index
        # where guess matched in word and replaces the dash with the letter
        for instance in myset:
            try:
                dashies[int(newbucket[newstartindex])] = guess
                newstartindex = newstartindex + 1
            except:
                outputbucket = outputbucket
            finally:
                cleandashies = " ".join(dashies)
        # resets variables for the next time
        startindex = -1
        newstartindex = 0
        outputbucket = []
        myset = 1
        newbucket = 1
        print("  "+cleandashies)
            
    def lives_hits_misses_space():
        print("\n\n\tLives left: ",lives)
        print("\tHits: ",goodguess,"\t  Category: ",cat_name)
        print("\tMisses: ",badguess)
        print("\n")
    # all the turtle stuff
    def hangmandrawing():
        turtle.width(3)
        if lives == 7:
            # the stand
            turtle.goto(0,-250)
            turtle.forward(70)
            turtle.back(140)
            turtle.forward(70)
            turtle.left(90)
            turtle.forward(500)
            turtle.right(90)
            turtle.forward(170)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
        if lives == 6:
            # head
            turtle.begin_fill()
            turtle.circle(40)
            turtle.end_fill()
            turtle.circle(40,180)
            turtle.right(90)
        if lives == 5:
            # torso
            turtle.forward(160)
        if lives == 4:
            # left arm
            turtle.back(100)
            turtle.right(30)
            turtle.forward(70)
            turtle.back(70)
            turtle.left(60)
        if lives == 3:
            # right arm
            turtle.forward(70)
            turtle.back(70)
            turtle.right(30)
        if lives == 2:
            #left leg
            turtle.forward(100)
            turtle.right(30)
            turtle.forward(90)
            turtle.back(90)
            turtle.left(60)
        if lives == 1:
            #right leg
            turtle.forward(90)
        if lives == 0:
            # left eye
            topleftx = 150
            turtle.penup()
            turtle.goto(150,170)
            turtle.pendown()
            turtle.color("red")
            turtle.goto(165,155)
            turtle.penup()
            turtle.goto(165,170)
            turtle.pendown()
            turtle.goto(150,155)
            turtle.penup()
            # right eye
            turtle.goto(175,170)
            turtle.pendown()
            turtle.goto(190,155)
            turtle.penup()
            turtle.goto(190,170)
            turtle.pendown()
            turtle.goto(175,155)
            turtle.penup()
            # frown
            turtle.goto(185,137)
            turtle.left(185)
            turtle.pendown()
            turtle.circle(20,120)
            turtle.penup()
            turtle.goto(-800,0)

    #-------------------------------------------
    # Begin Game!

    if category == "r":
        print('\n\n  You have randomly chosen "'+cat_name+'" as your category!')
    if category != "r":
        print('\n\n  You have chosen "'+cat_name+'" as your category!')
    print("\n  Time to guess the word. Good luck! :)")
    print("\n\n\tLives left: ",lives,"\n\n")

    print("  "+cleandashies)

    game = True
    gamecount = gamecount+1
    
    # changes turtle graphics colors based on game number, resets after 5
    if gamecount == 1:
        turtle.bgcolor("white")
    if gamecount == 2:
        turtle.bgcolor("cadet blue")
        turtle.color("cyan")
    if gamecount == 3:
        turtle.bgcolor("black")
        turtle.color("white")
    if gamecount == 4:
        turtle.bgcolor("purple")
        turtle.color("hot pink")
    if gamecount == 5:
        turtle.bgcolor("slate blue")
        turtle.color("yellow")
        gamecount = 0
    
    while game:
        guess = input("\n").lower()
        
        # if input is the word, you win
        if guess == word:
            wins = wins + 1
            print("\n  Great guess! You win!")
            break
            
        # if input is [enter], you exit
        if guess is "":
            sys.exit()
        
        # if input has already been guessed, throws error and doesn't 
        # take a life away
        if guess in badguess or guess in goodguess:
            print("\n\tAlready guessed!")
            lives_hits_misses_space()
            print("  "+cleandashies)
        
        # if input not yet guessed...
        elif guess not in badguess or guess not in goodguess:
            
            # if input is in word, add to correct list and add into dashes
            if guess in word:
                goodguess = (goodguess + [guess])
                lives_hits_misses_space()
                findreplace()
                if "_" not in cleandashies:
                    wins = wins + 1
                    print("  Nice job! You win!")
                    break
                    
            # if input not in word, add to bad guesses, deduct life,
            # call hangman function
            if guess not in word:
                badguess = (badguess + [guess])
                lives = lives - 1
                lives_hits_misses_space()
                print("  "+cleandashies)
                hangmandrawing()
                
                # if out of lives, tell you you stink
                if lives == 0:
                    losses = losses + 1
                    print("\n  Aw man, the guy got hung because you suck at guessing!\n  You stink :(")
                    print('\n  The word was "'+word+'".')
                    break
    
    # when game ends in some way, prompt to play again
    print("\n\n   -- Would you like to play again? --")
    playagain = input(" -- [Enter] to continue or [n] to quit --\n")
    turtle.clear()
    turtle.reset()
    clear()
    if playagain == "n":
        sys.exit()
    
