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
        print("\n")

    def roundWinner(self):
        winner = input("Who's the winner? ")
        while winner not in self.players:
            winner = input("No such player. Type again, dumdum. ")
        print("Good job, %s!" % winner)
        self.score[winner] += 1

    def finalWinner(self):
        return [p for p in self.score if self.score[p] == max(self.score.values())]
        # returns a list

    def farewell(self):
        print("The game has ended! The score is\n")
        self.printScore()
        winners = self.finalWinner()
        if len(winners) > 1:
            print(*winners[:-1], "and %s are the winners! Congratulations!" % winners[-1], sep = ", ")
        else:
            print("\n%s is the winner! Congratulations!" % 'a')
        

    def start(self):
        print("Welcome to The 24 Game!\n")
        while True:
            try:
                self.roundCount = int(input("How many rounds do you want to play? "))
                break
            except ValueError:
                print("You are giving the wrong input. Try again, dumdum\n")
        while True:
            try:
                self.playerCount = int(input("How many players are there? "))
                break
            except ValueError:
                print("You are giving the wrong input. Try again, dumdum\n")
        
            
        for i in range(self.playerCount):
            while True:
                name = input("Player %d's name: " % (i+1))
                if name in self.players:
                    print("This name is already taken. Give this player another name.")
                else:
                    break
            self.players.append(name)
            self.score[name] = 0
        print("Great! Let's start the game!")

        r = 1
        while r <= self.roundCount:
            print("\n==============================")
            print("~ Round %d ~\n" %r)
            self.printScore()
            cards = self.giveCard()
            print(cards, "\n")
            self.roundWinner()
            # Deal with winner
            print("==============================\n")
            r += 1
        self.farewell()

if __name__ == '__main__':
    g = Game()
    g.start()
