# Blockchain Charles by Gabriel Tu 

import discord
import asyncio
import random 
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix = '~')


@bot.event 
async def ready():
    print("hello")

#grabs quote from a file
def grab_q():
    q = open("quotes.txt", "r")
    q_len = q.readline()
    ran = random.randint(1,int(q_len))
    quote = q.readline()
    while True:
        ran -=1 
        if(not(ran)): return quote
        else: quote = q.readline()
        

#bot will respond with a quote 
@bot.command(pass_context=True)
async def quote(cfx):
    await bot.say(grab_q())

tok = open("token.txt", "r")
contents = tok.read()

bot.run(contents)