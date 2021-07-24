import discord, os
from sys import prefix
import json
from discord import embeds
from discord.colour import Color
from discord.ext import commands
from discord.ext.commands.core import has_permissions
from discord.flags import Intents
from keep_alive import keep_alive


intents = discord.Intents.default()

intents.members = True


def get_prefix(client, message):
    with open('data/prefixes.json', 'r') as f:
        prefix = json.load(f)

    return prefix[str(message.guild.id)]



client = commands.Bot(command_prefix=get_prefix, intents = intents)
client.remove_command('help')

#https://discord.com/api/oauth2/authorize?client_id=868297953998151751&permissions=8&scope=bot


for file_name in os.listdir("./cogs"):
    if file_name.endswith(".py"): 
        client.load_extension(f"cogs.{file_name[:-3]}")


@client.event
async def on_ready():
    """Bot startup"""
    print("Logged in!")
    await client.change_presence(status=discord.Status.online, afk=True)


@client.event
async def on_guild_join(guild):
    with open('data/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '?'

    with open('data/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4)


@client.event
async def on_guild_remove(guild):
    with open('data/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('data/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4)


@client.command(aliases = ['sp'])
@has_permissions(administrator=True)
async def setprefix(ctx, prefix):
    with open('data/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix 

    with open('data/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4)

    embed = discord.Embed(color = discord.Colour.greyple())
    embed.add_field(name = "Changed Prefix!", value = f'Prefix has been changed to: {prefix}')

    embed.set_footer(text = f'Use {prefix} before every command!')
    await ctx.send(embed=embed)


@client.command(aliases = ['gp', 'GP', 'Getprefix'])
async def getprefix(ctx):
    with open("data/prefixes.json", "r") as f:
        data = json.loads(f.read())
        guildID = str(ctx.guild.id)
        prefix = data[guildID]
        await ctx.send(f"Prefix: {prefix}")


@client.command()
async def membercount(ctx):
    embed=discord.Embed(timestamp = ctx.message.created_at, color = discord.Colour.blue())
    embed.add_field(name = "Membercount", value = ctx.guild.member_count)

    await ctx.send(embed=embed)

@client.command()
async def test(ctx):
    await ctx.send('Bruh deadass testing this, your mad lame :moyai:')



@client.group(invoke_without_command=True)
async def help(ctx):

    with open("data/prefixes.json", "r") as f:
        data = json.loads(f.read())
        guildID = str(ctx.guild.id)
        prefix = data[guildID]

    embed = discord.Embed(title = "Devial Commands", color = discord.Colour.dark_blue())

    embed.add_field(name = f"***{prefix}help fun***", value="Fun Commands To Use!", inline = True)
    embed.add_field(name = f"***{prefix}help mod***", value="Commands Mods Can Use!", inline = False)
    embed.add_field(name = f"***{prefix}help info***", value="Useful Commands To USe!", inline = False)
    embed.add_field(name = f'***{prefix}help setup***', value="Customize Certain Commands!", inline = False)

 
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=f"{ctx.guild} Make Sure to use {prefix} before every command!", icon_url=ctx.guild.icon_url)

    await ctx.send(embed=embed)


@help.command()
async def fun(ctx):
    with open("data/prefixes.json", "r") as f:
        data = json.loads(f.read())
        guildID = str(ctx.guild.id)
        prefix = data[guildID]


    embed = discord.Embed(title =f"**{ctx.guild}** Fun Commands!", color = discord.Colour.blurple())
    embed.add_field(name = f'{prefix}8ball', value  = 'Ask it a question! \nHas About 15 Random Answers!', inline = True)
    embed.add_field(name = f'{prefix}chances', value = f'Gives the member its chances of joining **{ctx.guild}**!', inline= True)
    embed.add_field(name = f'{prefix}ping', value = 'Gives the Bots Latency!', inline = True)
    embed.add_field(name = f'{prefix}coinflip', value = 'Flip a Coin and Get Heads or Tails!', inline = True)
    embed.add_field(name = f'{prefix}f', value = 'F to Pay Respect', inline  = True)
    embed.add_field(name = f'{prefix}rate', value = 'Rate Anyone in The Server!', inline = True)
    embed.add_field(name = f'{prefix}reverse', value = 'Everything You Type After Reverse Will of Course, be Reversed!', inline = True)


    embed.set_footer(text=f'Make sure to use {prefix} before every command!', icon_url=ctx.guild.icon_url)
    await ctx.send(embed = embed)


@help.command()
async def mod(ctx):
    with open("data/prefixes.json", "r") as f:
        data  = json.loads(f.read())
        guildID = str(ctx.guild.id)
        prefix = data[guildID]


    embed = discord.Embed(title = f'{ctx.guild} Mod Commands!', color = discord.Color.dark_purple())
    embed.add_field(name = f'{prefix}mute', value = 'Basic Mute Command!', inline = True)
    embed.add_field(name = f'{prefix}unmute', value = 'Basic Unmute Command!', inline = True)
    embed.add_field(name = f'{prefix}kick', value = 'Basic Kick Command!', inline = True)
    embed.add_field(name = f'{prefix}ban',value = 'Basic Ban Command!', inline = True)
    embed.add_field(name = f'{prefix}purge', value  = 'Clear as Mainy Message as You Want! (Max is 1000)', inline = True)


    embed.set_footer(text = f'Make sure to use {prefix} before every command!', icon_url = ctx.guild.icon_url)
    await ctx.send(embed = embed)



@help.command()
async def info(ctx):
    with open('data/prefixes.json', "r") as f:
        data = json.loads(f.read())
        guildID = str(ctx.guild.id)
        prefix = data[guildID]

    embed = discord.Embed(title = f'{ctx.guild} Discord Commands!', color = discord.Color.purple())
    embed.add_field(name = f'{prefix}avatar', value = 'Get A Members Avatar!', inline = True)
    embed.add_field(name = f'{prefix}servericon', value = 'Get The Servers Icon!', inline = True)
    embed.add_field(name = f'{prefix}serverbanner', value = 'Get The Server Banner!', inline  = True)
    embed.add_field(name = f'{prefix}userinfo', value = 'Get Info on a Member!', inline = True)
    embed.add_field(name = f'{prefix}serverinfo', value = f'Get Info on {ctx.guild.name}')
    embed.add_field(name = f'{prefix}membercount', value = f'Get The Amount Of members in {ctx.guild.name}')

    embed.set_footer(text = f'Make Sure to use {prefix} before every command!', icon_url = ctx.guild.icon_url)
    await ctx.send(embed = embed)
    


@help.command()
async def setup(ctx):
    with open('data/prefixes.json', "r") as f:
        data = json.loads(f.read())
        guildID = str(ctx.guild.id)
        prefix = data[guildID]

    embed = discord.Embed(title = f'{ctx.guild} Setup Commands!', color = discord.Color.dark_teal())
    embed.add_field(name = f'{prefix}setinsta', value  = 'Set The Team\'s Instagram!', inline = True)
    embed.add_field(name = f'{prefix}setyoutube', value  = 'Set The Team\'s Youtube!', inline = True)
    embed.add_field(name = f'{prefix}settwitter', value = 'Set The Team\'s Twitter!', inline = True)
    embed.add_field(name = f'{prefix}setTiktok', value = 'Set The Team\'s Tiktok', inline  = True)
    embed.add_field(name = f'{prefix}setprefix', value = 'Set The Bot\'s Prefix!')

    embed.set_footer(text = f'Make sure you have Admin permissions to set the commands!',
     icon_url = ctx.guild.icon_url)

    await ctx.send(embed = embed)


keep_alive()
client.run('Your-Token-Here')
