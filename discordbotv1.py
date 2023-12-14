# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run("MTE4NDYyMjE0MjA2Nzg0NzIzOA.GmBMsw.sV8RsgwnX3dFeboO-O4HmRnJOVkQEgQ7V9uw5w")