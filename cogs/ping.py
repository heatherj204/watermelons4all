import discord, datetime
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # bot latency cmd
    @commands.command(name='ping', aliases=['latency'])
    async def ping_cmd(self, ctx):
        embed = discord.Embed(
            title='Ping',
            description='Latency in ms',
            colour=discord.Color.dark_magenta()
            )
        embed.add_field(name=f"{self.bot.user.name}'s Latency:", value=f'{round(self.bot.latency * 1000)}ms.', inline=True)
        embed.set_footer(text=f'Requested by: {ctx.author.name}.', icon_url=ctx.author.avatar)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Ping(bot))
