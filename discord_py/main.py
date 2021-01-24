import discord
from discord.ext import commands
import configparser
from time import gmtime, strftime
import os

#startup sequence
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("---------------------")
#print("|2021-01-24 22:11:56|"
print("|"+strftime("%Y-%m-%d %H:%M:%S",gmtime())+"|")
print("---------------------")
dir = os.path.dirname(__file__)
print(dir)
config = configparser.ConfigParser()
config.read(os.path.join(dir,'config/config.ini'))
TOKEN = config['Discord']['token']
description = '''test bot'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')

@bot.command()
async def hello(ctx):
	"""Says world"""
	print("hello received")
	await ctx.send("world")

@bot.command()
async def add(ctx, left : int, right : int):
	"""Adds two numbers together."""
	print(left + " + " + right)
	await ctx.send(left + right)

bot.run(TOKEN)
