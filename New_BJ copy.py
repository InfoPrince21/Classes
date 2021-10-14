import random

players = []

deck_of_cards = {
    "Ace of Diamonds":11, "2 of Diamonds":2, "3 of Diamonds":3, "4 of Diamonds":4, "5 of Diamonds":5, "6 of Diamonds":6, "7 of Diamonds":7, "8 of Diamonds":8, "9 of Diamonds":9, "10 of Diamonds":10, "Jack of Diamonds":10, "Queen of Diamonds":10, "King of Diamonds":10,
    "Ace of Hearts":11, "2 of Hearts":2, "3 of Hearts":3, "4 of Hearts":4, "5 of Hearts":5, "6 of Hearts":6, "7 of Hearts":7, "8 of Hearts":8, "9 of Hearts":9, "10 of Hearts":10, "Jack of Hearts":10, "Queen of Hearts":10, "King of Hearts":10,
    "Ace of Clubs":11, "2 of Clubs":2, "3 of Clubs":3, "4 of Clubs":4, "5 of Clubs":5, "6 of Clubs":6, "7 of Clubs":7, "8 of Clubs":8, "9 of Clubs":9, "10 of Clubs":10, "Jack of Clubs":10, "Queen of Clubs":10, "King of Clubs":10,
    "Ace of Spades":11, "2 of Spades":2, "3 of Spades":3, "4 of Spades":4, "5 of Spades":5, "6 of Spades":6, "7 of Spades":7, "8 of Spades":8, "9 of Spades":9, "10 of Spades":10, "Jack of Spades":10, "Queen of Spades":10, "King of Spades":10
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
        print("")
        print("The deck of cards has been shuffled.")
        print("")
    
    def buildCards(self):
        for face, value in self.deck: 
                self.cards.append(Card(face,value))

    def dealCard(self):
        return self.cards.pop()
    
    def show(self):
        for c in self.cards:
            c.show()
       
class Player:
    def __init__(self, name, bank = 0, bet = 0):
        self.name = name
        self.hand = []
        self.bank = bank
        self.bet = bet
        self.busted = 0
        self.bj = 0
    
    def checkBust(self):
        if self.total() > 21:
            print(f"{self.name} Busts.")
            self.busted = 1
        
    def showBet(self):
        print(f'{self.name} has bet ${self.bet}')

    def wonBj(self):
        self.bank += (self.bet * 1.5)
        return self.bank

    def betWon(self):
        self.bank += self.bet
        return self.bank

    def betLost(self):
        self.bank -= self.bet
        return self.bank

    def info(self):
        print(f'{self.name} has ${self.bank}')
               
    def getCard(self, deck):
        self.hand.append(deck.dealCard())
        return self.hand
    
    def discard(self):
        return self.hand.clear()
        
    def show(self):
        for card in self.hand:
            card.show()
    
    def show1(self):
        self.hand[0].show()

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
        elif aces > 2 and sum_total > 31:
            return ace_total - 20
        elif aces > 3 and sum_total > 41:
            return ace_total - 30
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
        elif aces > 2 and sum_total > 41:
            print(f'{self.name} has a total of {ace_total - 20}')
        elif aces > 2 and sum_total < 41:
            print(f'{self.name} has a total of {ace_total - 20} or {ace_total - 10}')
        elif aces > 3:
            print(f'{self.name} has a total of {ace_total - 30} or {ace_total - 20} ')
        else:
            print(f'{self.name} has a total of {sum_total}')

def getPlayers():
    while True:    
        get_name = input("Enter here -------->: ").upper()
        if get_name.isalpha() == True:
            try:
                get_bank = float(input(f"Enter {get_name}'s bankroll amount: $"))
                get_name = Player(get_name, get_bank)
                return players.append(get_name)
            except:
                print("Bankroll entry must be a numerical value!")
                print("Enter name again:")
        else:
            print("Name must contain letters only.")
            continue
          
def currentPlayers():
    print("")
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

def player1card():
    for player in players:
        player.getCard(deck1)
        print(player.name, "Has:")
        player.show()
        player.total()
        player.showTotal()
        player.checkBust()
        if player.bust == 1:
            print(f'{player.name} Busts')
            continue
        print("")

def dealer2cards():
    dealer.getCard(deck1)
    dealer.getCard(deck1)
    dealer.total()
    print("")
    print("Dealer shows a:")
    dealer.show1()
    print("")

def dealer1card():
    while dealer.total() < 17:
        print("Dealer has less than 17 and hits.") 
        dealer.getCard(deck1)
        dealer.total()
        print("")
        print("Dealer Has:")
        dealer.show()
        print("")
    if dealer.total() > 21:
        dealer.busted = 1
        print("Dealer busts with", dealer.total())
        print("")
    if dealer.total() == 21:
        print("Dealer has 21")
    if dealer.total() >= 17 and dealer.total() < 21:
        print("Dealer has total of:", dealer.total())
        print("Dealer must stay with:")
        dealer.show()
        print("")

def calcWinner():
    for player in players:
        if player.total() < dealer.total() and dealer.total() <= 21:
            print(f'{player.name} loses ${player.bet}')
            player.betLost()
        if player.total() > 21:
            print(f'{player.name} busted before dealer showed hand and loses ${player.bet}')
            player.betLost()
        elif player.total() < dealer.total() and dealer.busted == 1:
            print(f'{player.name} wins ${player.bet}')
            player.betWon()
        elif player.total() == dealer.total() and dealer.total() <=21:
            print(f'{player.name} pushes.')
        elif player.total() == 21 and player.bj == 1:
            print(f'{player.name} wins ${player.bet * 1.5} ')
            player.wonBj()
        elif player.total() == 21:
            print(f'{player.name} wins ${player.bet}')
            player.betWon()
        elif player.total() > dealer.total() and dealer.total() < 21:
            print(f"{player.name} wins ${player.bet}")
            player.betWon()

def newGame():
    global dealer, deck1
    dealer = Player("Dealer")
    deck1 = Deck()
    deck1.shuffle()
    deck1.buildCards()

def enterPlayers():
    try:
        print("")
        print("----Welcome to the BlackJack Table----")
        print(f'There are currently {len(players)} player(s)')
        print(f'Maximum amount of players is 6.')
        print(f'Minimum amount is 1 player.')
        while True:
            p_count = int(input(f'How many players are joining the game?: '))
            if 1 <= (len(players) + p_count) < 7:
                for i in range(p_count):
                    print(f"What is player {i + 1}'s name?")
                    getPlayers()
                break
            else:
                print("Entry violates player min/maximum, try again.")
        
    except:
        print("Please enter a number.")
        enterPlayers()
    
def playerBets():
    for player in players:
        while True:
            try:
                get_bet = input(f'How much does {player.name} want to bet?: $')
                get_bet = float(get_bet) 
                player.bet = get_bet
                if player.bet > player.bank:
                    print(f"{player.name} doesn't have enough to cover ${player.bet} bet, try again.")
                    continue
                else:
                    break
            except:
                print("Bet must be a number.")

def showPlayerBets():
    print("----------Current Bets---------")
    print("There's" , len(players), "bets")   
    for player in players:
        player.showBet()
    print("-------------------------------") 

def clearHands():
    for player in players:
        player.discard()
        player.bet = 0
        player.bj = 0
        player.busted = 0
        dealer.busted = 0
        dealer.bj = 0
        removePlayers()

def playerOption():
        for player in players:
            while player.total() < 21:
                if player.bj == 1:
                    break
                print(f"{player.name} has {player.total()}, choose an option")
                choice = input("|1. To Hit | 2. Stay | : ")
                print("")
                if choice =="1":
                    player.getCard(deck1)
                    print(player.name, "Has:")
                    player.show()
                    player.total()
                    player.showTotal()
                    player.checkBust()
                    print("")
                    continue
                elif choice =="2":
                    break
                else:
                    print('Not a valid option')

def checkBlackJack():
    if dealer.total() !=21:
        print('Dealer does not have BlackJack')
        print("")
    for player in players:
        if player.total() == 21:
            player.bj = 1
            print(f'{player.name} has BlackJack!')
            print("")

def removePlayers():  
    for player in players:
        if player.bank == 0:
            print("")
            print(f"{player.name}'s bankroll is $0.0")
            while True:
                add_more = input(f'Does {player.name} want to add to their bankroll? (Y/N) ').upper()
                if add_more == "Y":
                    try:
                        add_bank = input(f"How much does {player.name} want to add to bankroll? $")
                        add_bank = float(add_bank)
                        player.bank = add_bank
                        break
                    except:
                        print("Must enter a number, try again.")
                elif add_more == "N":
                    print("")
                    print(f"{player.name} didn't add money to an empty bankroll and has been removed.")
                    players.remove(player)
                    break
                else:
                    print("Not a valid option")               
        else:
            break

def checkEmptyPlayers():
    if len(players) == 0:
        print("")
        print("There are currently no players")
        ask_add = input("Would you like to add player(s)  (Y/N)? ").upper()
        if ask_add == "Y":
            enterPlayers()
        elif ask_add == "N":
            print("Goodbye, thanks for playing!")
            quit()
        else:
            print("Not a valid option.")
    else:
        pass

def playerLeaves():
    while True:
        ask_to_quit = input("Remove player(s) from the game? (Y/N): ").upper()
        if ask_to_quit == "Y" and len(players) != 0:
            ask_who = input("Which player?: ").upper()
            for player in players:
                temp_list = []
                temp_list.append(player.name)
                if ask_who in temp_list:
                    print(f'{player.name} has been removed by request.')
                    players.remove(player)
                    currentPlayers()
                else:
                    print("Searching...")
                    print("Not found.")
                    currentPlayers()
        elif ask_to_quit == "Y" and len(players) == 0 :
            print("There's currently no more players.")
            break
        elif ask_to_quit == "N":
            break

def app():
    enterPlayers()
    currentPlayers()
    while True:
        checkEmptyPlayers()
        playerLeaves()
        play_game = input('Start Game? (Y/N) ').upper()
        if play_game == "Y":
            checkEmptyPlayers()
            currentPlayers()
            newGame()
            playerBets()
            showPlayerBets()
            dealer2cards()
            player2cards()
            checkBlackJack()
            if dealer.total() != 21:
                playerOption()
                dealer1card()
                calcWinner()
                currentPlayers()
                clearHands()
                removePlayers()
            elif dealer.total() == 21:
                print(f'Dealer has BlackJack')
                print("")
                dealer.show()
                print("")
                calcWinner()
                currentPlayers()
                clearHands()
                removePlayers()
            else:
                pass
        elif play_game == "N":
            print("Goodbye")
            quit()
        else:
            print('Not a valid option.')

app()