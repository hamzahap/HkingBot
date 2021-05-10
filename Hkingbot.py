import os
import random
import giphy_client
import discord
from giphy_client.rest import ApiException
from discord.ext import commands

client = commands.Bot(command_prefix="$")

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

@client.command()
async def gif(ctx,*,q):
    giphykey = os.getenv("GIPHY_KEY")
    api_instance = giphy_client.DefaultApi()

    try:
        api_response = api_instance.gifs_search_get(giphykey, q, limit, rating='r')
        lst = list(api_response.data)
        giff = random.choice(lst)
        emb = discord.Embed(title=q)
        emb.set_image(url=f'api.giphy.com/v1/gifs/search')

        await ctx.channel.send(embed=emb)

    except ApiException as e:
        print("Error calling API")

client.run(os.environ['DISCORD_TOKEN'])