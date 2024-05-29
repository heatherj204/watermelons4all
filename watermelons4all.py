
import discord, datetime, json, os, asyncio
from discord.ext import commands
from random import choice
# import json
# import os
# import asyncio

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


''' Slash Commands '''
@bot.tree.command(name="mannu", description="Mannu is a good boy")
async def slash_command(interaction:discord.Interaction):
    await interaction.response.send_message("Hello World!")

# slash command for getting the current prefix
@bot.tree.command(name="get_prefix", description="Hmm what is the prefix again??")
async def slash_command_prefix(interaction:discord.Interaction):
    await interaction.response.send_message(f"The prefix for all commands is: {call_prefix(interaction.guild.id)} ")


''' Event Commands'''
# on ready event
@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Bot is ready")

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
    # with open("watermelons4all\chatlog.txt", "w") as f:
    #         f.write (f'{line}\n')
    print(line)


''' Prefix commands '''

@bot.command()
async def setprefix(ctx, *, newprefix: str):
    with open("prefixes.json", "r") as f:
        prefix = json.load(f)
    prefix[str(ctx.guild.id)] = newprefix

    with open("prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)

    embed = discord.Embed(
        title=f'Prefix changed to {newprefix}',
        description=f'Prefix for all {ctx.bot.user.name} commands is now: {newprefix} thanks to: {ctx.author.mention}',
        colour=discord.Color.dark_blue()
        )
    embed.set_author(name=ctx.bot.user.name, icon_url=ctx.bot.user.avatar)
    await ctx.send(embed=embed)

# # hello command
# @bot.command(name='hello', aliases=['hi'])
# async def hello_msg_cmd(ctx):
#     embed = discord.Embed(
#         title='Hello there',
#         description=f'Hello there {ctx.author.mention}',
#         colour=discord.Color.dark_blue()
#         )
#     embed.set_author(name=ctx.bot.user.name, icon_url=ctx.bot.user.avatar)
#     await ctx.send(embed=embed)

# not so helpfull help command
@bot.command(name='help_msg', aliases=['helpme', 'sendhelp', 'helppls'])
async def help_msg_cmd(ctx):
    embed = discord.Embed(
        title="Help??, No help yourself NERD!!! xoxo",
        colour=discord.Color.blue()
        )
    embed.set_footer(text=ctx.bot.user.name, icon_url=ctx.author.avatar)
    await ctx.send(embed=embed)

# echos command
@bot.command()
async def echo(ctx, words):
    embed = discord.Embed(
        title=words,
        colour=discord.Color.dark_green()
        )
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
    await ctx.send(embed=embed)


async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

asyncio.run(load())
bot.run(token)
