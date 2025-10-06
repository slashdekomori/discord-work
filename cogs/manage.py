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
            title="Работа начата!",
            description=f"- Работник: {interaction.user.mention}",
            color=discord.Color.blurple()
        )
        embed.add_field(name="Name", value="Some value", inline=False)

        view = discord.ui.View()
        button = discord.ui.Button(label="Закончить работу", style=discord.ButtonStyle.primary)

        async def button_callback(btn_inter: Interaction):
            button.disable = True

            new_embed = discord.Embed(
                title="Работа окончена",
                description="Ты закончил раобту!",
                color=discord.Color.green()
            )

            await btn_inter.response.defer()
            await btn_inter.edit_original_response(embed=new_embed, view=None)
        button.callback = button_callback
        view.add_item(button)

        await interaction.response.send_message(embed=embed, view=view)


async def setup(bot):
    await bot.add_cog(Manage(bot))