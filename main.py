import discord
from discord.ext import commands

TOKEN = 'ODAxMjMyNTU5NDE3MDY1NTAy.YAdr-A.qN1UqomZacUGcdYV-dqQws8s3vo'
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
	await ctx.send("world")

@bot.command()
async def add(ctx, left : int, right : int):
	"""Adds two numbers together."""
	await ctx.send(left + right)

bot.run(TOKEN)
