import discord 
from discord.ext import commands


TOKEN = 'NTI0MzYxMzY1NDY1NTk1OTI0.Dvm98Q.gpbHFeDoYzEhkuwAIUwCWAC1cv4'

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Yeet its working')

@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))
    await client.process_commands(message)

@client.command()
async def ping():
    await client.say("Pong!")

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

client.run(TOKEN)