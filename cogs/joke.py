import discord
from random import choice
from discord.ext import commands


class Joke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # joke command
    @commands.command(name='joke', aliases=['pun', 'telljoke', 'jokes'])
    async def joke_msg_cmd(self, ctx):
        joke_choice = choice(['Did you hear they arrested the devil? Yeah, they got him on possession', 'My IQ test results came back. They were negative', 'What happens to an illegally parked frog? It gets toad away', 'Why arent dogs good dancers? Because they have two left feet', 'A Freudian slip is when you say one thing but mean your mother', 'What do fish say when they hit a concrete wall? Dam', 'If athletes get athletes foot, what do astronauts get? Missile toe'])
        embed = discord.Embed(
            title=f'The joke is:',
            description=f'{joke_choice}',
            colour=discord.Color.red()
            )
        embed.set_author(name=ctx.bot.user.name, icon_url=ctx.bot.user.avatar)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Joke(bot))