import random
import webbrowser

players = []

the_aces = ["Ace of Spades", "Ace of Diamonds", "Ace of Hearts, Ace of Clubs"]
the_kings = ["King of Spades", "King of Diamonds", "King of Hearts", "King of Clubs"]
the_queens = ["Queen of Spades", "Queen of Diamonds", "Queen of Hearts", "Queen of Clubs"]
the_jacks = ["Jack of Spades", "Jack of Diamonds", "Jack of Hearts", "Jack of Clubs"]
the_tens = ["10 of Spades", "10 of Diamonds", "10 of Hearts", "10 of Clubs"]

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
        self.split = []
        self.bank = bank
        self.bet = bet
        self.busted = 0
        self.bustedSplit = 0
        self.bj = 0
        self.bjSplit = 0
        self.aces = 0
        self.sum_total = 0
        self.history = []
        self.doubles = 0
        self.doubleDown = 0
        self.doubleDownSplit = 0
    
    def checkDoubles(self):
        check_1st = [self.hand[0].face]
        check_2nd = [self.hand[1].face]
        check_doubles = []
        for card in self.hand:
            check_doubles.append(card.count())
        if any(item in the_aces for item in check_1st) and any(item in the_aces for item in check_2nd)\
             or any(item in the_kings for item in check_1st) and any(item in the_kings for item in check_2nd)\
             or any(item in the_queens for item in check_1st) and any(item in the_queens for item in check_2nd)\
             or any(item in the_jacks for item in check_1st) and any(item in the_jacks for item in check_2nd):
            self.doubles = 1
            print("You can Split Doubles")
        elif self.total() < 20 and check_doubles[0] == check_doubles[1]:
            self.doubles = 1
            print("You can Split Doubles")
    
    def checkBust(self):
        if self.total() > 21:
            print(f"{self.name} Busts.")
            self.busted = 1

    def checkSplitBust(self):
        if self.totalSplit() > 21:
            print(f"{self.name} Busts.")
            self.bustedSplit = 1

    def showBet(self):
        print(f"{self.name} has bet ${'{:.2f}'.format(self.bet)}")

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
        print(f"{self.name} has ${'{:.2f}'.format(self.bank)}")
               
    def getCard(self, deck):
        self.hand.append(deck.dealCard())
        return self.hand

    def getSplitCard(self, deck):
        self.split.append(deck.dealCard())
        return self.split
    
    def discard(self):
        return self.hand.clear(), self.split.clear()
        
    def show(self):
        for card in self.hand:
            card.show()
    
    def showSplit(self):
        for card in self.split:
            card.show()
    
    def show1(self):
        self.hand[0].show()

    def total(self):
        total = []
        for card in self.hand:
            total.append(card.count())
        sum_total = sum(total)
        aces = total.count(11)
        if aces > 0 and sum_total > 21:
            sum_total = sum_total - 10
            return sum_total
        elif aces > 1 and sum_total > 31:
            sum_total = sum_total - 20
            return sum_total
        elif aces > 2 and sum_total > 31:
            sum_total = sum_total - 30
            return sum_total
        elif aces > 3 and sum_total > 41:
            sum_total = sum_total - 40
            return sum_total
        else:
            return sum_total
    
    def totalSplit(self):
        total = []
        for card in self.split:
            total.append(card.count())
        sum_total = sum(total)
        aces = total.count(11)
        if aces > 0 and sum_total > 21:
            sum_total = sum_total - 10
            return sum_total
        elif aces > 1 and sum_total > 31:
            sum_total = sum_total - 20
            return sum_total
        elif aces > 2 and sum_total > 31:
            sum_total = sum_total - 30
            return sum_total
        elif aces > 3 and sum_total > 41:
            sum_total = sum_total - 40
            return sum_total
        else:
            return sum_total

    def showSplitTotal(self):
        total = []
        for card in self.split:
             total.append(card.count())
        sum_total = sum(total)
        aces = total.count(11)
        if aces > 0 and sum_total > 21:
            print(f'{self.name} has a total of {sum_total - 10}')
        elif aces > 0 and sum_total < 21:
            print(f'{self.name} has a total of {sum_total - 10} or {sum_total}')
        elif aces > 1 and sum_total > 31:
            print(f'{self.name} has a total of {sum_total - 20}')
        elif aces > 1 and sum_total < 31:
            print(f'{self.name} has a total of {sum_total - 20} or {sum_total - 10}')
        elif aces > 2 and sum_total > 41:
            print(f'{self.name} has a total of {sum_total - 30}')
        elif aces > 2 and sum_total < 41:
            print(f'{self.name} has a total of {sum_total - 30} or {sum_total - 20}')
        elif aces > 3:
            print(f'{self.name} has a total of {sum_total - 40} or {sum_total - 30} ')
        else:
            print(f'{self.name} has a total of {sum_total}')
        return self.name    
    
    def showTotal(self):
        total = []
        for card in self.hand:
             total.append(card.count())
        sum_total = sum(total)
        aces = total.count(11)
        if aces > 0 and sum_total > 21:
            print(f'{self.name} has a total of {sum_total - 10}')
        elif aces > 0 and sum_total < 21:
            print(f'{self.name} has a total of {sum_total - 10} or {sum_total}')
        elif aces > 1 and sum_total > 31:
            print(f'{self.name} has a total of {sum_total - 20}')
        elif aces > 1 and sum_total < 31:
            print(f'{self.name} has a total of {sum_total - 20} or {sum_total - 10}')
        elif aces > 2 and sum_total > 41:
            print(f'{self.name} has a total of {sum_total - 30}')
        elif aces > 2 and sum_total < 41:
            print(f'{self.name} has a total of {sum_total - 30} or {sum_total - 20}')
        elif aces > 3:
            print(f'{self.name} has a total of {sum_total - 40} or {sum_total - 30} ')
        else:
            print(f'{self.name} has a total of {sum_total}')
        return self.name

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
    elif dealer.total() == 21:
        print("Dealer has 21")
    elif dealer.total() >= 17 and dealer.total() < 21:
        print("Dealer has total of:", dealer.total())
        print("Dealer must stay with:")
        dealer.show()
        print("")

