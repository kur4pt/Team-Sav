import discord
from discord.ext import commands
import json

class Gram(commands.Cog):

    def __init__(self, client):
        
        self.client = client





    def get_insta(client, message):
        with open('data/insta.json', 'r') as f:
            insta = json.load(f)

        return insta[str(message.guild.id)]

    def get_twitter(client, message):
        with open('data/twit.json', 'r') as f:
            twit = json.load(f)

        return twit[str(message.guild.id)]

    def get_youtube(client, message):
        with open('data/yt.json', 'r') as f:
            yt = json.load(f)

        return yt[str(message.guild.id)]

    def get_tiktok(client, message):
        with open('data/TikTok.json', 'r') as f:
            tik = json.load(f)

        return tik[str(message.guild.id)]





#Tiktok command
    @commands.Cog.listener()
    async def on_guild_join(guild):
        with open('data/TikTok.json', 'r') as f:
            tiktok = json.load(f)

        tiktok[str(guild.id)] = 'No Tiktok Set'

        with open('data/TikTok.json', 'w') as f:
            json.dump(tiktok, f, indent = 4)


    @commands.Cog.listener()
    async def on_guild_remove(guild):
        with open('data/TikTok.json', 'r') as f:
            tiktok = json.load(f)

        tiktok.pop(str(guild.id))

        with open('data/TikTok.json', 'w') as f:
            json.dump(tiktok, f, indent = 4)


    @commands.command(aliases = ['stt', 'settioktok'])
    @commands.has_permissions(administrator = True)
    async def setTiktok(self, ctx, tik):
        with open('data/TikTok.json', 'r') as f:
            tiktok = json.load(f)

        tiktok[str(ctx.guild.id)] = tik

        with open('data/TikTok.json', 'w') as f:
            json.dump(tiktok, f, indent = 4)

        embed = discord.Embed(color = discord.Colour.greyple())
        embed.add_field(name = "TikTOk Set!", value = f'TikTok set to: {tik}')

        await ctx.send(embed=embed)


    @commands.command()
    async def tiktok(self, ctx):
        with open('data/TikTok.json', "r") as f:
            data = json.loads(f.read())
            guildID = str(ctx.guild.id)
            tik = data[guildID]

        embed = discord.Embed(coloor = discord.Colour.magenta())

        embed.add_field(name  = "Team TikTok", value = f'Make Sure to follow our TikTok! \n{tik}')
        embed.set_footer(icon_url=ctx.guild.icon_url)
        await ctx.send(embed = embed)


    @setTiktok.error
    async def setTiktok_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please Insert a Link!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You Do Not Have the Required Permissons') 




