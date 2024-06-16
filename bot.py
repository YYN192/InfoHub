import discord
from discord.ext import commands
import os
from config import TOKEN

# Define the intents
intents = discord.Intents.default()
intents.message_content = True  # Enable the intent to read message content

# Initialize the bot with a command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Load cogs
async def load_cogs():
    cogs = ['cogs.news', 'cogs.weather', 'cogs.crypto', 'cogs.stock', 'cogs.help']
    for cog in cogs:
        await bot.load_extension(cog)

# Start the bot
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Run the bot with the asynchronous cog loading
async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

# Execute the main function
import asyncio
asyncio.run(main())
