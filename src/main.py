import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Nigerundayou!')
    if message.content.startswith('Czy '):
        await message.channel.send(random.choice(['Tak', 'Nie']))
        print(message.channel)
client.run('MTE5NjExOTQzNjU1NDQyNDM3MQ.GbwUrv.NeR6AvmFd5PygSWxonsU_Bc5xkLHJT9xbB9c1o')
