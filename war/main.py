import random as rand
import json

def pretty_print(val):
    print(json.dumps(val, indent=2))

def rand_pop(iter):
    i = rand.randint(0, len(iter)-1)
    return iter.pop(i)

def shuffle(cards):
    rslt = []
    while cards != []:
        rslt.append(rand_pop(cards))
    return rslt

class Player:

    def __str__(self):
        return str(self.hand)

    def __init__(self) -> None:
        self.hand = []
        self.won_cards = []
    
    def next(self):
        rtrn = self.hand.pop(0)            
        if self.hand == []:
            if self.won_cards != []:
                self.hand = shuffle(self.won_cards)
                self.won_cards = []
            else:
                rtrn = None
        return rtrn

    def recieves(self, vals):
        self.won_cards += vals

class Main:

    CARDS = list(range(2,15)) #2 - Ace(14)
    NUM_SUITS = 4

    NUM_PLAYERS = 2

    def __init__(self) -> None:
        self.deck = self.new_deck()

        self.players = [Player() for i in range(self.NUM_PLAYERS)]

        for i, plyr in enumerate(self.players):
            plyr.hand = self.deck[len(self.deck)//(i+2):]

        self.has_won = False
        
        # pretty_print([str(plyr) for plyr in players])
    
    def rem_player(self, index):
        del self.players[index]
        if len(self.players) == 1:
            return True
        return False
    
    def new_deck(self):
        return shuffle(self.CARDS*self.NUM_SUITS)
    
    def play(self, played_cards):
        '''
        list of payed cards, indices must match corresponding player
        returns (index of winning player, cards won)
        '''
        # get players' cards
        # 

        for card in played_cards:
            if card is None:
                i = played_cards.index(card)
                del played_cards[i]
                self.has_won = self.rem_player(i)


        #check if war occurs
        if all([played_cards[i] != played_cards[(i+1)%len(played_cards)] for i in range(len(played_cards))]):

            same_sets = {}
            for i in range(len(played_cards)):
                if played_cards[i] == played_cards[(i+1)%len(played_cards)]:
                    same_sets[played_cards[i]] = same_sets.get(played_cards[i], set()) + {i, i+1}
            
            for plrs in same_sets.values():
                antes = [[self.players[plyr_i].next() for _ in range(3)] for plyr_i in plrs]
                up_cards = [self.players[plyr_i].next() for plyr_i in plrs]

                winner, oth_antes = self.play(up_cards)

                return winner, [card for ante in antes for card in ante] + played_cards + oth_antes
        else:
            return played_cards.index(max(played_cards)), played_cards
            # self.players[played_cards.index(max(played_cards))].recieves(played_cards)
        return [1,2]

main = Main()

while True:
    played_cards = [plyr.next() for plyr in main.players]

    winner, cards_won = main.play(played_cards)

    main.players[winner].recieves(cards_won)

    if main.has_won:
        print(f'winner: player')
        break

# Main().play()