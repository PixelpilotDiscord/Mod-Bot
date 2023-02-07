import os
import discord
from discord.ext import commands
from flask import Flask
app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'

app.run(host='0.0.0.0', port=8080)

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='For Help use !help'))

@bot.command()
async def greet(ctx):
    await ctx.send(f'Hello, {ctx.author.name}!')

@bot.command()
async def echo(ctx, *, message: str):
    await ctx.send(message)

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, user: discord.Member, *, reason: str):
    await ctx.send(f'{user.name} has been warned for {reason}')

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason: str):
    await user.ban(reason=reason)
    await ctx.send(f'{user.name} has been banned for {reason}')

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason: str):
    await user.kick(reason=reason)
    await ctx.send(f'{user.name} has been kicked for {reason}')

my_secret = os.environ['TOKEN']
bot.run(my_secret)
