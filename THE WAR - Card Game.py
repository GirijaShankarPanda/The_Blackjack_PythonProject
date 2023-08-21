#!/usr/bin/env python
# coding: utf-8

# ## <ins>THE WAR</ins> (Card Game) :

# ### `GLOBAL VARIABLE`

# In[1]:


# SUIT,RANK,VALUE
import random
suits = ('Hearts', 'Diamond', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


# ### `CARD CLASS`

# In[2]:


class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit


# #### Check

# In[3]:


three_clubs = Card("Clubs","Three")


# In[4]:


two_hearts = Card("Hearts","Two")


# In[5]:


three_clubs.value


# In[6]:


three_clubs.rank


# In[7]:


two_hearts.value < three_clubs.value


# ### `DECK CLASS`

# In[8]:


class Deck():
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                # Create the Card Object
                created_card = Card(suit,rank)
                
                self.all_cards.append(created_card)   
            
    def shuffle(self):
        random.shuffle(self.all_cards)       


# #### Check
# **Printing all cards in the deck.**

# In[9]:


new_deck = Deck()


# In[10]:


for card_object in new_deck.all_cards:
    print(card_object)


# **printing a card after shuffle**

# In[11]:


new_deck.shuffle()


# In[12]:


# Card at the bottom of the Deck
print(new_deck.all_cards[-1])


# In[13]:


class Deck():
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                # Create the Card Object
                created_card = Card(suit,rank)
                
                self.all_cards.append(created_card)   
            
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()


# #### Check

# In[14]:


new_deck = Deck()


# In[15]:


new_deck.shuffle()


# In[16]:


mycard = new_deck.deal_one()


# In[17]:


print(mycard)


# In[18]:


len(new_deck.all_cards)


# ### `PLAYER CLASS`

# In[19]:


class Player():
    
    def __init__(self,name):
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            # List of multiple Card Object
            self.all_cards.extend(new_cards)
            
        else:
            # For a single Card Object
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


# #### Check

# In[20]:


new_player = Player('John')


# In[21]:


print(new_player)


# In[22]:


print(mycard)


# In[23]:


new_player.add_cards(mycard)


# In[24]:


print(new_player)


# In[25]:


print(new_player.all_cards[0])


# In[26]:


new_player.add_cards([mycard,mycard,mycard])


# In[27]:


print(new_player)


# In[28]:


new_player.remove_one()


# In[29]:


print(new_player)


# # `GAME LOGIC`

# In[33]:


# GAME SETUP
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


# In[34]:


game_on = True


# In[35]:


round_num = 0

while game_on:
    round_num += 1
    print(f'Round {round_num}')
    
    if len(player_one.all_cards) == 0:
        print('Player One, out of cards! Player Two Wins!')
        game_on = False
        break
        
    if len(player_two.all_cards) == 0:
        print('Player Two, out of cards! Player One Wins!')
        game_on = False
        break
        
    # START A NEW ROUND
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    # AT WAR
    at_war = True
    
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            at_war = False
            
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            
            at_war = False
            
        else:
            print('WAR!')
            
            if len(player_one.all_cards) < 5:
                print("Player One unable to declare War.")
                print("PLAYER TWO WINS!")
                game_on = False
                break
                
            elif len(player_one.all_cards) < 5:
                print("Player Two unable to declare War.")
                print("PLAYER ONE WINS!")
                game_on = False
                break
                
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

