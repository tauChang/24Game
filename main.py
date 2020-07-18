from random import randrange
import itertools
import math

cards = [randrange(1, 14), randrange(1, 14), randrange(1, 14), randrange(1,14)]

def judgee(cards):
    if(len(cards) == 1):
        return math.isclose(cards[0], 24)
    return any(judgee([x] + rest)
           for a, b, *rest in itertools.permutations(cards)
           for x in {a + b, a - b, a * b, b and a / b})

class Game:
    def __init__(self):
        self.playerCount = 2
        self.players = []
        self.score = []
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
        for i in range(self.playerCount):
            print("> ", self.players[i], ":", self.score[i])
        
    def start(self):
        print("Welcome to The 24 Game!\n")
        self.roundCount = int(input("How many rounds do you want to play? "))
        self.playerCount = int(input("How many players are there? "))
        for i in range(self.playerCount):
            self.players.append(input("Player %d's name: " % (i+1)))
            self.score.append(0)
        print("Great! Let's start the game!")

        r = 1
        while r <= self.roundCount:
            print("\n==============================")
            self.printScore()
            cards = self.giveCard()
            print(cards)
            # Deal with winner
            print("==============================\n")
            r += 1
            