def calcWinner():
    for player in players:
        if player.total() < dealer.total() and dealer.total() <= 21:
            print(f"{player.name} loses ${'{:.2f}'.format(player.bet)} with {player.total()}")
            player.history.append(f"{player.name} loses ${'{:.2f}'.format(player.bet)} with {player.total()}")
            player.betLost()
            if player.doubleDown == 1:
                player.betLost()
                print(f"{player.name} also loses ${'{:.2f}'.format(player.bet)} because of Double Down bet.")
                player.history.append(f"{player.name} also loses ${'{:.2f}'.format(player.bet)} because of Double Down bet.")
        if player.total() > 21:
            print(f"{player.name} busted before dealer showed hand and loses ${'{:.2f}'.format(player.bet)}")
            player.history.append(f"{player.name} busted before dealer showed hand and loses ${'{:.2f}'.format(player.bet)}")
            player.betLost()               
        elif player.total() < dealer.total() and dealer.busted == 1:
            print(f"{player.name} wins ${'{:.2f}'.format(player.bet)} with {player.total()}")
            player.history.append(f"{player.name} wins ${'{:.2f}'.format(player.bet)} with {player.total()}")
            player.betWon()
            if player.doubleDown == 1:
                player.betWon()
                print(f"{player.name} also wins ${'{:.2f}'.format(player.bet)} because of Double Down bet.")
                player.history.append(f"{player.name} also wins ${'{:.2f}'.format(player.bet)} because of Double Down bet.")
        elif player.total() == dealer.total() and dealer.total() <=21:
            print(f'{player.name} pushes with {player.total()}')
            player.history.append(f'{player.name} pushes. with {player.total()}')
        elif player.total() == 21 and player.bj == 1:
            print(f"{player.name} wins ${'{:.2f}'.format(player.bet * 1.5)} with {player.total()} ")
            player.history.append(f"{player.name} wins ${'{:.2f}'.format(player.bet * 1.5)} with {player.total()} ")
            player.wonBj()
        elif player.total() == 21:
            print(f"{player.name} wins ${'{:.2f}'.format(player.bet)} with {player.total()}")
            player.history.append(f"{player.name} wins ${'{:.2f}'.format(player.bet)} with {player.total()}")
            player.betWon()
            if player.doubleDown == 1:
                player.betWon()
                print(f"{player.name} also wins ${'{:.2f}'.format(player.bet)} because of Double Down bet.")
                player.history.append(f"{player.name} also wins ${'{:.2f}'.format(player.bet)} because of Double Down bet.")            
        elif player.total() > dealer.total() and dealer.total() < 21:
            print(f"{player.name} wins ${'{:.2f}'.format(player.bet)} with {player.total()}")
            player.history.append(f"{player.name} wins ${'{:.2f}'.format(player.bet)} with {player.total()}")
            player.betWon()
            if player.doubleDown == 1:
                player.betWon()
                print(f"{player.name} also wins ${'{:.2f}'.format(player.bet)} because of Double Down bet.")
                player.history.append(f"{player.name} also wins ${'{:.2f}'.format(player.bet)} because of Double Down bet.")

