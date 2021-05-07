import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    Mudkiproasts = [
        'Mudkip is literally the worst Pokemon',
        'Mudkip needs to have an opinion on everything.' ,
        (
            'Mudkip should stop boasting about his GPA'
            '\nHe really needs help'
        ),
    ]
    Zeshaanroasts = [
        'Zeshaan is still shifting lol',
        'What about Zeshaan? that man can\'t leave Mesaid. It\'s been like 3 months now lol'
    ]

    if 'mudkip' in message.content.lower():
        response = random.choice(Mudkiproasts)
        await message.channel.send(response)
    if 'zeshaan' in message.content.lower() or 'biryani' in message.content.lower():
        response = random.choice(Zeshaanroasts)
        await message.channel.send(response)
client.run(TOKEN)