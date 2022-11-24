import os
import json
import sys

from discord.ext import commands, tasks
from discord.ext.commands import Bot, Context
import discord

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)

intents = discord.Intents.all()
client = commands.Bot(intents=intents, command_prefix=">")

@client.event
async def on_ready():
    print("----------------------")
    print("Logged In As")
    print("Username: %s"%client.user.name)
    print("ID: %s"%client.user.id)
    print("----------------------")

@client.command()
async def hello(ctx):
    username = str(ctx.author).split('#')[0]
    await ctx.send(username)

client.run(config["token"])