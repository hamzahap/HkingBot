import os

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
        'Do you have to have an opinion on everything?' ,
        (
            'Stop boasting about your GPA, we know you are smart'
            'You really need help'
        ),
    ]

    if message.content == 'Mudkip':
        response = random.choice(Mudkiproasts)
        await message.channel.send(response)
client.run(TOKEN)