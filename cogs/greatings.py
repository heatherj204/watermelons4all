import discord
from discord.ext import commands


class Greatings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # hello command
    @commands.command(name='hello', aliases=['hi'])
    async def hello_msg_cmd(self, ctx):
        embed = discord.Embed(
            title='Hello there',
            description=f'Hello there {ctx.author.mention}',
            colour=discord.Color.dark_blue()
            )
        embed.set_author(name=ctx.bot.user.name, icon_url=ctx.bot.user.avatar)
        await ctx.send(embed=embed)



async def setup(bot):
    await bot.add_cog(Greatings(bot))