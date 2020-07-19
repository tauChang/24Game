from random import randrange
import itertools
import math

class Game:
    def __init__(self):
        self.playerCount = 2
        self.players = []
        self.score = {}
        self.roundCount = 10

    def judge(self, cards):
        if(len(cards) == 1):
            return math.isclose(cards[0], 24)
        return any(self.judge([x] + rest)
               for a, b, *rest in itertools.permutations(cards)
               for x in {a + b, a - b, a * b, b and a / b})

    def giveCard(self):
        while True:
            cards = [randrange(1, 14) for i in range(4)]
            if self.judge(cards):
                break
        return cards

    def printScore(self):
        for player in self.players:
            print("> ", player, ":", self.score[player])

    def roundWinner(self):
        winner = input("Who's the winner? ")
        while winner not in self.players:
            winner = input("Type again, dumdum. ")
        print("Good job, %s!" % winner)
        self.score[winner] += 1

    def finalWinner(self):
        return []
        # returns a list

    def farewell(self):
        print("The game has ended! The score is\n")
        self.printScore()
        print("\n%s is the winner! Congratulations!" % 'a')
        

    def start(self):
        print("Welcome to The 24 Game!\n")
        self.roundCount = int(input("How many rounds do you want to play? "))
        self.playerCount = int(input("How many players are there? "))
        for i in range(self.playerCount):
            name = input("Player %d's name: " % (i+1))
            self.players.append(name)
            self.score[name] = 0
        print("Great! Let's start the game!")

        r = 1
        while r <= self.roundCount:
            print("\n==============================")
            self.printScore()
            cards = self.giveCard()
            print(cards)
            self.roundWinner()
            # Deal with winner
            print("==============================\n")
            r += 1
        self.farewell()

if __name__ == '__main__':
    g = Game()
    g.start()
