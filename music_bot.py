import discord
from discord.ext import commands
import os
from bot import config

config.load()

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=config.DISCORD_COMMAND_PREFIX, intents=discord.Intents.all())
        
    async def on_ready(self):
        print(f'We have logged in as {bot.user}')
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="music"))
        synced = await self.tree.sync()
        print(f"Synced {len(synced)} command(s)")
        
    async def setup_hook(self):
        await self.load_extension('cogs.music')
        
bot = Client()

bot.run(config.DISCORD_API_TOKEN)