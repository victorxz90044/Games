from __future__ import print_function
import random


def read_int(prompt):
    value = raw_input(prompt)
    return int(value)

def yes_or_no(prompt):
    value = raw_input(prompt + " y/n: ")
    return value != "n"

class Game:

    def __init__(self, min, max, tries):
        self.min = min
        self.max = max
        self.tries = tries
        self.attempts = 0
        self.answer = random.randint(min, max)
        self._is_winner = False

    def can_continue(self):
        return (not self.is_winner) and (self.attempts < self.tries)

    def check_guess(self, guess):
        result = Result(guess, self.answer)
        self.attempts = self.attempts + 1
        self._is_winner = result.is_correct
        return result

    @property
    def is_winner(self):
        return self._is_winner

    @property
    def is_loser(self):
        return not self._is_winner

class Result:
    def __init__(self, guess, answer):
        self.is_correct = guess == answer
        self.too_low = guess < answer
        self.too_high = guess > answer

if __name__ == "__main__":
    high_score = None

    while True:
        game = Game(min=1, max=10, tries=5)
        print(game.answer)

        while game.can_continue():
            guess = read_int("Guess a number between %s and %s: " % (game.min, game.max))
            result = game.check_guess(guess)

            if result.is_correct:
                print("Congratulations! You guess correctly in only %s tries" % (game.attempts))
            else:
                if result.too_low:
                    print("Guess higher")
                elif result.too_high:
                    print("Guess lower")

        if game.is_loser:
            print("The correct answer was %s" % (game.answer))
        
        if game.is_winner and (high_score is None or high_score > game.attempts):
            print("You beat the high score")
            high_score = game.attempts

        play_again = yes_or_no("Would you like to play again?")
        if not play_again:
            print("Thanks for playing!")
            break