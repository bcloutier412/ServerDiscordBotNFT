import os
import discord
from keep_alive import keep_alive
from discordbot import *

client = discord.Client()
my_secret = os.environ['TOKEN']

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$msgbot'):
    use_bot()
    
keep_alive()
client.run(my_secret)

