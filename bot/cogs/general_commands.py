import discord # type: ignore
from discord.ext import commands # type: ignore
from discord import app_commands # type: ignore

class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(
        name="ping",
        description="check if the server is up",
    )
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("Pong!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(GeneralCommands(bot))

async def teardown(bot):
    await bot.remove_cog("GeneralCommands")