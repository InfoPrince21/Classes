import random

deck_of_cards = {
    "Ace of Diamonds":11, "2 of Diamonds":2, "3 of Diamonds":3, "4 of DiamondsD":4, "5 of Diamonds":5, "6 of Diamonds":6, "7 of Diamonds":7, "8 of Diamonds":8, "9 of Diamonds":9, "10 of Diamonds":10, "Jack of Diamonds":10, "Queen of Diamonds":10, "King of Diamonds":10,
    "Ace of Hearts":11, "2 of Hearts":2, "3 of Hearts":3, "4 of Hearts":4, "5 of Hearts":5, "6 of Hearts":6, "7 of Hearts":7, "8 of Hearts":8, "9 of Hearts":9, "10 of Hearts":10, "Jack of Hearts":10, "Queen of Hearts":10, "King of Hearts":10,
    "Ace of Clubs":11, "2 of Clubs":2, "3 of Clubs":3, "4 of Clubs":4, "5 of Clubs":5, "6 of Clubs":6, "7 of Clubs":7, "8 of Clubs":8, "9 of Clubs":9, "10 of Clubs":10, "Jack of Clubs":10, "Queen of Clubs":10, "King of Clubs":10,
    "Ace of Spades":11, "2 of SpadesS":2, "3 of Spades":3, "4 of Spades":4, "5 of Spades":5, "6 of Spades":6, "7 of Spades":7, "8 of Spades":8, "9 of Spades":9, "10 of Spades":10, "Jack of Spades":10, "Queen of Spades":10, "King of Spades":10
    }

class Card:
    def __init__(self, face, value):
        self.face = face
        self.value = value
    
    def show(self):
        print(self.face)
    
    def count(self):
        count = int(self.value)
        return count

class Deck:
    def __init__(self):
        self.deck = list(deck_of_cards.items())
        self.cards = []

    def shuffle(self):
        random.shuffle(self.deck)
        print("The deck of cards has been shuffled.")
    
    def buildCards(self):
        for face, value in self.deck: 
                self.cards.append(Card(face,value))

    def dealCard(self):
        return self.cards.pop()
    
    def show(self):
        for c in self.cards:
            c.show()
       
class Player:
    def __init__(self, name, bank = 0):
        self.name = name
        self.hand = []
        self.bank = bank
    
    def info(self):
        print(f'{self.name} with a bankroll of ${self.bank}')

    def wager(self, bet_amount):
        self.bet_amount = bet_amount
        print(f'You bet {bet_amount}')
        return bet_amount
                
    def getCard(self, deck):
        self.hand.append(deck.dealCard())
        return self.hand
    
    def show(self):
        for card in self.hand:
            card.show()
    
    def total(self):
        total = []
        ace_option = 10
        for card in self.hand:
            total.append(card.count())
        sum_total = sum(total)
        aces = total.count(11)
        ace_total = (sum_total - ace_option)
        if aces > 0 and sum_total > 21:
            return ace_total
        elif aces > 1 and sum_total > 31:
            return ace_total - 10
        else:
            return sum_total
    
    def showTotal(self):
        total = []
        ace_option = 10
        for card in self.hand:
            total.append(card.count())
        sum_total = sum(total)
        ace_total = (sum_total - ace_option)
        aces = total.count(11)
        if aces > 0 and sum_total > 21:
            print(f'{self.name} has a total of {ace_total}')
        elif aces > 0 and sum_total < 21:
            print(f'{self.name} has a total of {ace_total} or {sum_total}')
        elif aces > 1 and sum_total > 31:
            print(f'{self.name} has a total of {ace_total - 10}')
        elif aces > 1 and sum_total < 31:
            print(f'{self.name} has a total of {ace_total - 10} or {ace_total}')
        else:
            print(f'{self.name} has a total of {sum_total}')

def newPlayer():
    global total_players
    while True:    
        get_name = input("What is the new player's name?: ").upper()
        try:
            get_bank = float(input(f"Enter {get_name}'s bankroll amount: $"))
            get_name = Player(get_name, get_bank)
            return players.append(get_name)
        except:
            print("Bankroll must be a numerical value!")
            print("Please try again.")
          
def currentPlayers(): 
    print("--------Current Players--------")
    print("There's" , len(players), "player(s)")   
    for player in players:
        player.info()
    print("-------------------------------")    

def player2cards():
    for player in players:
        player.getCard(deck1)
        player.getCard(deck1)
        print(player.name, "Has:")
        player.show()
        player.total()
        player.showTotal()
        print("")

def dealer2cards():
    dealer.getCard(deck1)
    dealer.getCard(deck1)
    dealer.total()
    print("")
    print("Dealer Has:")
    dealer.show()
    print("Dealer has total of:", dealer.total())
    print("")

def calcWinner():
    for player in players:
        if player.total() < dealer.total():
            print(f'{player.name} Loses!')
        elif player.total() == dealer.total():
            print(f'{player.name} Pushes!')
        else:
            print(f"{player.name} Wins!")  

def newGame():
    dealer = Player("Dealer")
    players = []
    deck1 = Deck()
    deck1.buildCards()
    deck1.shuffle()
    return dealer, players, deck1

def addPlayer():
    p_count = input(f'How many players?: ')
    p_count = int(p_count)
    
    for i in range(p_count):
        newPlayer() * i
        

newGame()
addPlayer()


#deck1.shuffle()
# player1.getCard(deck1)
# player1.getCard(deck1)
# player1.getCard(deck1)
# player1.getCard(deck1)
# print(player1.name, "was dealt:")
# player1.show()
# player1.total()
# player1.showTotal()

# dealer.getCard(deck1)
# dealer.getCard(deck1)
# dealer.getCard(deck1)
# dealer.getCard(deck1)
# print(dealer.name, "was dealt:")
# dealer.show()
# dealer.total()
# dealer.showTotal()

# if player1.total() < dealer.total():
#     print(f'{player1.name} loses to {dealer.name}')

# if player1.total() > dealer.total():
#     print(f'{player1.name} beats {dealer.name}')

