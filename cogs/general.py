import discord
from discord import app_commands, Interaction, User
from discord.ext import commands

devs = [749001740170559570,456802396874735616,1218993322442490036,1108543819370205255]

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
        query = await self.db.get_workers(str(interaction.user.id))
        embed.add_field(name="Штрафы:", value=int(query[1]), inline=False)
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="give_penalty", description="Информация о боте.")
    @app_commands.describe(user="Пользователь, которому хотите выдать штраф.")
    async def give_penalty(self, interaction: Interaction, user: User):
        if interaction.user.id not in devs:
            await interaction.response.send_message("У вас нет прав на использование этой команды.", ephemeral=True)
            return
        await self.db.give_penalty(str(user.id))
        await interaction.response.send_message(f"Штраф выдан пользователю {user.mention}.")
        

async def setup(bot):
    await bot.add_cog(General(bot))