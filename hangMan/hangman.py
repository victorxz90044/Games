'''
Created on Jun 19, 2017

@author: u0512418
'''

def hangman(word):
    wrong = 0 
    stages = ["", 
            "| ._____))______|   ",
            "| | / / ||          ",
            "| |/ /  ||          ",
            "| | /   ||.-''.     ",
            "| |/    |/  _  \    ",
            "| |     ||  `/,|    ",
            "| |     (\\`_.'     ",
            "| |    .-`--'.      ",
            "| |   /Y . . Y\     ",
            "| |  // |   | \\    ",
            "| | //  | . |  \\   ",
            "| |')   |   |   (`  ",
            "| |     ||'||       ",
            "| |     || ||       ",
            "| |     || ||       ",
            "| |     || ||       ",
            "| |    / | | \      ",
            "*****|_`-' `-' |***|",
            "|*|**\ \       '*|*|",
            "| |   \ \        | |",
            ": :    \ \       : :",
            ". .     `'       .  ",
    
              ]
     
    
    
    rletters = list(word)
    board = ["*"] * len(word)
    win = False
    print ("Welcome to hangman")
    
    while wrong < len(stages) - 1:
        print ("\n")
        msg = "Guess a letter"
        char = input(msg)
        
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind]='$'
            
        else:
            wrong += 1
        print(("".join(board)))
        e = wrong + 1
        print ("\n".join(stages[0:e]))
        if "*" not in board:
            print("You win!")
            win=True
            break
        
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lost! It was {}.".format(word))
        
        
hangman("horse")