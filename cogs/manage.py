import discord
from discord import app_commands, Interaction, User
from discord.ext import commands

# для парсинга времени 
import humanfriendly


class Manage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.db

    @app_commands.command(name="start_work", description="Используй чтобы начать работу.")
    async def start_work(self, interaction: Interaction):
        embed = discord.Embed(
            title="Работа начата!",
            description=f"- Работник: {interaction.user.mention}",
            color=discord.Color.blurple()
        )
        embed.add_field(name="Name", value="Some value", inline=False)

        view = discord.ui.View()
        button = discord.ui.Button(label="Закончить работу", style=discord.ButtonStyle.primary)

        async def button_callback(btn_inter: Interaction):
            if btn_inter.user.id != interaction.user.id:
                await btn_inter.response.send_message(
                    "Эта кнопка не для тебя", ephemeral=True
                )
                return

            button.disabled = True 
            new_embed = discord.Embed(
                title="Работа окончена",
                description="Ты закончил работу!",
                color=discord.Color.green()
            )
            await btn_inter.response.edit_message(embed=new_embed, view=None) 

        button.callback = button_callback
        view.add_item(button)

        await interaction.response.send_message(embed=embed, view=view)

    @app_commands.command(name="break", description="Используй чтобы взять перерыв.")
    async def ping(self, interaction: Interaction, time: str):
        parsed = humanfriendly.parse_timespan(time)

        embed = discord.Embed(
            title="Перерыв.",
            description=f"{interaction.user.mention} взял перерыв на {parsed} s"
            color=discord.Color.yellow()
        )

        await interaction.response.send_message(embed=embed)
 
async def setup(bot):
    await bot.add_cog(Manage(bot))