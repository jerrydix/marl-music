import discord
from discord.ext import commands
import os
from bot import config

config.load()

bot = commands.Bot(command_prefix=config.DISCORD_COMMAND_PREFIX, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="music"))
    await bot.load_extension('cogs.music')



# @bot.event
# async def on_message(message):
    # if message.content.startswith(config.DISCORD_COMMAND_PREFIX + 'echo') and message.content[5] == ' ':
        # msg = message.content[5:]
        # await message.channel.send(msg)
        

bot.run(config.DISCORD_API_TOKEN)