
class FrenchCard:

    def __init__(self):
        self.suit = ""
        self.rank = ""
        self.value = 0

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, rank):
        self._rank = rank

    def __hash__(self):
        return hash((self.suit, self.rank))

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def output(self):
        if self.rank == '0':
            response = "10 of "
        elif self.rank == 'j':
            response = "Jack of "
        elif self.rank == 'k':
            response = "King of "
        elif self.rank == 'q':
            response = "Queen of "
        elif self.rank == 'a':
            response = "Ace of "
        else:
            response = f"{self.rank} of "

        if self.suit == 's':
            response += '\U00002660'
        elif self.suit == 'c':
            response += '\U00002663'
        elif self.suit == 'h':
            response += '\U00002665'
        else:
            response += '\U00002666'

        return response
