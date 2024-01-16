import discord
from discord.ext import commands

import random

#connect other project files
import database, chatGPT

intents = discord.Intents.default()
intents.message_content = True

token = open('token.txt').read()

bot = commands.Bot(intents=intents)

@bot.slash_command()
async def channel_info(ctx):
    channel = ctx.channel.name
    channel_id = ctx.channel.id
    await ctx.respond(str(channel) + ' - ' + str(channel_id))

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if str(message.channel) == 'joseph-joestar':
        if message.content.startswith('Czy '):
            await message.channel.send(random.choice(['Tak', 'Nie']))

bot.run(token)
