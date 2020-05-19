
from discord.ext import commands
import discord
import Prefix
import json


class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        show_avatar = discord.Embed(
            title=f'{member}',
            colour=discord.Colour.blue()
        
        )
        show_avatar.set_image(url='{}' .format(member.avatar_url))
        await ctx.send(embed=show_avatar)

    @commands.command(name="poll", description="Make a poll")
    async def poll(self, ctx, *, args= None):
      prefix = Prefix.getprefix(ctx.guild)
      if args == None:
        embed = discord.Embed(title="Help for {}embed".format(prefix), color=blue)
        embed.add_field(name="Arguments", value= "{}poll [poll question]".format(prefix))
        await ctx.send(embed=embed)
      else:
          embed = discord.Embed(color=discord.Colour.blue())
          embed.add_field(name="Poll from {}".format(ctx.author), value= args)
          reactthis = await ctx.send(embed=embed)
          await reactthis.add_reaction("\U0001F44D")
          await reactthis.add_reaction("\U0001F44E")
          await ctx.message.delete()



    @commands.command(name="prefix", description="Set, fetch and reset prefixes")
    async def prefix(self, ctx, what = None, set= None):
        try:
            with open('prefixes.json') as f:
                prefixes = json.load(f)
                srvr = prefixes[str(server.id)]
        except:
            theprefix = "-"
            srvr = theprefix
        embed = discord.Embed(title=f"Help for {Prefix.getprefix(ctx.guild)}prefix", color=0xFF8700)
        embed.add_field(name="Command help:", value='Please use one of these arguments', inline=False)
        embed.add_field(name="Usage:", value=f"{Prefix.getprefix(ctx.guild)}prefix set [prefix]\n{Prefix.getprefix(ctx.guild)}prefix fetch\n{Prefix.getprefix(ctx.guild)}prefix reset", inline=False)
        if what == None:
            await ctx.send(embed=embed)
        elif what == 'set':
            if ctx.message.author.guild_permissions.manage_guild:
                with open('prefixes.json') as f:
                    prefixes = json.load(f)
                prefixes[str(ctx.guild.id)] = set
                with open('prefixes.json', 'w') as f:
                    json.dump(prefixes, f, indent=4)
                await ctx.send("> The prefix for **" + ctx.guild.name + "** has been set to **" + set + "**")
            else:
                await ctx.send("Go get some perms and try again.")
        elif what == 'fetch':
            await ctx.send('The prefix for **{}** is **{}**'.format(ctx.guild.name, Prefix.getprefix(ctx.guild)))
        elif what == 'reset':
            if ctx.message.author.guild_permissions.manage_guild:
                with open('prefixes.json') as f:
                    prefixes = json.load(f)
                prefixes[str(ctx.guild.id)] = "-"
                with open('prefixes.json', 'w') as f:
                    json.dump(prefixes, f, indent=4)
                await ctx.send('The prefix for **{}** has been reset to **{}**'.format(ctx.guild.name, set))
            else:
                await ctx.send("Go get some perms and try again.")
        else:
            await ctx.send(embed=embed)



    @commands.command()
    async def coronacount(self, ctx):
        await ctx.send('https://www.worldometers.info/coronavirus/')


    @commands.command()
    async def issue(self, ctx):
        embed=discord.Embed(
        title='If you have any issues, run this command',
        description=f'{Prefix.getprefix(ctx.guild)}report <issue>'
        )
        embed.add_field(name='Or Join and Report in', value='[This server](https://discord.gg/4dYzmYS)')
        await ctx.send(embed=embed)


    @commands.command(aliases=['author'])
    async def creator(self, ctx):
        embed=discord.Embed(
        title='Creator',
        description='Suteki#3477',
        colour=discord.Colour.blue()


        )

        embed.set_image(url="https://images-ext-1.discordapp.net/external/FR-mA0PVavjPibdTQNwr-UECIu93_Bcxxy8pj4zMU1Y/https/images-ext-2.discordapp.net/external/ZIeUgIKSBKeH9HLuziNvR4KG-NB8e_pI1ev7ccUMgQI/https/media.discordapp.net/attachments/696121556119715890/703691658797252657/image0.png?width=971&height=546")
        embed.add_field(name='Youtube', value="[Click Here!](https://www.youtube.com/channel/UCUlVOye5aOCp7eqhkQAXZhg)")
        embed.add_field(name='Created on', value='Python 3.8. Script written on Visual Studio Code')
        embed.add_field(name='Suteki Reddit', value='[Click here!](https://www.reddit.com/user/Watashi-sugoi)')
        embed.add_field(name='Support Server', value='[Click Here!](https://discord.gg/MddDvR7)')
        embed.add_field(name='Name meaning', value='Suteki means "Fantastic" in Japanese')
        embed.add_field(name='Someone who helped me a ton making this bot', value='Coolo2 #5499 (try command `-coolo2`)')
        await ctx.send(embed=embed)

    @commands.command(aliases=['userinfo'])
    async def whois(self, ctx, member : discord.Member=None):
      if member == None:
        await ctx.send(f'Whos information do you want to see?\n\nCommand Usage:\n`{Prefix.getprefix(ctx.guild)}userinfo <member>`')
      else:
        embed=discord.Embed(
        colour=discord.Colour.blue()
        )
        embed.set_author(name=f'User Info for {member}')
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f'Requested by {ctx.author}')

        embed.add_field(name='ID', value=member.id)
        embed.add_field(name='Guild Nickname:', value=member.display_name)

        embed.add_field(name='Created at:', value=member.created_at.strftime('%a, %#d, %B, %Y, %I :%M %p UTC'))
        embed.add_field(name='Top Role:', value=member.top_role.mention)
        embed.add_field(name='Bot?', value=member.bot)
        await ctx.send(embed=embed)

    @commands.command()
    async def announce(self, ctx, *, announcement=None):
        if announcement == None: 
            await ctx.send(f'What would you like to announce?\n\nCorrect Usage:\n`{Prefix.getprefix(ctx.guild)}announce <announcement>')
        else:
            embed=discord.Embed(
                title=f'{ctx.author.name} has made an announcement!',
                description=f'{announcement}',
                colour=discord.Colour.blue()
            )
            embed.set_footer(text=f'Announced by {ctx.author}')
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/696121556119715890/709806706057674872/announcements-icon.png?width=502&height=502')
            await ctx.send(embed=embed)
            await ctx.message.delete()


    @commands.command()
    async def clap(self, ctx, word, word1, word2=None, word3=None, word4=None):
        if word3 == None:
            await ctx.send(f'{word} 👏 {word1} 👏 {word2} 👏 {word}')
        else:
            await ctx.send(f'{word} 👏 {word1} 👏 {word2} 👏 {word3}')



def setup(bot):
    bot.add_cog(misc(bot))
