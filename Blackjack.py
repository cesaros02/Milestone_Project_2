
"""
Corregir el escenario cuando vuelas y hay al menos un ace (adjust_for_aces is applied)
"""

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
            
    def __int__(self):
        return values[self.rank]
    
    def __str__(self):
        return f"{self.rank} of {self.suit} \n"


class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    
    def __str__(self):
        return ''.join(str (e) for e in self.deck)

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.card = card
        self.cards.append(self.card)
        self.value += values[self.card.rank]
        if self.card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        self.value -= self.aces*10


class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
        print(f"You won. You have {self.total} remaining chips.")
        
    
    def lose_bet(self):
        self.total -= self.bet
        print(f"You lost. You have {self.total} remaining chips.")


def take_bet(Chips):
    while True:
        try:
            Chips.bet = int(input("Enter your bet:"))
        except:
            print("Enter a number")
        else:
            if Chips.bet > Chips.total:
                print("You can't bet more than you have...")
                
            else:
                print("Ok, beat taken.")
                break





def hit(deck,hand):
    card_played = test_deck.deal()
    hand.add_card(card_played)


def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    a = True
    option = input("Want to hit or stand? Enter \"hit\" or \"stand\": ")

    while a == True:
        try:
            option = option.lower()
            if option == "hit":
                hit(deck,hand)
                #
                break
            elif option == "stand":
                playing = False
                break
            else:
                print("invalid option, enter only \"hit\" or \"stand\"...")
                option = input("Want to hit or stand? Enter \"hit\" or \"stand\": ")
        except:
            print("invalid option, enter only \"hit\" or \"stand\"...")
            option = input("Want to hit or stand? Enter \"hit\" or \"stand\": ")
    
    return playing


def show_some(player,dealer):
    print("\n***Dealer's hand***")
    for card in dealer.cards:
        if card == dealer.cards[0]:
            print("****\n")
        else:
            print(str(card))  
    
    print("\n***Player's hand***")  
    for card in player.cards:
        print(str(card))    
    
    
def show_all(player,dealer):
    print("\n***Dealer's hand***")
    for card in dealer.cards:
        print(str(card))  
    print("\n***Player's hand***")  
    for card in player.cards:
        print(str(card))    


def player_busts(player):
    print(f"Player busted, hand value is {player.value}")
    player_chips.total -= player_chips.bet
    player_chips.bet = 0

def player_wins(player):
    print(f"Player wins, hand value is {player.value}")
    player_chips.total += player_chips.bet
    player_chips.bet = 0


def dealer_busts(dealer):
    print(f"Dealer busted, hand value is {dealer.value}")
    player_chips.total += player_chips.bet
    player_chips.bet = 0


def dealer_wins(dealer):
    print(f"Dealer wins, hand value is {dealer.value}")
    player_chips.total -= player_chips.bet
    player_chips.bet = 0

    
def push():
    print(f"no se que es is {player.value}")




if __name__ == "__main__":
    playing = True
    player_chips = Chips()


    print("Welcome to the Blackjack game!!!")

    while True:
        test_deck = Deck()
        dealer_hand = Hand()
        player_hand = Hand()

        print(f"Your current ammount of chips is {player_chips.total}")
        

        test_deck.shuffle()
        take_bet(player_chips)


        for a in range(2):
            hit(test_deck,player_hand)
            hit(test_deck,dealer_hand)

        show_some(player_hand, dealer_hand)

        while playing:
            hit_or_stand(test_deck, player_hand)
            show_some(player_hand, dealer_hand)

            if player_hand.value > 21:
                if player_hand.aces > 0:
                    player_hand.adjust_for_ace()
                    break
                playing = False
                player_busts(player_hand)
            elif player_hand.value == 21:
                player_wins(player_hand)
                playing = False

        if player_hand.value < 21:
            show_all(player_hand, dealer_hand)
            if dealer_hand == 21:
                dealer_wins(dealer_hand)

            while dealer_hand.value < 17:
                hit(test_deck, dealer_hand)
                if dealer_hand.value > 21:
                    dealer_busts(dealer_hand)
                else:
                    if dealer_hand.value > player_hand.value:
                        dealer_wins(dealer_hand)

            if dealer_hand.value == 17:
                if dealer_hand.value > player_hand.value:
                    dealer_wins(dealer_hand)
        elif player_hand.value == 21:
            player_wins(player_hand)
        

        show_all(player_hand, dealer_hand)
            
        print(f"Current ammount of chips is {player_chips.total}")
        # print(f"Playing == {playing}")
        # show_all(player_hand, dealer_hand)
        if (player_chips.total < 1):
            break
                
        keepplay = input("Want to keep playing? (y/n): ").lower()
        if keepplay == 'y':
            continue
        elif keepplay == 'n':
            break
    print("Thanks for playing with us!")

        