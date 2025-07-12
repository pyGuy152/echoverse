import discord, os
from dotenv import load_dotenv
from utils.llm import askAI

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True  
intents.members = True
intents.presences = True

bot = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(bot)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await tree.sync()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    return

@tree.command(name="ping", description="Test the bot's responsiveness.")
async def ping_slash(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!", ephemeral=True)

@tree.command(name="create_world", description="Create a world for the server!!!")
async def ping_slash(interaction: discord.Interaction, world_name:str, genre:str , description: str = ""):
    creator = str(interaction.user.display_name)
    guild_name = str(interaction.guild.name)
    guild_description = str(interaction.guild.description)
    world_description = askAI(f'''You're helping write a short, casual, and creative description for a world in a Discord server. The world doesnt always have to be fantasy use the genre given.

The tone should feel friendly and imaginative — something you'd hear from a person setting up a cool story or RP world for friends. Keep it simple, easy to read, and fun. Avoid sounding like an AI or using complex words or dramatic clichés.

Here’s the info to base it on:
- World Name: {world_name}
- Genre: {genre}
- Any extra ideas (optional): {description}
- Server name: {guild_name}
- Server description (you can lightly reference it): {guild_description}

The final result should be 5–6 sentences max, and sound natural. Don’t include titles, intros, or lists — just the description. Just describe the world btw dont invite ppl and stuff. USE 3RD PERSON POV.
''')
    await interaction.response.send_message(f"{interaction.user.mention} made a new world named {world_name} with a genre of {genre}. Inital description - \n\n{world_description}")

bot.run(TOKEN)