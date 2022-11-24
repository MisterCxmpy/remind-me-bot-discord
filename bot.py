import os
import json
import sys
from datetime import datetime, timezone, timedelta

from discord.ext import commands, tasks
from discord.ext.commands import Bot, Context
import discord

year = 365
month = 30

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
async def remind(ctx, time, time_period):

    user = await client.fetch_user(ctx.author.id)

    if time_period not in ["seconds", "minutes", "hours", "days", "weeks", "months", "years"]:
        return

    current_time = datetime.now(timezone.utc)

    if time_period == "seconds":
        time_change = timedelta(seconds=int(time))
    elif time_period == "minutes":
        time_change = timedelta(minutes=int(time))
    elif time_period == "hours":
        time_change = timedelta(hours=int(time))
    elif time_period == "days":
        time_change = timedelta(days=int(time))
    elif time_period == "weeks":
        time_change = timedelta(weeks=int(time))
    elif time_period == "months":
        time_change = timedelta(days=(month * int(time)))
    elif time_period == "years":
        time_change = timedelta(days=(year * int(time)))
    else:
        return
    
    remind_time = current_time + time_change

    message = f"{user.mention} Messaging you on " + str(remind_time)[:19] + " UTC to remind you of this comment."

    await ctx.channel.send(message)

client.run(config["token"])