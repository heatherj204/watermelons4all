import discord, datetime, json, os, asyncio
from discord.ext import commands, tasks
from random import choice
from itertools import cycle

# adds all server ID's along with the current prefix
def get_server_prefix(bot, message):
    with open("prefixes.json", "r") as f:
        prefix = json.load(f)

    return prefix[str(message.guild.id)]

# gives back the prefix for the server it is called in
def call_prefix(server_id):
    with open("prefixes.json", "r") as f:
        prefixs = json.load(f)

    return prefixs[str(server_id)]

#import bot token
from botstuff import *

intents = discord.Intents.all()
intents.message_content = True
intents.members = True

bot = commands.Bot(intents=intents, command_prefix=get_server_prefix, case_insensitive=True)

bot_statuses = cycle(["Looking for watermelons", "Found a watermelon", "Enjoying some watermelon", "Thinking about watermelons", "I <3 watermelons", "Watermelon for life!"])

@tasks.loop(seconds=30)
async def change_bot_status():
    await bot.change_presence(activity=discord.Game(next(bot_statuses)))

''' Slash Commands '''
@bot.tree.command(name="mannu", description="Mannu is a good boy")
async def slash_command(interaction:discord.Interaction):
    await interaction.response.send_message("Hello World!")

# slash command for getting the current prefix
@bot.tree.command(name="get_prefix", description="Hmm what is the prefix again??")
async def slash_command_prefix(interaction:discord.Interaction):
    await interaction.response.send_message(f"The prefix for all commands is: {call_prefix(interaction.guild.id)} ")

# slash command for getting all the commands
@bot.tree.command(name="commands_list", description="A list of all the commands")
async def slash_command_command_list(interaction:discord.Interaction):
    commandslst = "```"
    for bot_command in interaction.client.commands:
        commandslst+=f"{call_prefix(interaction.guild.id)}{bot_command}\n"
    commandslst+= "```"
    await interaction.response.send_message(commandslst)


''' Event Commands'''
# on ready event
@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Bot is ready")
    change_bot_status.start()

# set defaily prefix on join
@bot.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefix = json.load(f)
    prefix[str(guild.id)] = "$"

    with open("prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)

# remove the prefix from json file when bot is removed form server
@bot.event
async def on_guild_remove(guild):
    with open("prefixes.json", "r") as f:
        prefix = json.load(f)
    prefix.pop(str(guild.id))

    with open("prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    line = f'{message.guild}, {message.channel}: {message.author} wrote: {message.content}'
    print(line)

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

asyncio.run(load())
bot.run(token)
