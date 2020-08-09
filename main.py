import discord
import commandinterpreter
import logging

logging.basicConfig(format='%(asctime)s-%(process)d-%(levelname)s-%(message)s', filename='jbot1.log',
                    filemode='w', level=logging.DEBUG)

client = discord.Client()
command = commandinterpreter.CommandInterpreter()
bot_prefix = '$'
bot_token = 'ENTER YOUR DISCORD BOT TOKEN HERE'


@client.event
async def on_ready():
    logging.info(f"We have logged in as '{client.user}'")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content[0] == bot_prefix:
        await command.process(message)


client.run(bot_token)
