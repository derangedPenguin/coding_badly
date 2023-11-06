CONV_RANK = {
    7:'7',
    8:'8',
    9:'9',
    10:'10',
    11:'Jack',
    12:'Queen',
    13:'King',
    14:'Ace'
}

GET_SUIT = {
    'BB':'Spades',
    'BR':'Clubs',
    'RB':'Diamonds',
    'RR':'Hearts'
}

SUIT_COLOR = {
    'Spades': 'B',
    'Clubs': 'B',
    'Diamonds': 'R',
    'Hearts': 'R'
}

# {'rank':rank, 'suit':suit} ex: {'rank':11, 'suit':'Clubs'}
cards = []
five_cards = list(input('Enter Colors: '))

def eval_card():
    rank = 7
    if five_cards[2] == 'B':
        rank += 4
    if five_cards[3] == 'B':
        rank += 2
    if five_cards[4] == 'B':
        rank += 1

    cards.append({'rank':rank, 'suit':GET_SUIT[''.join(five_cards[:2])]})

    #find sixth card and cut top card to bottom
    if cards[-1]['rank'] == 9 or (cards[-1]['rank'] == 8 and (cards[-1]['suit'] in {'Hearts', 'Clubs'})):
        five_cards.append(SUIT_COLOR[cards[-1]['suit']])
    else:
        five_cards.append('B' if SUIT_COLOR[cards[-1]['suit']] == 'R' else 'R')
    
    five_cards.remove(five_cards[0])

for i in range(5):
    eval_card()

for card in cards:
    print(CONV_RANK[card['rank']] + ' of ' + card['suit'])