import discord, datetime
from discord.ext import commands

class Profiles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # user profile cmd
    @commands.command(name='profile', aliases=['pf'])
    async def user_profile_cmd(self, ctx, user: discord.Member=None):

        if user == None:
            user = ctx.message.author
        inline = True
        embed=discord.Embed(
            title=user.name,
            colour=discord.Color.dark_magenta()
        )
        userData = {
            "Mention" : user.mention,
            "Nick" : user.nick,
            "Created at" : user.created_at.strftime("%b %d, %Y, %T"),
            "Joined at" : user.joined_at.strftime("%b %d, %Y, %T"),
            "Server" : user.guild,
            "Top role" : user.top_role
        }
        for [fieldName, fieldValue] in userData.items():
            embed.add_field(name=fieldName + ":", value=fieldValue, inline=inline)
        embed.set_footer(text=f'id: {user.id}')

        embed.timestamp = datetime.datetime.utcnow()
        embed.set_thumbnail(url=user.avatar)
        await ctx.send(embed=embed)

    # server profile cmd
    @commands.command(name='server')
    async def server_pf_cmd(self, ctx):
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

        embed.set_thumbnail(url=guild.icon)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Profiles(bot))