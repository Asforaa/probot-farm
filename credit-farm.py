import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time
import random
import string
from datetime import datetime


#متمسحش العلامتين دول  ''
token = input("Token : ")

#حط هنا بريفيكس البوت و بردو متمسحش نفس العلامتين الي فوق
botprefix = input('prefix : ')

bot = commands.Bot(command_prefix=botprefix)
bot = discord.client
Clientdiscord = discord.Client()

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(f'Credit farm by Asforaa'))
    print(f'{client.user} البوت اونلاين ( ͡° ͜ʖ ͡°)')

def randomthings(stringLength=1):
        lettersAndDigits = string.ascii_uppercase
        return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

@bot.command()
async def spam(ctx):
    spamm=1
    content=randomthings
    await ctx.send('> Spam : **ON**')
    while spamm > 0:
        await ctx.send(content)

@bot.command()
async def stop(ctx):
    spamm=0
    await ctx.send('> Spam : **OFF**')

@client.command()
async def say(ctx, *, msg):
    await ctx.send(msg)

client.run(token, bot=False)
