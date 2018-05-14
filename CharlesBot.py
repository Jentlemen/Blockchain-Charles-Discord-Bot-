# Blockchain Charles by Gabriel Tu 
import discord
import asyncio
import random 
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix = '~')


tok = open("token.txt", "r")
contents = tok.read()

bot.run(contents)