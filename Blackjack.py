
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
        print("\\\\Adjusting for aces...\\\\")
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
    card_played = deck.deal()
    hand.add_card(card_played)



def hit_or_stand(deck,hand):
    while True:
        try:
            option = input("Want to hit or stand? Enter \"hit\" or \"stand\": ").lower()
            if option == "hit":
                print("\YouChoseHIT")
                hit(deck,hand)
                #
                return "hit"
            elif option == "stand":
                print("\YouChoseSTAND")
                return "stand"
            else:
                print("invalid option, enter only \"hit\" or \"stand\"...")
                option = input("Want to hit or stand? Enter \"hit\" or \"stand\": ")
        except:
            print("invalid option, enter only \"hit\" or \"stand\"...")
            option = input("Want to hit or stand? Enter \"hit\" or \"stand\": ")


def show_some(player,dealer):
    print("\n***Dealer's hand***")
    for card in dealer.cards:
        if card == dealer.cards[0]:
            print("****")
        else:
            print(str(card))

    print("\n***Player's hand***")
    for card in player.cards:
        print(str(card))
    print(f"Player hand currently is {player.value}")
    print(f"----------------------show some--------------------------")

def show_all(player,dealer):
    print("\n***Dealer's hand***")
    for card in dealer.cards:
        print(str(card))
    print(f"Dealer hand currently is {dealer.value}")

    print("\n***Player's hand***")
    for card in player.cards:
        print(str(card))

    print(f"Player final value is {player.value}")
    print(f"-----------------------show all-------------------------")



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
    dealeroutcome = False
    player_chips = Chips()
    option = ""


    print("Welcome to the Blackjack game!!!")

    while True:
        dealeroutcome = False
        if playing == False:
            break
        else:
            test_deck = Deck()
            dealer_hand = Hand()
            player_hand = Hand()
            

            print(f"Your current ammount of chips is {player_chips.total}")


            test_deck.shuffle()
            take_bet(player_chips)


            for a in range(2):
                hit(test_deck,player_hand)
                hit(test_deck,dealer_hand)

            print("&These are your initial cards...")
            show_some(player_hand, dealer_hand)
            if player_hand.value == 21:
                print("\\\\player hand is 21, great!!!!\\\\")
                player_wins(player_hand)
                pass

            while playing:
                if dealeroutcome == False:
                    print(f"*****************stating iteration of while playing*******************")
                
                    option = hit_or_stand(test_deck, player_hand)
                    
                    if option == "hit":
                        show_some(player_hand, dealer_hand)

                        if player_hand.value <= 21:
                            print("\\\\player hand is less or equal than 21\\\\")
                            if player_hand.value == 21:
                                print("\\\\player hand is 21, great!!!!\\\\")
                                player_wins(player_hand)
                                break
                        elif player_hand.aces > 0:
                                player_hand.adjust_for_ace()
                                show_some(player_hand, dealer_hand)
                                if player_hand.value == 21:
                                    print("\\\\player hand is 21 after adjusting for aces, Lucky you!!!!\\\\")
                                    player_wins(player_hand)
                                    break
                        else:
                            player_busts(player_hand)
                            break

                    elif option == "stand":
                        while True:
                            show_all(player_hand, dealer_hand)
                            if dealer_hand.value >= 21:
                                if dealer_hand.value == 21:
                                    dealer_wins(dealer_hand)
                                    dealeroutcome = True
                                    break
                                else:
                                    dealer_busts(dealer_hand)
                                    dealeroutcome = True
                                    break
                            elif dealer_hand.value <17:
                                if dealer_hand.value == 17:
                                    dealer_wins(dealer_hand)
                                    dealeroutcome = True
                                    break
                                else:
                                    hit(test_deck, dealer_hand)
                            elif dealer_hand.value > player_hand.value:
                                dealer_wins(dealer_hand)
                                dealeroutcome = True
                                break
                            else:
                                hit(test_deck, dealer_hand)
                else:
                        break




        print("++++Somebody won, let's see the final hand++++\n")
        show_all(player_hand, dealer_hand)
        print("\n=====End of the current table====\n\n")

        print(f"After this round, your current ammount of chips is {player_chips.total}")

        if (player_chips.total < 1):
            print("It seems you have no chips! =(")
            break

        keepplay = input("Want to keep playing? (y/n): ").lower()
        if keepplay == 'y':
            continue
        elif keepplay == 'n':
            playing = False


    print("Thanks for playing with us!")

