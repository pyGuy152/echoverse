import discord, os
from dotenv import load_dotenv

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
    await message.channel.send(f'Hi {message.author.mention}!')

@tree.command(name="ping", description="Test the bot's responsiveness.")
async def ping_slash(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!", ephemeral=True)


bot.run(TOKEN)