#youtube commmand 
    @commands.Cog.listener()
    async def on_guild_join(guild):
        with open('data/yt.json', 'r') as f:
            youtube = json.load(f)

        youtube[str(guild.id)] = 'No twiter Set'

        with open('data/yt.json', 'w') as f:
            json.dump(youtube, f, indent = 4)


    @commands.Cog.listener()
    async def on_guild_remove(guild):
        with open('data/yt.json', 'r') as f:
            youtube = json.load(f)

        youtube.pop(str(guild.id))

        with open('data/yt.json', 'w') as f:
            json.dump(youtube, f, indent = 4)


    @commands.command(aliases = ['syt'])
    @commands.has_permissions(administrator = True)
    async def setyoutube(self, ctx, yt):
        with open('data/yt.json', 'r') as f:
            youtube = json.load(f)

        youtube[str(ctx.guild.id)] = yt

        with open('data/yt.json', 'w') as f:
            json.dump(youtube, f, indent = 4)

        embed = discord.Embed(color = discord.Colour.greyple())
        embed.add_field(name = "Youtube Set!", value = f'Youtube set to: {yt}')

        await ctx.send(embed=embed)


    @commands.command(aliases = ['yt'])
    async def youtube(self, ctx):
        with open("data/yt.json", "r") as f:
            data = json.loads(f.read())
            guildID = str(ctx.guild.id)
            yt = data[guildID]

        embed = discord.Embed(coloor = discord.Colour.magenta())

        embed.add_field(name  = "Team Youtube", value = f'Make Sure you sub to our YouTube! \n{yt}')
        embed.set_footer(icon_url=ctx.guild.icon_url)
        await ctx.send(embed = embed)


    @setyoutube.error
    async def setyoutube_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please Insert a Link!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You Do Not Have the Required Permissons') 




    #twitter command
    @commands.Cog.listener()
    async def on_guild_join(guild):
        with open('data/twit.json', 'r') as f:
            twitter = json.load(f)

        twitter[str(guild.id)] = 'No twiter Set'

        with open('data/twit.json', 'w') as f:
            json.dump(twitter, f, indent = 4)


    @commands.Cog.listener()
    async def on_guild_remove(guild):
        with open('data/twit.json', 'r') as f:
            twitter = json.load(f)

        twitter.pop(str(guild.id))

        with open('data/insta.json', 'w') as f:
            json.dump(twitter, f, indent = 4)


    @commands.command(aliases = ['st'])
    @commands.has_permissions(administrator = True)
    async def settwitter(self, ctx, twit):
        with open('data/twit.json', 'r') as f:
            twitter = json.load(f)

        twitter[str(ctx.guild.id)] = twit

        with open('data/twit.json', 'w') as f:
            json.dump(twitter, f, indent = 4)

        embed = discord.Embed(color = discord.Colour.greyple())
        embed.add_field(name = "Twitter Set!", value = f'Twitter set to: {twit}')

        await ctx.send(embed=embed)


    @commands.command()
    async def twitter(self, ctx):
        with open("data/twit.json", "r") as f:
            data = json.loads(f.read())
            guildID = str(ctx.guild.id)
            twit = data[guildID]

        embed = discord.Embed(coloor = discord.Colour.magenta())

        embed.add_field(name  = "Team Twitter", value = f'Make Sure to follow our Twitter! \n{twit}')
        embed.set_footer(icon_url=ctx.guild.icon_url)
        await ctx.send(embed = embed)


    @settwitter.error
    async def settwitter_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please Insert a Link!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You Do Not Have the Required Permissons') 



    #Instagram command
    @commands.Cog.listener()
    async def on_guild_join(guild):
        with open('data/insta.json', 'r') as f:
            instagram = json.load(f)

        instagram[str(guild.id)] = 'No Insta Set'

        with open('data/insta.json', 'w') as f:
            json.dump(instagram, f, indent = 4)


    @commands.Cog.listener()
    async def on_guild_remove(guild):
        with open('data/insta.json', 'r') as f:
            instagram = json.load(f)

        instagram.pop(str(guild.id))

        with open('data/insta.json', 'w') as f:
            json.dump(instagram, f, indent = 4)


    @commands.command(aliases = ['si'])
    @commands.has_permissions(administrator = True)
    async def setinsta(self, ctx,insta):
        with open('data/insta.json', 'r') as f:
            instagram = json.load(f)

        instagram[str(ctx.guild.id)] = insta 

        with open('data/insta.json', 'w') as f:
            json.dump(instagram, f, indent = 4)

        embed = discord.Embed(color = discord.Colour.greyple())
        embed.add_field(name = "Instagram Set!", value = f'Team Instagram set to: {insta}')

        await ctx.send(embed=embed)


    @commands.command()
    async def insta(self, ctx):
        with open("data/insta.json", "r") as f:
            data = json.loads(f.read())
            guildID = str(ctx.guild.id)
            insta = data[guildID]

        embed = discord.Embed(coloor = discord.Colour.magenta())

        embed.add_field(name  = "Team Insta", value = f'Make Sure to follow our instagram! \n{insta}')
        embed.set_footer(icon_url=ctx.guild.icon_url)
        await ctx.send(embed = embed)


    @setinsta.error
    async def setinsta_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please Insert a Link!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You Do Not Have the Required Permissons') 





#Social command
    @commands.command()
    async def socials(self, ctx):
        guildID = str(ctx.guild.id)
        with open('data/twit.json', 'r') as f:
            twit = json.load(f)[guildID]
        with open('data/insta.json', 'r') as f:
            insta = json.load(f)[guildID]
        with open('data/yt.json', 'r') as f:
            yt = json.load(f)[guildID]
        with open('data/TikTok.json', 'r') as f:
            tik = json.load(f)[guildID]

        embed = discord.Embed(title = 'Socials', color = discord.Colour.blue())

        embed.add_field(name = 'Team Youtube', value = f'Subscribe to Our Youtube! \n{yt} ', inline = False)
        embed.add_field(name = 'Team Instagram', value = f'Follow Our Instagram! \n{insta}', inline = False)
        embed.add_field(name = 'Team Twitter', value = f'Follow Our Twitter! \n{twit}', inline  = False)
        embed.add_field(name = 'Team TikTok', value = f'Follow our TikTok! \n{tik}', inline = False)


        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(icon_url=ctx.guild.icon_url)

        await ctx.send(embed=embed)

        

    @commands.Cog.listener()
    async def on_ready(self):
        print('Socials Cog is Ready')

def setup(client):
    client.add_cog(Gram(client))
