import sqlaccess
import random
import datetime
import games


class CommandInterpreter:

    def __init__(self):
        self.storage = sqlaccess.Storage()
        self.games = games.Games()

    async def create_new_player(self, message):
        if self.storage.create_new_player(message.author):
            response = f"Player {message.author} has been created"
        else:
            response = f"Player {message.author} already exists"

        await message.channel.send(response)

    async def process(self, message):
        botcmd = message.content[1:].lower().split(" ")
        cmd = botcmd[0]

        if cmd == "profile" or cmd == "me":
            await message.channel.send(self.output_profile(message))

        elif cmd == "new":
            await self.create_new_player(message)

        elif cmd == "flip":
            await self.games.flip(message, botcmd)

        elif cmd == "highcard":
            await self.games.high_card(message, botcmd)

    def output_profile(self, message):
        name = message.author
        results = self.storage.get_player_record(name)[0]

        if results is not None:
            currency = results[1]
            created = results[2]
            played = results[3]
            return f"Name: {message.author.mention}\nCurrency: {currency}\nCreated: {created}\nLast Played: {played}\n"
        else:
            return f"Player {message.author.mention} does not exist. Type $new to create a new account"