def calcSplitWinner():
    for player in players:
        if len(player.split) != 0:
            if player.totalSplit() < dealer.total() and dealer.total() <= 21:
                print(f"{player.name} #2 loses ${'{:.2f}'.format(player.bet)} with {player.totalSplit()}")
                player.history.append(f"{player.name} #2 loses ${'{:.2f}'.format(player.bet)} with {player.totalSplit()}")
                player.betLost()
            if player.totalSplit() > 21:
                print(f"{player.name} #2 busted before dealer showed hand and loses ${'{:.2f}'.format(player.bet)}")
                player.history.append(f"{player.name} #2 busted before dealer showed hand and loses ${'{:.2f}'.format(player.bet)}")
                player.betLost()
            elif player.totalSplit() < dealer.total() and dealer.busted == 1:
                print(f"{player.name} #2 wins ${'{:.2f}'.format(player.bet)} with {player.totalSplit()}")
                player.history.append(f"{player.name} #2 wins ${'{:.2f}'.format(player.bet)} with {player.totalSplit()}")
                player.betWon()
            elif player.totalSplit() == dealer.total() and dealer.total() <=21:
                print(f'{player.name} #2 pushes with {player.totalSplit()}')
                player.history.append(f'{player.name} #2 pushes. with {player.totalSplit()}')
            elif player.totalSplit() == 21 and player.bjSplit == 1:
                print(f"{player.name} #2 wins ${'{:.2f}'.format(player.bet * 1.5)} with {player.totalSplit()} ")
                player.history.append(f"{player.name} #2 wins ${'{:.2f}'.format(player.bet * 1.5)} with {player.totalSplit()} ")
                player.wonBj()
            elif player.totalSplit() == 21:
                print(f"{player.name} #2 wins ${'{:.2f}'.format(player.bet)} with {player.totalSplit()}")
                player.history.append(f"{player.name} #2 wins ${'{:.2f}'.format(player.bet)} with {player.totalSplit()}")
                player.betWon()
            elif player.totalSplit() > dealer.total() and dealer.total() < 21:
                print(f"{player.name} #2 wins ${'{:.2f}'.format(player.bet)} with {player.totalSplit()}")
                player.history.append(f"{player.name} #2 wins ${'{:.2f}'.format(player.bet)} with {player.totalSplit()}")
                player.betWon()
        else:
            continue

def newGame():
    global dealer, deck1
    dealer = Player("Dealer")
    deck1 = Deck()
    deck1.shuffle()
    deck1.buildCards()

def enterPlayers():
    try:
        print("")
        print(f'Game supports 1-6 players.')
        print(f'Current players: {len(players)}\n')
        while True:
            p_count = int(input(f'How many players are joining the game?: '))
            if 1 <= (len(players) + p_count) < 7:
                for i in range(p_count):
                    print(f"What is player {i + 1}'s name?")
                    getPlayers()
                    currentPlayers()
                break
            else:
                print("Entry violates player min/maximum, try again.")
        
    except:
        print("Please enter a number.")
        #enterPlayers()
    
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
    dealer.busted = 0
    dealer.bj = 0
    dealer.discard()
    for player in players:
        player.discard()
        player.bet = 0
        player.bj = 0
        player.bjSplit = 0
        player.busted = 0
        player.bustedSplit = 0
        player.aces = 0
        player.doubles = 0
        player.doubleDown = 0
        removePlayers()

