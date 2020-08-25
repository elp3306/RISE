import discord
import os
from discord.ext import commands
import asyncio
from random import *
whiteList = ['bmp','jpeg','jpg','png']
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
     print(bot.user.id)
     print('ready')
     game = discord.Game("개발자 노트")
     await bot.change_presence(status=discord.Status.online, activity=game)

     i = randint(1, 5)
     print(i)





@bot.command()
async def DM(ctx, user: discord.User, *, message=None):
    message = message or "This Message is sent via DM"
    await user.send(message)
    print('보냄')

@bot.event
async def on_message(message):


     if message.author.id!=bot.user.id and message.channel.type is discord.ChannelType.private and message.author.name!='_Hi':

        embed = discord.Embed(title=message.author.name , description=message.author.mention,color=discord.Colour.blue())
        if message.attachments :
            embed.add_field(name='내용', value=message.content+message.attachments[0].url, inline=True)
        else:
            embed.add_field(name='내용', value=message.content, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        #await bot.get_channel(int(699662084321050634)).send(message.author.name + ': ' + message.content)
        await bot.get_user(int(714101459397902418)).send(embed=embed)
        # await bot.get_channel(int(699662084321050634)).send(message.author.name + ': ' + message.content)


     if message.content.startswith('.사진'):
         pic = message.content.split(" ")[1]
         await message.channel.send(file=discord.File(pic))
     await bot.process_commands(message)




access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
