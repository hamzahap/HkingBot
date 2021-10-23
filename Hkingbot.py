import os
import random
from discord import message
import giphy_client
import discord
from discord.ext import commands
from giphy_client.rest import ApiException

#from google_images_search import GoogleImagesSearch

VIBE_IMAGE = "https://hamzahap.github.io/VibeGIFS/Vibe.gif"
VIBIER_IMAGE = "https://hamzahap.github.io/VibeGIFS/Vibey.gif"
VIBIEST_IMAGE = "https://hamzahap.github.io/VibeGIFS/Vibey.gif"



client = commands.Bot(command_prefix="!")




@client.event
async def on_reaction_add(reaction, user):
    #await reaction.message.channel.send(reaction.emoji.id)
    if reaction.emoji == '⭐':
        if reaction.count==1:        
            #hannel1 = discord.utils.get(client.get_all_channels(), name='bookmark')
            channel = client.get_channel(878984320130355220)
            embedVar = discord.Embed(title="Original Message",url = reaction.message.jump_url, description = reaction.message.content, color = 0xFFFF00)
            embedVar.set_author(name=reaction.message.author.display_name,icon_url=reaction.message.author.avatar_url)
            embedVar.set_image(reaction.message)
            #await channel1.send(reaction.message.content)
            await channel.send(embed=embedVar)
    
        #await reaction.message.channel.send(reaction.message.content)
    #if 'star' in message.reactions:
        
    #    await message.channel.send('message')



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
async def gif(ctx, *, q="searchterm"):
    if q == "searchterm":
        await ctx.channel.send("Enter a search term noob!")
    else:
        giphykey = os.getenv("GIPHY_KEY")    
        api_instance = giphy_client.DefaultApi()
        api_response = api_instance.gifs_search_get(giphykey, q, limit=25, rating='r')
        list1 = list(api_response.data)
        giff = random.choice(list1)

        await ctx.channel.send(giff.embed_url)

@client.command()
async def megakek(ctx):
    await ctx.channel.send(file=discord.File('megakek.mp3'))

#@client.command()
#async def image(ctx, *, q="searchterm"):
#    if q == "searchterm":
#        await ctx.channel.send("Enter a search term noob!")
#   else:
#       gis = GoogleImagesSearch(os.getenv("GOOGLE_KEY"), os.getenv("GOOGLE_CX"))
#        _search_params = {
#            'q': q,
#            'num': 10,
#           'safe': 'high|medium|off',
#           'fileType': 'jpg|gif|png',
#            'imgType': 'clipart|face|lineart|news|photo',
#            'imgSize': 'huge|icon|large|medium|small|xlarge|xxlarge',
#            'imgDominantColor': 'black|blue|brown|gray|green|pink|purple|teal|white|yellow',
#            'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived'
#        }
        
#        list2 = list(gis.search(search_params=_search_params))
#        images = random.choice(list2)
#        await ctx.channel.send(images)


client.run(os.environ['DISCORD_TOKEN'])