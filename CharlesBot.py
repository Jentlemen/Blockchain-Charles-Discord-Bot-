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

@bot.command(pass_context=True)
async def help(cfx):
    await bot.say("help - placeholder")

#grabs a rand quote from a file
#first line of quotes.txt must be # of quotes in the file
def grab_q():
    q = open("quotes.txt", "r")
    q_len = q.readline() #grab num from line 0 
    ran = random.randint(1,int(q_len)) # make rand# from 1-q_len
    quote = q.readline()
    #grab the quote from line ran
    while True:
        ran -=1 
        if(not(ran)): return quote
        else: quote = q.readline()
        

#bot will respond with a quote 
@bot.command(pass_context=True)
async def quote(cfx):
    await bot.say(grab_q())

#read the token from the 
tok = open("token.txt", "r")
contents = tok.read()

bot.run(contents)