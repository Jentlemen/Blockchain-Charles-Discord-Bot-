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

    
#bot will respond with a math stuff 
@bot.command(pass_context=True)

async def math(cfx, equation):
    await bot.say(eval(equation))
    #await bot.say("Bézout's lemma")

#help command
bot.remove_command('help')
@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Blockchain Charles", description="Im Charles. My commands are:", color=0xff69b4)
    embed.add_field(name="~quote", value="I say one of my infamous quotes", inline=False)
    embed.add_field(name="~math", value="I calculate easy math", inline=False)
    await bot.say(embed=embed)

#read the token from the 
tok = open("token.txt", "r")
contents = tok.read()

bot.run(contents)