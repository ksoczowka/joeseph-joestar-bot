import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

token = open('token.txt').read()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if str(message.channel) == 'joseph-joestar':
        if message.content.startswith('Czy '):
            choice = ['Tak', 'Nie']
            await message.channel.send(random.choice(choice))
        if message.content.startswith('TT'):
            await message.channel.send(str(message.channel) + ' - ' + str(message.channel.id))
client.run(token)
