#!/usr/bin/env python3

import discord, datetime
from discord.ext import commands
from random import choice
# from datetime import datetime

#import bot token
from botapistuff import *

intents = discord.Intents.all()
intents.message_content = True
intents.members = True

bot = commands.Bot(intents=intents, command_prefix="$", case_insensitive=True)


''' Slash Commands '''

@bot.tree.command(name="mannu",description="Mannu is a good boy")
async def slash_command(interaction:discord.Interaction):
    await interaction.response.send_message("Hello World!")

@bot.tree.command(name="get_prefix",description="Hmm what is the prefix again??")
async def slash_command_prefix(interaction:discord.Interaction):
    await interaction.response.send_message("The prefix for all commands is: $")


''' Event Commands'''

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Bot is ready")

# member joins
# @bot.event
# async def on_member_join(member):
#     channel = bot.get_channel()
#     await channel.send('Hello there!')


''' Prefix commands '''

# hello command
@bot.command(name='hello', aliases=['hi'])
async def hello_msg_cmd(ctx):
    embed = discord.Embed(
        title='Hello there',
        description=f'Hello there {ctx.author.mention}',
        colour=discord.Color.dark_blue()
        )
    embed.set_author(name=ctx.bot.user.name, icon_url=ctx.bot.user.avatar)
    await ctx.send(embed=embed)

# not so helpfull help command
@bot.command(name='help_msg', aliases=['helpme', 'sendhelp', 'helppls'])
async def help_msg_cmd(ctx):
    embed = discord.Embed(
        title="Help??, No help yourself NERD!!! xoxo",
        colour=discord.Color.blue()
        )
#    embed.set_author(name=ctx.bot.user.name, icon_url=ctx.bot.user.avatar)
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

# joke command
@bot.command(name='joke', aliases=['pun', 'telljoke', 'jokes'])
async def joke_msg_cmd(ctx):
    joke_choice = choice(['Did you hear they arrested the devil? Yeah, they got him on possession', 'My IQ test results came back. They were negative', 'What happens to an illegally parked frog? It gets toad away', 'Why arent dogs good dancers? Because they have two left feet', 'A Freudian slip is when you say one thing but mean your mother', 'What do fish say when they hit a concrete wall? Dam', 'If athletes get athletes foot, what do astronauts get? Missile toe'])
    embed = discord.Embed(
        title=f'The joke is:',
        description=f'{joke_choice}',
        colour=discord.Color.red()
        )
    embed.set_author(name=ctx.bot.user.name, icon_url=ctx.bot.user.avatar)
    await ctx.send(embed=embed)

# bot latency cmd
@bot.command(name='ping', aliases=['latency'])
async def ping_cmd(ctx):
    embed = discord.Embed(
        title='Ping',
        description='Latency in ms',
        colour=discord.Color.dark_magenta()
        )
    embed.add_field(name=f"{bot.user.name}'s Latency:", value=f'{round(bot.latency * 1000)}ms.', inline=True)
    embed.set_footer(text=f'Requested by: {ctx.author.name}.', icon_url=ctx.author.avatar)
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

# user profile cmd
@bot.command(name='profile', aliases=['pf'])
async def user_profile_cmd(ctx, user: discord.Member=None):

    if user == None:
        user = ctx.message.author
    inline = True
    embed=discord.Embed(
        title=user.name,
        colour=discord.Color.dark_magenta()
    )
    userData = {
        "mention" : user.mention,
        "Nick" : user.nick,
        "Created at" : user.created_at.strftime("%b %d, %Y, %T"),
        "joined at" : user.joined_at.strftime("%b %d, %Y, %T"),
        "Server" : user.guild,
        "Top role" : user.top_role
    }
    for [fieldName, fieldValue] in userData.items():
        embed.add_field(name=fieldName + ":", value=fieldValue, inline=inline)
    embed.set_footer(text=f'id: {user.id}')

    embed.timestamp = datetime.datetime.utcnow()
#    embed.set_thumbnail(user.display_avatar)
    await ctx.send(embed=embed)

@bot.command(name='server')
async def server_pf_cmd(ctx):
    guild = ctx.message.author.guild
    inline = True
    embed=discord.Embed(
        title=guild.name,
        colour=discord.Color.dark_magenta()
    )
    serverData = {
        "Owner" : guild.owner.mention,
        "Channels" : len(guild.channels),
        "Members" : guild.member_count,
        "Created at" : guild.created_at.strftime("%b %d, %Y, %T"),
        "Description" : guild.description,
    }
    for [fieldName, fieldValue] in serverData.items():
        embed.add_field(name=fieldName + ":", value=fieldValue, inline=inline)
    embed.set_footer(text=f'id: {guild.id}')

#    embed.set_thumbnail(guild.icon)
    embed.timestamp = datetime.datetime.utcnow()
#    embed.set_thumbnail(user.display_avatar)
    await ctx.send(embed=embed)

bot.run(token)