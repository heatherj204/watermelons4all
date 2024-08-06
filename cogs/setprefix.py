import discord, json
from discord.ext import commands


class Setprefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setprefix(self, ctx, *, newprefix: str):
        with open("./prefixes.json", "r") as f:
            prefix = json.load(f)
        prefix[str(ctx.guild.id)] = newprefix

        with open("./prefixes.json", "w") as f:
            json.dump(prefix, f, indent=4)

        embed = discord.Embed(
            title=f'Prefix changed to {newprefix}',
            description=f'Prefix for all {ctx.bot.user.name} commands is now: {newprefix} thanks to: {ctx.author.mention}',
            colour=discord.Color.dark_blue()
            )
        embed.set_author(name=ctx.bot.user.name, icon_url=ctx.bot.user.avatar)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Setprefix(bot))