import os
import random
import giphy_client
import discord
from discord.ext import commands
import urllib
import json

VIBE_IMAGE = "https://s3.gifyu.com/images/catvibe.gif"
VIBIER_IMAGE = "https://s3.gifyu.com/images/ezgif.com-gif-maker-174e18faa852a3028.gif"
VIBIEST_IMAGE = "https://s3.gifyu.com/images/ezgif.com-gif-maker-2664260aedaea9638.gif"

client = commands.Bot(command_prefix="!")

@client.command()
async def vibe(ctx, vibelevel : int = 1):
    if vibelevel == 1:
        await ctx.send(VIBE_IMAGE)
    elif vibelevel == 2:
        await ctx.send(VIBIER_IMAGE)
    else:
        await ctx.send(VIBIEST_IMAGE)

@client.command()
async def kys(ctx):
    await ctx.send(file=discord.File('kermit.gif'))

@client.command()
async def ettu(ctx):
    await ctx.send(file=discord.File('ettu.gif'))

@client.command()
async def gif(ctx, *, q):
    giphykey = os.getenv("GIPHY_KEY")
    url = "http://api.giphy.com/v1/gifs/search"
    params = urllib.parse.urlencode({
        "q": q,
        "api_key": giphykey,
        "limit": "25"
    })
    with urllib.request.urlopen(url.join(params)) as response:
        data = json.loads(response.read())
    list1 = list(data)
    giff = random.choice(list1)

    await ctx.channel.send(giff)

client.run(os.environ['DISCORD_TOKEN'])