import discord
from discord.ext import commands
from dotenv import load_dotenv
from utils.database import Database
import os
import sys
load_dotenv()

token = os.getenv("TOKEN")
class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        self.db = Database()
        super().__init__(command_prefix=commands.when_mentioned_or("!"), intents = intents)

    async def setup_hook(self):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py') and not filename.startswith('_'):
                try:
                    await self.load_extension(f'cogs.{filename[:-3]}')
                    print(f'Loaded extension: {filename}')
                except Exception as e:
                    print(f'Failed to load extension {filename}.', e)
                    sys.exit()

        await self.tree.sync()
        print('Slash commands synced.')

bot = Bot()

bot.run(token)