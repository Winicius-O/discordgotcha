from discord.ext import commands, tasks
import asyncio
import os


client = commands.Bot(command_prefix = "_")

@client.event
async def on_ready():
    print("user ON")

@tasks.loop(minutes=30.0)
async def sender(startingUp=True):
    if startingUp:
        await asyncio.sleep(5)
        startingUp = False

    channel = client.get_channel(658202312862334976)
    await channel.send("$p")

sender.start()
client.run(os.environ.get("USER_TOKEN"), bot=False)