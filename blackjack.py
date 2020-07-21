import random
playing = True
shape = ('Heart' , 'Diamond', 'Spade' , 'Clover')
number = ('Ace','two','three','four','five','six','seven','eight','nine','ten','Jack','Queen','King')
card_value = {'Ace':11,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'Jack':10,'Queen':10,'King':10}
class Card:
    def __init__(self,shape,number):
        self.shape=shape
        self.number=number

    def __str__(self):
        return self.shape + '  ->  '+ self.number
    
class Deck:
    def __init__(self):
        self.deck = []
        for s in shape:
            for n in number:
                   self.deck.append(Card(s,n))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

    def __str__(self):
        deck_comp=' '
        for card in self.deck:
            deck_comp+= '\n' + card.__str__()
        return ("The deck has : "+ deck_comp)

class Hand:
    def __init__(self):
        self.cards = []
        self.value= 0
        self.ace= 0

    def add_card(self,card):
        self.cards.append(card)  # deal return card , (poping card) will append here
        self.value += card_value[card.number]
        if card.number == 'Ace':
            self.ace+=1

    def adjust_for_ace(self):
        while self.value>21 and self.ace:
            self.value -=10
            self.ace-=1

class Chips:
    def __init__(self, total = 500):
        self.total = total
        self.bet=0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
        
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Enter the amount of chips that you are willing to bet  :  "))
        except:
            print("Please enter the integer value only")
        else:
            if chips.bet > chips.total:
                 print("Alert!!! The chips amount must be in the range of {}".format(chips.total))
            else:
                break

def hit(deck,hand):
    p = deck.deal()
    print("you are hitting a card " )
    print(p)
    hand.add_card(p)
    print(hand.value)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing
    while True:
        x = input("\nAre you now going to hit or stand ?  \nh -> Hit \ns -> Stand\n")
        print("---------------------------------------------------------------------")
        if x[0].lower() == 'h':
            print(hand.value)
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("\n\nYou are decided to stand\nDealer will play now !")
            playing = False
            break
        else:
            print("Enter the valid input (h or s)")

def player_busts(player,dealer,chips):
    print("Dealer Win ! Player Busts")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("****************Player Win****************")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("****************Player Win ! Dealer Busts****************")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("****************Dealer Win****************")
    chips.lose_bet()

def push(player,dealer):
    print("****************Player and Dealer tie !! ****************")

def show_some(player,dealer):
    print("Dealer Cards ")
    print("--------------------------------------------------------------")
    print("Dealer First cart is hidden")
    print(dealer.cards[1])
    print("\nPlayer Cards ")
    print("--------------------------------------------------------------")
    print(player.cards[0])
    print(player.cards[1])
    
def show_all(player,dealer):
    print("\n\n--------------------------------------------------------------")
    print("The Dealer Cards are \n")
    print("--------------------------------------------------------------\n")
    for card in dealer.cards:
        print(card)
    print("\n\n--------------------------------------------------------------")
    print("The Player Cards are \n")
    print("--------------------------------------------------------------\n")
    for card in player.cards:
        print(card)
    
while True:
    print("*=*=*=*=*=*=*=*=*=*= BLACK JACK *=*=*=*=*=*=*=*=*=*=*")
    deck = Deck()
    deck.shuffle()

    player = Hand()
    p = deck.deal()
    player.add_card(p)
    p = deck.deal()
    player.add_card(p)
    print(player.value)
    
    dealer = Hand()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player,dealer)

    while playing:
        hit_or_stand(deck,player)
        show_some(player,dealer)
        if player.value > 21 :
            player_busts(player,dealer,player_chips)
            break
    if player.value <=21:
        while dealer.value < player.value:
            hit(deck,dealer)
        show_all(player,dealer)

        if dealer.value >21 :
            dealer_busts(player,dealer,player_chips)

        elif dealer.value > player.value:
            dealer_wins(player,dealer,player_chips)

        elif dealer.value < player.value:
            player_wins(player,dealer,player_chips)

        else:
            push(player,dealer)

    print("\n The total chips of player at the end are {} ".format(player_chips.total))

    again = input("\nWould you like to play again ? \nY -> Yes \nN -> No\n")
    if again[0].lower() == 'y':
        playing = True
        continue
    else:
        break
            

















            













                
