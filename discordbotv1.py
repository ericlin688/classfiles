# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run("key")
