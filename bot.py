import discord

from discord.ext import commands

client = commands.Bot(  command_prefix = ';')
#Префикс

@client.event

async def on_ready():
	print('BOT CONECTED')
	
@client.command( pass_context = True)

async def hello(ctx):
	await ctx.send( 'Hello')
	
@client.command(pass_context = True)

async def clear(ctx, amount = 100):
	await ctx.channel.purge( limit = amount)
	await ctx.send( 'Было очищено' amount 'Сообщений')

#connect

token = open('token.txt', 'r').readline()

client.run( token )