import os
import json
import sys

from discord.ext import commands, tasks
from discord.ext.commands import Bot, Context

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)

client = commands.Bot(command_prefix = config["command_prefix"])

@client.event
async def on_ready():
    print("----------------------")
    print("Logged In As")
    print("Username: %s"%client.user.name)
    print("ID: %s"%client.user.id)
    print("----------------------")

client.run(config["token"])