import discord
from discord import app_commands, Interaction, User
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.db
    @app_commands.command(name="profile", description="Узнать информацию о себе.")
    async def profile(self, interaction: Interaction):
        embed = discord.Embed(
            title="Профиль",
            description=f"Информация о пользователе {interaction.user.name}",
            color=discord.Color.blurple()
        )
        penalty_points = self.db.get_workers(interaction.user.id)
        embed.add_field(name="Штрафы:", value=str(penalty_points), inline=False)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(General(bot))