import discord
from discord import embeds
from discord.embeds import Embed
from discord.ext import commands
import random
import asyncio


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
        determine_flip = [1,0]

    @commands.command(aliases = ['cf'])
    async def coinflip(self, ctx, color: discord.Color = None):
        coinsides = ['Heads', 'Tails']
        embed = discord.Embed(color = color or random.randint(0, 0xFFFFFF))
        embed.add_field(name = 'Coin Flipped!', value = f'{ctx.author.mention} flipped a coin and got **{random.choice(coinsides)}**!')
        await ctx.send(embed= embed)


    @commands.command()
    async def f(self, ctx, *, text: commands.clean_content = None):
        hearts = ["❤", "💛", "💚", "💙", "💜"]
        reason = f"For **{text}** " if text else""
        await ctx.send(f"**{ctx.author.name}** has paid their respect {reason}{random.choice(hearts)}")


    @commands.command(aliases = ['rv'])
    async def reverse(self, ctx, *, text: str):
        """ !poow ,ffuts esreveR
        Everything you type after reverse will of course, be reversed
        """
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        await ctx.send(f"🔁 {t_rev}")


    @commands.command()
    async def rate(self, ctx, *, member: discord.Member = None):
        if not member:
            member = ctx.author
        """ Rates what you desire """
        rate_amount = random.uniform(0.0, 100.0)
        await ctx.send(f"I'd rate **{member.mention}** a **{round(rate_amount, 2)} / 100**")


    @commands.command()
    async def beer(self, ctx, user: discord.Member = None, *, reason: commands.clean_content = ""):
        """ Give someone a beer! 🍻 """
        if not user or user.id == ctx.author.id:
            return await ctx.send(f"**{ctx.author.name}**: paaaarty!🎉🍺")
        if user.id == self.bot.user.id:
            return await ctx.send("*drinks beer with you* 🍻")
        if user.bot:
            return await ctx.send(f"I would love to give beer to the bot **{ctx.author.name}**, but I don't think it will respond to you :/")
        beer_offer = f"**{user.name}**, you got a 🍺 offer from **{ctx.author.name}**"
        beer_offer = beer_offer + f"\n\n**Reason:** {reason}" if reason else beer_offer
        msg = await ctx.send(beer_offer)
        def reaction_check(m):
            if m.message_id == msg.id and m.user_id == user.id and str(m.emoji) == "🍻":
                return True
            return False

        try:
            await msg.add_reaction("🍻")
            await self.bot.wait_for("raw_reaction_add", timeout=30.0, check=reaction_check)
            await msg.edit(content=f"**{user.name}** and **{ctx.author.name}** are enjoying a lovely beer together 🍻")
        except asyncio.TimeoutError:
            await msg.delete()
            await ctx.send(f"well, doesn't seem like **{user.name}** wanted a beer with you **{ctx.author.name}** ;-;")
        except discord.Forbidden:
            # Yeah so, bot doesn't have reaction permission, drop the "offer" word
            beer_offer = f"**{user.name}**, you got a 🍺 from **{ctx.author.name}**"
            beer_offer = beer_offer + f"\n\n**Reason:** {reason}" if reason else beer_offer
            await msg.edit(content=beer_offer)


    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = [
        discord.Embed(title='It is certain.'),
        discord.Embed(title='It is decidedly so.'),
        discord.Embed(title='Without a doubt.'),
        discord.Embed(title='Yes - definitely.'),
        discord.Embed(title='You may rely on it.'),
        discord.Embed(title='Most likely.'),
        discord.Embed(title='Outlook good.'),
        discord.Embed(title='Yes.'),
        discord.Embed(title='Signs point to yes.'),
        discord.Embed(title='Reply hazy, try again.'),
        discord.Embed(title='Ask again later.'),
        discord.Embed(title='Better not tell you now.'),
        discord.Embed(title='Cannot predict now.'),
        discord.Embed(title='Concentrate and ask again.'),
        discord.Embed(title="Don't count on it."),
        discord.Embed(title='My reply is no.'),
        discord.Embed(title='My sources say no.'),
        discord.Embed(title='Outlook not very good.'),
        discord.Embed(title='Very doubtful.')
            ]
        responses = random.choice(responses)
        await ctx.send(content=f'Question: {question}\nAnswer:', embed=responses)



    @commands.command()
    async def chances(self, ctx):
        Team = str(ctx.guild)    
        responses = [
        discord.Embed(title='1% chance of joining '+ Team +'!'),
        discord.Embed(title='5% chnace of joining '+ Team +'!'),
        discord.Embed(title='12% chance of joining '+ Team +'!'),
        discord.Embed(title='7% chance of joining '+ Team +'!'),
        discord.Embed(title='23% chance of joining '+ Team +'!'),
        discord.Embed(title='21% chance of joining '+ Team +'!'),
        discord.Embed(title='38% chance of joining '+ Team +'!'),
        discord.Embed(title='29% chance of joining '+ Team +'!'),
        discord.Embed(title='42% chance of joining '+ Team +'!'),
        discord.Embed(title='48% chance of joining '+ Team +'!'),
        discord.Embed(title='45% chance of joining '+ Team +'!'),
        discord.Embed(title='50% chance of joining '+ Team +'!'),
        discord.Embed(title='53% chance of joining '+ Team +'!'),
        discord.Embed(title='59% chance of joining '+ Team +'!'),
        discord.Embed(title='60% chance of joining '+ Team +'!'),
        discord.Embed(title='63% chance of joining '+ Team +'!'),
        discord.Embed(title='66% chance of joining '+ Team +'!'),
        discord.Embed(title='***69%*** chance of joining '+ Team +'!'),
        discord.Embed(title='70% chance of joining '+ Team +'!'),
        discord.Embed(title='72% chance of joining '+ Team +'!'),
        discord.Embed(title='76% chance of joining '+ Team +'!'),
        discord.Embed(title='73% chance of joining '+ Team +'!'),
        discord.Embed(title='79% chance of joining '+ Team +'!'),
        discord.Embed(title='80% chance of joining '+ Team +'!'),
        discord.Embed(title='83% chance of joining '+ Team +'!'),
        discord.Embed(title='87% chance of joining '+ Team +'!'),
        discord.Embed(title='94% chance of joining '+ Team +'!'),
        discord.Embed(title='97% chance of joining '+Team+'!'),
        discord.Embed(title='***AIN\'t NO WAY YOU JOINING*** '+ Team +'***!!!***'),
        discord.Embed(title='***SIGN THIS MAN TO ' +Team+ 'RIGHT NOW***')
            ]
        responses = random.choice(responses)
        await ctx.send(embed=responses)



    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun Cog Ready')

def setup(client):
    client.add_cog(Fun(client))