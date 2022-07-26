from CheckJokbo import checkJokbo

class PrototypeAI:
    def __init__(self, game):
        self.nowDeck = []
        self.game = game
        
    def initCard(self):
        self.nowDeck = []

    def addCard(self, newCard):
        self.nowDeck.append(newCard)
    
    def bettingReply(self, playerBetting):
        jokbo, score = checkJokbo(self.nowDeck)
        if self.game.turn == 1:
            if sum(self.nowDeck) >= 30 or score >= 200:
                return True
            else:
                return False
        elif self.game.turn == 4 and playerBetting >= 1000:
            if score >= 300:
                return True
            else:
                return False
        else:
            if score >= 200:
                return True
            else:
                return False

    def allInReply(self):
        jokbo, score = checkJokbo(self.nowDeck)
        if self.game.turn == 1:
            if score >= 200:
                return True
            else:
                return False
        else:
            if score >= 500:
                return True
            else:
                return False