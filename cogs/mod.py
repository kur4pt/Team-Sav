import discord 
from discord.ext import commands
import typing
import random

from discord.ext.commands.errors import BadArgument


class Mod(commands.Cog):

    def __init__(self, client):
        self.client = client



    @commands.command(aliases = ['clear'])
    async def purge(self, ctx, amount = 1000, color: typing.Optional[discord.Colour] = None):
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(color = color or random.randint(9, 0xFFFFFF))
        embed.add_field(name = 'Messages Cleared!', value = f'**{amount}** messages have been cleared!')
        embed.set_footer(text= f'Purge Made by {ctx.author}')
        await ctx.send(embed = embed)


    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specify the amount of messages you would like to clear.')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You Do Not Have the Required Permissons')        



#Kick commands
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason = "No reason given!", color: typing.Optional[discord.Color] = None):
        await member.kick(reason=reason)
        embed=discord.Embed(color=color or random.randint(0, 0xFFFFFF))
        embed.add_field(name='Member Kick!', value = f'**{member}** has been kicked by **{ctx.message.author}**')
        await ctx.send(embed=embed)



    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Member not found")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please Mention a Member!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You Do Not Have the Required Permissons') 



    #Ban Commands
    @commands.command(pass_context=True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason = 'No reason given', color : typing.Optional[discord.Color]= None):
        await member.ban(reason = reason)
        embed = discord.Embed(coloe=color or random.randint(0, 0xFFFFFF))
        embed.add_field(name='Member Banned!', value = f'**{member}** has been banned by **{ctx.message.author}** \nReason : {reason}')
        await ctx.send(embed=embed)


    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Member not found")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please Mention a Member!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You Do Not Have the Required Permissons') 


    @commands.command(description="Mutes the specified user.")
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        embed = discord.Embed(title="Member Muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
        await ctx.send(embed=embed)
        await member.add_roles(mutedRole, reason=reason)
        await member.send(f" You have been muted from: **{guild.name}** \nReason: {reason}")


    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Member not found")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please Mention a Member!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You Do Not Have the Required Permissons') 


    @commands.command(description="Unmutes a specified user.")
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        await member.remove_roles(mutedRole)
        await member.send(f" you have unmutedd from: **{ctx.guild.name}**")
        embed = discord.Embed(title="unmute", description=f"**{member.mention}** has been unmuted!",colour=discord.Colour.light_gray())
        await ctx.send(embed=embed)


    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Member not found")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please Mention a Member!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You Do Not Have the Required Permissons') 


    @commands.Cog.listener()
    async def on_ready(self):
        print('Mod Cog is ready!')

def setup(client):
    client.add_cog(Mod(client))

