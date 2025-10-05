import discord
from discord import app_commands, Interaction, User
from discord.ext import commands

class Manage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.db

    @app_commands.command(name="start_work", description="Используй чтобы начать работу.")
    async def ping(self, interaction: Interaction):
        embed = discord.Embed(
            title="Example",
            description="TEst",
            color=discord.Color.blurple()
        )
        embed.add_field(name="Name", value="Some value", inline=False)

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Manage(bot))