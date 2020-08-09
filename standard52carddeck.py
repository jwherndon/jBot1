import frenchcard


class Standard52CardDeck:

    def __init__(self):
        self.suits = ['s', 'c', 'h', 'd']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '0', 'j', 'q', 'k', 'a']
        self.deck = self.create_deck()

    def create_deck(self):
        deck = []
        for suit in self.suits:
            for rank in self.ranks:
                new_card = frenchcard.FrenchCard()
                new_card.suit = suit
                new_card.rank = rank
                new_card.value = self.ranks.index(rank)
                deck.append(new_card)

        return deck

    def remove_card(self, card):
        # card_hash = card.__hash__()
        if card in self.deck:
            self.deck.remove(card)
