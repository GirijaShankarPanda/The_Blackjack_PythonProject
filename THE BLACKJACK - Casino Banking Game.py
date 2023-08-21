
# ## <ins>THE BLACKJACK</ins> (Casino Banking Game) :

# ### `GLOBAL VARIABLE`

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True


# ### `CARD CLASS`

class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + " of " + self.suit


# ### `DECK CLASS`

class Deck():
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    # This "__str__" method is only for printing the contents of deck
    def __str__(self):
        deck_comp = ''  
        for card in self.deck:
            deck_comp += '\n '+card.__str__() 
        return 'The deck carries:' + deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card


# **Check :**</br>

test_deck = Deck()
print(test_deck)

# AFTER SHUFFLING THE DECK:

test_deck.shuffle()
print(test_deck)


# ### `HAND CLASS`

class Hand():
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0    # An attribute to keep track of aces
        
    def add_card(self,card):
        # card passed in
        # from Deck.deal() --> single card(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]
        
        # Track for Aces
        if card.rank == 'Ace':
            self.aces += 1
            
    def adjust_ace(self):
        # If total value > 21 and still have an Ace
        # then change my Ace to be 1 instead of 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 


# **Check** for **`add_card()`** :

test_deck = Deck()
test_deck.shuffle()

# PLAYER
test_player = Hand()

# Deal 2 card from the Deck Card(suit,rank)
print(test_deck.deal())
test_player.add_card(test_deck.deal())
print(test_player.value)


# ### `CHIPS CLASS`

class Chips:
    
    def __init__(self, total=100):
        self.total = total  
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


# ### `TAKE_BET() FUNCTION`

def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry! a bet must be an Integer.")
        else:
            if chips.bet > chips.total:
                print(f'Sorry! you have only {chips.total} chips to bet.')
            else:
                break


# ### `HIT() FUNCTION`

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_ace()


# ### `HIT_OR_STAND() FUNCTION`

def hit_or_stand(deck,hand):
    global playing     # To control an upcoming while loop
    
    while True:
        x = input("Would you like to Hit or Stand? Enter h/s: ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player Stands, Dealer's turn")
            playing = False
        else:
            print("Sorry! I didn't understand, please enter 'h' or 's' only.")
            continue
        break


# ### `SHOW_CARDS() FUNCTION`

def show_some(player,dealer):
    
    # Show only ONE card of Dealer's hand
    print("\nDEALER'S HAND: ")
    print("Hidden Card!")
    print(dealer.cards[1])
    
    # Show all (2 cards) of Player's hand
    print("\nPLAYER'S HAND: ", *player.cards, sep='\n')
    
def show_all(player,dealer):
    
    # Show all Dealer's cards
    print("\nDEALER'S HAND: ", *dealer.cards, sep='\n')
    # Display value
    print(f"Value of Dealer's Hand is: {dealer.value}")
    
    # Show all Player's cards
    print("\nPLAYER'S HAND: ", *player.cards, sep='\n') 
    # Display value
    print(f"Value of Player's Hand is: {player.value}")

# ### `PLAYER_BUSTS()` & `PLAYER_WINS() FUNCTION`

def player_busts(player,dealer,chips):
    print("Player BUSTS!")
    chips.lose_bet()
    
def player_wins(player,dealer,chips):
    print("Player WINS!")
    chips.win_bet()
    
def dealer_busts(player,dealer,chips):
    print("Player WINS, Dealer BUSTED!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer WINS!")
    chips.lose_bet()
    
def push(player,dealer):
    print("A TIE between Dealer and Player! It's a PUSH.")


# ### `THE ENDGAME`

while True:
    
    print("WELCOME TO BLACKJACK!")
    
    # Create and shuffle the deck,dealing two cards to each player.
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # Setting up the Player's chips
    player_chips = Chips()
    
    # Prompting the Player for their bet
    take_bet(player_chips)
    
    # Show cards (keeping 1 Dealer's card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:    # Global variable from hit_or_stand() function
        # Prompting the Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        # Show cards (keeping 1 Dealer's card hidden)
        show_some(player_hand,dealer_hand)
        
        # If Player's hand exceed 21
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
            
    # If Player hasn't busted
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
            
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips) 
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips) 
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
            
        # Total Chips the Player have
        print(f"\n Player's winning stand at {player_chips.total}")
        
        # For playing again
        new_game = input("Would you like to play another hand? y/n: ")
        
        if new_game[0].lower() == 'y':
            playing = True
            continue
        elif new_game[0].lower() == 'n':
            print("Thank you for playing!")
        else:
            print("Sorry! I didn't understand! Enter 'y' or 'n': ")
        break

