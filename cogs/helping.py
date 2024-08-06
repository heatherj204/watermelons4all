import discord
from discord.ext import commands


class Helping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help_msg', aliases=['helpme', 'sendhelp', 'helppls'])
    async def help_msg_cmd(self, ctx):
        embed = discord.Embed(
            title="Help??, No help yourself NERD!!! xoxo",
            colour=discord.Color.blue()
            )
        embed.set_footer(text=ctx.bot.user.name, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Helping(bot))