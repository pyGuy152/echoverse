import discord, os # type: ignore
from discord.ext import commands # type: ignore
from dotenv import load_dotenv # type: ignore
from database.schemas import setup_tables

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def load_cogs():
    """
    Loads all cogs from the 'cogs' directory.
    """
    for filename in os.listdir("./bot/cogs"):
        if filename.endswith(".py"):
            cog_name = filename[:-3]
            if cog_name == "__init__":
                continue
            try:
                await bot.load_extension(f"bot.cogs.{cog_name}")
                print(f"Loaded cog: {cog_name}")
            except Exception as e:
                print(f"Failed to load cog {cog_name}: {e}")

async def unload_cogs():
    """
    Unloads all currently loaded cogs.
    """
    for cog_name in list(bot.extensions.keys()):
        try:
            await bot.unload_extension(cog_name)
            print(f"Unloaded cog: {cog_name}")
        except Exception as e:
            print(f"Failed to unload cog {cog_name}: {e}")




@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    setup_tables()
    print("DB set up")
    await load_cogs()
    await bot.tree.sync()
    print("Bot is ready")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    return

# @tree.command(name="ping", description="Test the bot's responsiveness.")
# async def ping_slash(interaction: discord.Interaction):
#     await interaction.response.send_message("Pong!", ephemeral=True)

bot.run(TOKEN)