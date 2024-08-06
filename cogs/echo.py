import discord
from discord.ext import commands


class Echo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # echos command
    @commands.command()
    async def echo(self, ctx, words):
        embed = discord.Embed(
            title=words,
            colour=discord.Color.dark_green()
            )
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed)



async def setup(bot):
    await bot.add_cog(Echo(bot))