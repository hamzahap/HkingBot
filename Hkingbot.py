import os
import random

import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'vibecat' in message.content.lower() or 'catvibe' in message.content.lower() or 'vibe' in message.content.lower():
        await message.channel.send(file=discord.File('catvibe.gif'))
    if 'kermit' in message.content.lower() or 'kys' in message.content.lower():
        await message.channel.send(file=discord.File('kermit.gif'))
    if 'ettu' in message.content.lower():
        await message.channel.send(file=discord.File('ettu.gif'))

client.run(os.environ['DISCORD_TOKEN'])