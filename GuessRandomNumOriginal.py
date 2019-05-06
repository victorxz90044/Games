'''
Title: Guess the number
Requirements: random number between 1,10
            ask the user to guess a number 1,10
            If the user guesses correctly. Tell them you win.
            If the user gussess incorrectly. Tell them they suck.

            Loop under user guesses correctly.

            Print the number of guesses.

            Limit the guess to 3. 

            Tell user after each guesses if the number is higher or lower

            Add the abiliy to start again. 

            Local high score
'''

from __future__ import print_function
import random


def genRanNum():
    ranNum = random.randint(1,10)
    return ranNum

def isHigherLower(userGuess,ranNum):
    if userGuess < ranNum:
        print("Number is higher")
    elif userGuess > ranNum:
        print("Number is lower")



def playGame():
    ranNum = genRanNum()
    userIsCorrect = False
    numOfGuesses = 0

    while userIsCorrect == False and numOfGuesses <3:
        userGuess = int(input("Please enter a number 1-10. ")) 
        numOfGuesses= numOfGuesses+1
        if userGuess == ranNum:
            print("You have guessed the number correctly and it took you",numOfGuesses,"guesses.")
            userIsCorrect = True
        else:
            isHigherLower(userGuess,ranNum)
            if numOfGuesses ==3:
                print("The correct number was ",ranNum)
            
    
    return (numOfGuesses,userIsCorrect)
    
    
        



game=True
highScore = 4
while game == True:
    print("Let's play a game.")
    (score,isWinner) = playGame()
    if score < highScore and isWinner == True:
        highScore=score
        print("Congrats, its your best run")
    continueGame = input("Do you want to play again? (y/n)")
    if continueGame =="n":
        game = False
        print("GTFO")
   








