import sqlaccess
import random
import datetime
import standard52carddeck


class Games:

    def __init__(self):
        self.storage = sqlaccess.Storage()

    async def flip(self, message, command):

        if len(command) == 3 and (command[1][0] == 'h' or command[1][0] == 't') \
                and str.isdigit(command[2]):
            faces = ['Heads', 'Tails']
            player_face = faces[0] if command[1][0] == 'h' else faces[1]
            wager = int(command[2])
            name = message.author

            if self.storage.check_player_credit(name, wager):
                response = f"{message.author.mention} has chosen {player_face} and wagered {wager} coins\n"

                self.storage.set_player_last_played(message.author, datetime.datetime.now(tz=datetime.timezone.utc))
                result = random.choice(faces)

                response += '...flipping coin...\n'

                if player_face == result:
                    response += f'{result}! Winner! {message.author.mention} won {wager} coins!'
                    self.storage.add_player_currency(message.author, wager)
                else:
                    response += f'{result}! Loser! {message.author.mention} lost {wager} coins!'
                    self.storage.sub_player_currency(message.author, wager)

            else:
                response = f"{message.author.mention} You do not have enough coins to make that wager"
        else:
            response = f"{message.author.mention} Please enter $flip < heads | tails > < wager >\n" \
                       "Example: $flip heads 20"

        await message.channel.send(response)

    async def high_card(self, message, command):
        high_card_deck = standard52carddeck.Standard52CardDeck()
        response = ""

        if len(command) == 2 and str.isdigit(command[1]):
            wager = int(command[1])
            name = message.author
            player_card = None
            dealer_card = None

            if self.storage.check_player_credit(name, wager):
                dealer_card = random.choice(high_card_deck.deck)
                high_card_deck.remove_card(dealer_card)
                player_card = random.choice(high_card_deck.deck)
                response = f"{message.author.mention} turns over {player_card.output()}\n" \
                           + f"Dealer turns over {dealer_card.output()}\n"
                if dealer_card > player_card:
                    response += f"Dealer wins!  You lost {wager} coins!"
                    self.storage.sub_player_currency(name, wager)
                elif dealer_card < player_card:
                    response += f"{message.author.mention} wins!  You won {wager} coins!"
                    self.storage.add_player_currency(name, wager)
                else:
                    response += f"PUSH! No one wins."

            else:
                response = f"{message.author.mention} You do not have enough coins to make that wager"

        else:
            response = f"{message.author.mention} Please enter $highcard < wager >\n" \
                       "Example: $highcard 20"

        await message.channel.send(response)
