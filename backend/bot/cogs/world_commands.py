import discord # type: ignore
from utils.llm import askAI
from discord.ext import commands # type: ignore
from discord import app_commands # type: ignore

class WorldCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="create_world",
        description="Create a world for the server!!!"
    )
    @app_commands.describe(
        world_name="The name of your new world",
        world_genre="The genre of the world",
        world_inspiration="Something to base your world off of"
    )
    @app_commands.checks.has_permissions(
        administrator=True
    )
    async def create_world(self, interaction: discord.Interaction, world_name:str, world_genre:str , world_inspiration: str = ""):
        creator = str(interaction.user.display_name)
        guild_name = str(interaction.guild.name)
        guild_description = str(interaction.guild.description)
        description = askAI(f'''You're helping write a short, casual, and creative description for a world in a Discord server. The world doesnt always have to be fantasy use the genre given.

    The tone should feel friendly and imaginative — something you'd hear from a person setting up a cool story or RP world for friends. Keep it simple, easy to read, and fun. Avoid sounding like an AI or using complex words or dramatic clichés.

    Here's the info to base it on:
    - World Name: {world_name}
    - Genre: {world_genre}
    - Any extra ideas (optional): {world_inspiration}
    - Server name: {guild_name}
    - Server description (you can lightly reference it): {guild_description}

    The final result should be 5-6 sentences max, and sound natural. Don't include titles, intros, or lists — just the description. Just describe the world btw dont invite ppl and stuff. USE 3RD PERSON POV.
    ''')
        await interaction.response.send_message(f"{interaction.user.mention} made a new world named {world_name} with a genre of {world_genre}. Inital description - \n\n{description}")

async def setup(bot):
    await bot.add_cog(WorldCommands(bot))

async def teardown(bot):
    await bot.remove_cog("WorldCommands")