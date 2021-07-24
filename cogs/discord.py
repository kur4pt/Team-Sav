import discord 
from discord.ext import commands
import random
import datetime
from discord.ext.commands.core import command



class Discord(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases  =['av'])
    async def avatar(self, ctx, *, member: discord.Member= None, color : discord.Color = None):
        if not member:
            member = ctx.author
        embed = discord.Embed(color = color or random.randint(0, 0xFFFFFF))
        embed.add_field(name  = f'{ctx.author}', value = '**Avatar**')
        embed.set_image(url = member.avatar_url)
        await ctx.send(embed = embed)


    @commands.command(aliases = ['icon', 'sa'])
    async def servericon(self, ctx):
        if not ctx.guild.icon:
            return await ctx.send('This Server Does Not Have A Avatar...')
        embed  = discord.Embed(color = discord.Color.greyple())
        embed.add_field(name  = f'{ctx.guild.name}', value = '**Avatar**')
        embed.set_image(url = ctx.guild.icon_url)
        await ctx.send(embed=embed)
        

    @commands.command(aliases = ['banner', 'sb'])
    async def serverbanner(self, ctx, color: discord.Color = None):
        if not ctx.guild.banner:
            return await ctx.send('This server does have a banner set...')
        embed = discord.Embed(color = color or random.randint(0, 0xFFFFFF))
        embed.add_field(name = f'{ctx.guild.name}', value = '**Banner**')
        embed.set_image(url = ctx.guild.banner_url)
        await ctx.send(embed = embed)


    @commands.command()
    async def serverinfo(self, ctx):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)

        role_count = len(ctx.guild.roles)
        list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]

        #  owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)

        icon = str(ctx.guild.icon_url)
        
        embed = discord.Embed(
            title=name + " Server Information",
        #      description=description,
            color=discord.Color.blue()
            )
        embed.set_thumbnail(url=icon)
        embed.add_field(name='Name', value=f"{ctx.guild.name}", inline=False)
        embed.add_field(name='Number of roles', value=str(role_count), inline=False)
        embed.add_field(name='Number Of Members', value=ctx.guild.member_count, inline=False)
        embed.add_field(name='Bots:', value=(', '.join(list_of_bots)))
        embed.add_field(name='Created At', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
        embed.add_field(name="Owner", value = f"{str(ctx.guild.owner)}", inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)

        await ctx.send(embed=embed)
    

    @commands.command(pass_context = True)
    async def poopcount(self,ctx):
        server = ctx.message.guild
        online = 0
        for i in server.members:
            if str(i.status) == 'online' or str(i.status) == 'idle' or str(i.status) == 'dnd':
                online += 1
        all_users = []
        for user in server.members:
            all_users.append('{}#{}'.format(user.name, user.discriminator))
        all_users.sort()
        all = '\n'.join(all_users)

        embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Colour.blue())
        embed.add_field(name = 'Members' , value = server.member_count , inline = True)

        await ctx.send(embed=embed)



    @commands.command(aliases=["whois"])
    async def userinfo(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author  # set member as the author
        roles = [role for role in member.roles]

        embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

        embed.set_author(name=member)

        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Name:", value=member.display_name)

        embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
        embed.add_field(name="Highest role:", value=member.top_role.mention)

        embed.add_field(name="Accout Made:", value=member.created_at.strftime("%a, %Y %B %#d, %I:%M %p"))
        embed.add_field(name="Joined:", value=member.joined_at.strftime("%a, %Y %B %#d, %I:%M %p"))

        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def nick(self, ctx, user: discord.Member, *, nickname: str = None):
        if not user:  # if member is no mentioned
            user = ctx.message.author 
            
        prevnick = user.nick or user.name
        await user.edit(nick=nickname)
        newnick = nickname or user.name
        await ctx.send(f"Changed {prevnick}'s nickname to {newnick}")


    @nick.error
    async def nick_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Member not found")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You Do Not Have the Required Permissons') 


    @commands.Cog.listener()
    async def on_ready(self):
        print('Discord Cog Ready!')


def setup(client):
    client.add_cog(Discord(client))