def playerOption():
        for player in players:
            player.checkDoubles()
        for player in players:
            while player.total() < 21:
                if player.bj == 1:
                    break
                if player.doubles == 1 and len(player.hand) == 2:
                    print(f"{player.showTotal()}, choose an option.")
                    print("You can split doubles.")
                    choice = input("|1. Hit | 2. Stay | 3. Split : ")
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
                    elif choice == "3":
                        player.split.append(player.hand.pop())
                        print(player.name, "Hand #1 Has:")
                        player.getCard(deck1)
                        player.show()
                        player.total()
                        player.showTotal()
                        if player.total() == 21:
                            player.bj == 1
                            break
                        if len(player.hand) == 2 and 8 < player.total() < 12:
                            print(f"{player.showTotal()}, choose an option.")
                            print("You can Double Down if first two cards equals to 9, 10, or 11.")
                            choice = input("|1. Hit | 2. Stay | 3. Double Down : ")
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
                            elif choice == "3":
                                player.doubleDown = 1
                                player.getCard(deck1)
                                print(player.name, "Has:")
                                player.show()
                                player.total()
                                player.showTotal()
                                print("")
                                break                                                             
                        else:
                            while player.total() < 21:    
                                choice = input("|1. Hit | 2. Stay | : ")
                                print("")
                                if choice == "1":
                                    player.getCard(deck1)
                                    player.show()
                                    player.total()
                                    player.showTotal()
                                    player.checkBust()
                                    print("")
                                    continue
                                elif choice == "2":
                                    break                                               
                            print(player.name, "Hand #2 Has:")
                            player.getSplitCard(deck1)
                            player.showSplit()
                            player.totalSplit()
                            player.showSplitTotal()
                            if player.totalSplit() == 21:
                                player.bjSplit = 1
                                break
                            if len(player.split) == 2 and 8 < player.totalSplit() < 12:
                                print(f"{player.showTotal()}, choose an option.")
                                print("You can Double Down if first two cards equals to 9, 10, or 11.")
                                choice = input("|1. Hit | 2. Stay | 3. Double Down : ")                            
                                if choice =="1":
                                    player.getSplitCard(deck1)
                                    print(player.name, "Hand #2 Has:")
                                    player.showSplit()
                                    player.totalSplit()
                                    player.showSplitTotal()
                                    player.checkSplitBust()
                                    print("")
                                    while player.totalSplit() < 21:
                                        choice = input("|1. Hit | 2. Stay | : ")
                                        print("")
                                        if choice == "1":
                                            player.getSplitCard(deck1)
                                            player.showSplit()
                                            player.totalSplit()
                                            player.showSplitTotal()
                                            player.checkSplitBust()
                                            print("")
                                            continue
                                        elif choice == "2":
                                            break                                
                                elif choice =="2":
                                    break
                                elif choice == "3":
                                    player.doubleDownSplit = 1
                                    player.getSplitCard(deck1)
                                    print(player.name, "Has:")
                                    player.showSplit()
                                    player.totalSplit()
                                    player.showTotalSplit()
                                    print("")
                                    break                            
                            while player.totalSplit() < 21:
                                choice = input("|1. Hit | 2. Stay | : ")
                                print("")
                                if choice == "1":
                                    player.getSplitCard(deck1)
                                    player.showSplit()
                                    player.totalSplit()
                                    player.showSplitTotal()
                                    player.checkSplitBust()
                                    print("")
                                    continue
                                elif choice == "2":
                                    break
                    else:
                        print("Not a valid option.")
                elif len(player.hand) == 2 and 8 < player.total() < 12:
                    print(f"{player.showTotal()}, choose an option.")
                    print("You can Double Down if first two cards equals to 9, 10, or 11.")
                    choice = input("|1. Hit | 2. Stay | 3. Double Down : ")
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
                    elif choice == "3":
                        player.doubleDown = 1
                        player.getCard(deck1)
                        print(player.name, "Has:")
                        player.show()
                        player.total()
                        player.showTotal()
                        print("")
                        break
                if len(player.split) == 0:
                    print(f"{player.showTotal()}, choose an option.")
                    choice = input("|1. Hit | 2. Stay | : ")
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
                else:
                    break

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
        print("There are currently no players.\n")
        ask_add = input("Would you like to add player(s)? (Y/N): ").upper()
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
        if len(players) != 0:
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
        else:
            break

def gameMenu():
    while True:
        print("*******************************")
        print("*/\/\*   BlackJack Menu  */\/\*")
        print("*******************************")
        print("*      1. Start / Deal        *")
        print("*      2. Add Player(s)       *")
        print("*      3. Remove Player(s)    *")
        print("*      4. Current Player(s)   *")
        print("*      5. Game History        *")
        print("*      6. Rules to play       *")
        print("*      7. Quit Game           *")
        print("*******************************")    
        get_user_choice = input("Pick an option: ")
        if get_user_choice == "1":
            checkEmptyPlayers()
            break
        elif get_user_choice == "2":
            enterPlayers()
        elif get_user_choice =="3":
            playerLeaves()
        elif get_user_choice == "4":
            currentPlayers()
            gameHistory()
        elif get_user_choice == "5":
            gameHistory()
        elif get_user_choice == "6":
            print("There is no insurance/surrendering/resplitting, or dealer hitting on soft 17.")
            print("Every other rule is standard from wikipedia's rules for BlackJack")
            print("")
            full_rules = input("Do you want review full rules on wikipedia? (Y/N) ").upper()
            if full_rules == "Y":
                webbrowser.open("https://en.wikipedia.org/wiki/Blackjack")
            elif full_rules == "N":
                continue
            else:
                print("That wasn't a valid option")
        elif get_user_choice == "7":
            quit()
        else:
            print("That was not a valid option")

def gameHistory():
    if len(players) != 0:
        print("------Player Game History------")
        for player in players:
            game = 1
            for item in player.history:
                print(f'Game {game}: {item}')
                game += 1
        print("-------------------------------\n")
    else:
        print("There are no players to show game history for.")

def app():
    while True:
        gameMenu()
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
            calcSplitWinner()
            currentPlayers()
            clearHands()
            removePlayers()
        elif dealer.total() == 21:
            print(f'Dealer has BlackJack')
            print("")
            dealer.show()
            print("")
            calcWinner()
            calcSplitWinner()
            currentPlayers()
            clearHands()
            removePlayers()

app()