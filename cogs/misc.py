import discord
from discord.ext import commands
import json
import os
import typing
import random
import asyncio


snipe_message_author = {}
snipe_message_content = {}

class Misc(commands.Cog):

    def __init__(self, client):

        self.client = client





    @commands.command(pass_context=True, aliases=['stream', 'watching', 'listening'])
    @commands.has_permissions(administrator=True)
    async def game(self, ctx, *, game: str = None):
        
        with open('data/prefixes.json', 'r') as f:
            data = json.loads(f.read())
            guildID = str(ctx.guild.id)
            bot_PREFIX = data[guildID]

        """Set game/stream. Ex: [p]game napping [p]help game for more info

`        Your game/stream status will not show `for yourself, only other people can see it. This is a limitation of how the client works and how the api interacts with the client.

        --Setting playing/watching/listening--
        Set a game: [p]game <text>
        Set watching: [p]watching <text>
        Set listening: [p]listening <text>
        To set a rotating game status, do [p]game game1 | game2 | game3 | etc.
        It will then prompt you with an interval in seconds to wait before changing the game and after that the order in which to change (in order or random)
        Ex: [p]game with matches | sleeping | watching anime

        --Setting stream--
        Same as above but you also need a link to the stream. (must be a valid link to a stream or else the status will not show as streaming).
        Add the link like so: <words>=<link>
        Ex: [p]stream Underwatch=https://www.twitch.tv/a_seagull
        or [p]stream Some moba=https://www.twitch.tv/doublelift | Underwatch=https://www.twitch.tv/a_seagull"""
        is_stream = False
        if ctx.invoked_with == "game":
            message = "Playing"
            self.client.status_type = discord.ActivityType.playing
        elif ctx.invoked_with == "stream":
            is_stream = True
            self.client.status_type = discord.ActivityType.streaming
            self.client.is_stream = True
        elif ctx.invoked_with == "watching":
            message = "Watching"
            self.client.status_type = discord.ActivityType.watching
        elif ctx.invoked_with == "listening":
            message = "Listening to"
            self.client.status_type = discord.ActivityType.listening
        if game:
            # Cycle games if more than one game is given.
            if ' | ' in game:
                await ctx.send(bot_PREFIX + 'Input interval in seconds to wait before changing (``n`` to cancel):')

                def check(msg):
                    return (msg.content.isdigit() or msg.content.lower().strip() == 'n') and msg.author == self.client.user

                def check2(msg):
                    return (msg.content == 'random' or msg.content.lower().strip() == 'r' or msg.content.lower().strip() == 'order' or msg.content.lower().strip() == 'o') and msg.author == self.client.user

                reply = await self.client.wait_for("message", check=check)
                if not reply:
                    return
                if reply.content.lower().strip() == 'n':
                    return await ctx.send(bot_PREFIX + 'Cancelled')
                elif reply.content.strip().isdigit():
                    interval = int(reply.content.strip())
                    if interval >= 5:
                        self.client.game_interval = interval
                        games = game.split(' | ')
                        if len(games) != 2:
                            await ctx.send(bot_PREFIX + 'Change in order or randomly? Input ``o`` for order or ``r`` for random:')
                            s = await self.client.wait_for("message", check=check2)
                            if not s:
                                return
                            if s.content.strip() == 'r' or s.content.strip() == 'random':
                                await ctx.send(bot_PREFIX + '{status} set. {status} will randomly change every ``{time}`` seconds'.format(
                                                                status=message, time=reply.content.strip()))
                                loop_type = 'random'
                            else:
                                loop_type = 'ordered'
                        else:
                            loop_type = 'ordered'

                        if loop_type == 'ordered':
                            await ctx.send(bot_PREFIX + '{status} set. {status} will change every ``{time}`` seconds'.format(
                                                            status=message, time=reply.content.strip()))

                        stream = 'yes' if is_stream else 'no'
                        games = {'games': game.split(' | '), 'interval': interval, 'type': loop_type, 'stream': stream, 'status': self.client.status_type}
                        with open('data/games.json', 'w') as g:
                            json.dump(games, g, indent=4)

                        self.client.game = game.split(' | ')[0]

                    else:
                        return await ctx.send(bot_PREFIX + 'Cancelled. Interval is too short. Must be at least 10 seconds.')

            # Set game if only one game is given.
            else:
                self.client.game_interval = None
                self.client.game = game
                stream = 'yes' if is_stream else 'no'
                games = {'games': str(self.client.game), 'interval': '0', 'type': 'none', 'stream': stream, 'status': self.client.status_type}
                with open('data/games.json', 'w') as g:
                    json.dump(games, g, indent=4)
                if is_stream and '=' in game:
                    g, url = game.split('=')
                    await ctx.send(bot_PREFIX + 'Stream set as: ``Streaming %s``' % g)
                    await self.client.change_presence(activity=discord.Streaming(name=g, url=url))
                else:
                    embed = discord.Embed( color = discord.Colour.red())
                    embed.add_field(name = 'Presence Set!', value = '**Game Set as:** {} {}'.format(message, game))
                    await ctx.send(embed=embed)
                    #await ctx.send(bot_PREFIX + 'Game set as: ``{} {}``'.format(message, game))
                    await self.client.change_presence(activity=discord.Activity(name=game, type=self.client.status_type))

        # Remove game status.
        else:
            self.client.game_interval = None
            self.client.game = None
            self.client.is_stream = False
            await self.client.change_presence(activity=None)
            await ctx.send(bot_PREFIX + 'Set playing status off')
            if os.path.isfile('data/games.json'):
                os.remove('data/games.json')



    @game.error
    async def game_error(self, ctx, error, color: typing.Optional[discord.Color] = None):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(color = color or random.randint(0, 0xFFFFFF))
            embed.add_field(name = 'Missing Permissions', value = 'You do not have the required permssions!')
            await ctx.send(embed=embed)


    @commands.command(aliases=["em"])
    async def embed(self, ctx, color: typing.Optional[discord.Color] = None, *, text):
        """embed text
        Parameters
        • text - the text to embed
        • color - the color of the embed, a random color is used if left empty
        """
        em = discord.Embed(color=color or random.randint(0, 0xFFFFFF))
        em.description = text
        await ctx.send(embed=em)
        await ctx.message.delete()
    

    @commands.Cog.listener()
    async def on_message_delete(self, message):

        snipe_message_author[message.channel.id] = message.author
        snipe_message_content[message.channel.id] = message.content
        await asyncio.sleep(60)
        del snipe_message_author[message.channel.id]
        del snipe_message_content[message.channel.id]



    @commands.command()
    async def snipe(self, ctx):
        with open("data/logged_message.json", "r") as f:
            open_file = json.load(f)

        if str(ctx.channel.id) not in open_file: 
            no_message_embed = discord.Embed(
                title = "Nothing to snipe.",
                color = discord.Color.red()
            )
            return await ctx.send(embed = no_message_embed)
        user = await self.client.fetch_user(open_file[str(ctx.channel.id)]["author"])
        content = open_file[str(ctx.channel.id)]["message_content"]

        sniped_embed = discord.Embed(
            description = f"{content}",
            color = discord.Color.blue()
        )
        sniped_embed.set_author(name = user, icon_url = str(user.avatar_url))
        await ctx.send(embed = sniped_embed)



    @commands.Cog.listener()
    async def on_ready(self):
        print('Misc Cog Ready!')


def setup(client):
    client.add_cog(Misc(client))