import discord
from discord import app_commands, Interaction, User
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.db
# баловался 
    @app_commands.command(name="ping", description="Zdarova pasiki")
    async def ping(self, interaction: Interaction):
        await interaction.response.send_message("Здарова пасики!")

async def setup(bot):
    await bot.add_cog(General(bot))