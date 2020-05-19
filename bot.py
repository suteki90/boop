
import discord
import json
import random
import os
from discord.ext import commands
import Prefix
import aiohttp
import time

def get_prefix(client, message):
    try:
        with open('prefixes.json') as f:
            prefixes = json.load(f)
        
        return commands.when_mentioned_or(prefixes[str(message.guild.id)])(client, message)
    except:
        return commands.when_mentioned_or("-")(client, message)

client = commands.Bot(command_prefix = get_prefix, case_insensitive=True)

client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(' in {} servers | -help' .format(len(client.guilds))))
    print(' ☑️  Bop has awoken.. ☑️')

@client.command(name='ping', description='Returns the bots latency (ms)')
async def ping(ctx):
  t1 = time.perf_counter()
  message = await ctx.send("checking ping...")
  t2 = time.perf_counter()
  ping = round((t2-t1)*1000)
  pingme = str(ping)
  em = discord.Embed(
    title='Bot latency:',
    description='`' + pingme + '`' + 'ms',
    colour=discord.Colour.blue()

  )
  em.add_field(name='Discord Latency:', value=f'`{round(client.latency*1000)}`ms')
  await ctx.send(embed=em)
  await message.delete()



@client.command(aliases=['commands'])
async def help(ctx, choice=None):
  if choice == None:
    embed=discord.Embed(
      title='Categories',
      colour=discord.Colour.blue()
    )
    embed.add_field(name='Server Prefix', value=f'`{Prefix.getprefix(ctx.guild)}`')
    embed.add_field(name='**Moderation**', value=f'Type **{Prefix.getprefix(ctx.guild)}help moderation** to get utility commands!', inline=False),
    embed.add_field(name='**Fun**', value=f'Type **{Prefix.getprefix(ctx.guild)}help fun** to get fun commands!')
    embed.add_field(name='**Misc**', value=f'Type **{Prefix.getprefix(ctx.guild)}help misc** to get miscellaneous commands!', inline=False)
    embed.add_field(name='**Image**', value=f'Type **{Prefix.getprefix(ctx.guild)}help image** to get image commands!', inline=False)
    embed.add_field(name='Support', value='[Bop Server](https://discord.gg/GBfwYCg)')
    await ctx.send(embed=embed)
  if choice == 'moderation':
    embed=discord.Embed(
      title='Moderation commands!',
      description=f'`{Prefix.getprefix(ctx.guild)}mute`\n`{Prefix.getprefix(ctx.guild)}unmute`\n`{Prefix.getprefix(ctx.guild)}kick`\n`{Prefix.getprefix(ctx.guild)}clear`\n`{Prefix.getprefix(ctx.guild)}ban`, `{Prefix.getprefix(ctx.guild)}joinmessage`',
      colour=discord.Colour.blue()
    )
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/696121556119715890/709489095822409858/Utilities-icon.png?width=503&height=503')
    await ctx.send(embed=embed)
  if choice == 'fun':
    embed=discord.Embed(
      title='Fun commands!',
      description=f'`{Prefix.getprefix(ctx.guild)}fact`\n`{Prefix.getprefix(ctx.guild)}quote`\n`{Prefix.getprefix(ctx.guild)}8ball (question)`\n`{Prefix.getprefix(ctx.guild)}coinflip`\n`{Prefix.getprefix(ctx.guild)}roll`\n`{Prefix.getprefix(ctx.guild)}kill (person)`\n`{Prefix.getprefix(ctx.guild)}lenny`\n`{Prefix.getprefix(ctx.guild)}number`\n`{Prefix.getprefix(ctx.guild)}holdup`\n`{Prefix.getprefix(ctx.guild)}bug (person)`\n`{Prefix.getprefix(ctx.guild)}email(person) (message)`\n`{Prefix.getprefix(ctx.guild)}tweet (message)`\n`{Prefix.getprefix(ctx.guild)}declare (message)`\n`{Prefix.getprefix(ctx.guild)}meme`\n`{Prefix.getprefix(ctx.guild)}say`',
      colour=discord.Colour.blue()
    )
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/703034703627681845/709489467706048522/75b.png?width=902&height=382')
    await ctx.send(embed=embed)
  if choice == 'misc':
    embed=discord.Embed(
      title='Miscellaneous commands',
      description=f'`{Prefix.getprefix(ctx.guild)}ping`\n`{Prefix.getprefix(ctx.guild)}creator`\n`{Prefix.getprefix(ctx.guild)}issue`\n`{Prefix.getprefix(ctx.guild)}coronacount`\n`{Prefix.getprefix(ctx.guild)}script`\n`{Prefix.getprefix(ctx.guild)}prefix`\n`{Prefix.getprefix(ctx.guild)}userinfo`\n`{Prefix.getprefix(ctx.guild)}server`, `{Prefix.getprefix(ctx.guild)}suggest (suggestion)`',
      colour=discord.Colour.blue()
    )
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/696121556119715890/709492440566071437/miscellaneous.png')
    await ctx.send(embed=embed)
  if choice == 'image':
    embed=discord.Embed(
      title='Image commands',
      description=f'`{Prefix.getprefix(ctx.guild)}salad`\n`{Prefix.getprefix(ctx.guild)}sandwich`\n`{Prefix.getprefix(ctx.guild)}burger`\n`{Prefix.getprefix(ctx.guild)}corona`\n`{Prefix.getprefix(ctx.guild)}brownies`\n`{Prefix.getprefix(ctx.guild)}sketchers`\n`{Prefix.getprefix(ctx.guild)}popcorn`\n`{Prefix.getprefix(ctx.guild)}cheese`\n`{Prefix.getprefix(ctx.guild)}avatar`\n`{Prefix.getprefix(ctx.guild)}cat`\n`{Prefix.getprefix(ctx.guild)}dog`\n`{Prefix.getprefix(ctx.guild)}food`',
      colour=discord.Colour.blue()
    )
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/696121556119715890/709519766502768740/apps.png')
    await ctx.send(embed=embed)


@client.command()
async def script(ctx):
    embed=discord.Embed(
        title='Script',
        description='This bot was made with python and script written in Visual Studio Code',
        colour=discord.Colour.blue()

    )
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/696121556119715890/704402945927544902/1200px-Visual_Studio_Code_1.png?width=630&height=630')
    await ctx.send(embed=embed)



@client.command()
async def fakespawn(ctx):
    embed=discord.Embed(
        title='‌‌A wild pokémon has аppeаred!',
        description='Guess the pokémon аnd type p!cаtch <pokémon> to cаtch it!',
        colour=discord.Colour.green()


    )
    responses=random.choice(['https://media.discordapp.net/attachments/693584026140672020/694218579700088862/PokecordSpawn.jpg', 'https://media.discordapp.net/attachments/696121556119715890/710175100959195156/1200px-383Groudon.png?width=502&height=502', 'https://media.discordapp.net/attachments/696121556119715890/710175364634247168/151Mew.png?width=502&height=502','https://media.discordapp.net/attachments/696121556119715890/710175423283069081/150Mewtwo.png?width=502&height=502'])
    embed.set_image(url=responses)
    await ctx.send(embed=embed)
    await ctx.message.delete()

@client.command()
async def fakecatch(ctx):
    await ctx.send(f'Congratulations {ctx.author.mention}! You caught a level 32 Eternatus!')

@client.command()
async def british(ctx):
  embed=discord.Embed(
    title='British picture for you',
    colour=discord.Colour.blue()
  )
  responses=random.choice(['https://media.discordapp.net/attachments/625842127284469760/708018725508349972/queen-elizabeth-ii.png?width=777&height=519', 'https://media.discordapp.net/attachments/625842127284469760/708019220121649694/WIPO.png?width=692&height=519', 'https://media.discordapp.net/attachments/625842127284469760/708019360265928793/english-crumpets-1500-58a4acc13df78c4758cd2323.png?width=779&height=519', 'https://media.discordapp.net/attachments/625842127284469760/708019575094116472/OIP.png','https://media.discordapp.net/attachments/704779434674225283/708379024262430750/maxresdefault.png?width=879&height=495','https://media.discordapp.net/attachments/625842127284469760/708377809621483550/image1.jpg?width=879&height=495', 'https://media.discordapp.net/attachments/625842127284469760/708378115813933066/image0.png', 'https://media.discordapp.net/attachments/625842127284469760/708380885317189632/image0.jpg', 'https://media.discordapp.net/attachments/625842127284469760/708380885598339132/image1.jpg?width=755&height=503', 'https://media.discordapp.net/attachments/625842127284469760/708380886143336548/image2.jpg?width=670&height=503', 'https://media.discordapp.net/attachments/625842127284469760/708380886718087208/image3.jpg?width=252&height=503'])
  embed.set_image(url=responses)
  await ctx.send(embed=embed)

@client.event
async def on_command_error(ctx, error):
    if str(error) == "Command raised an exception: Forbidden: 403 Forbidden (error code: 50013): Missing Permissions":
        message = "I dont have permission to do that! Please give me administrator permissions to use the **{}** command".format(ctx.command)
    elif "Command raised an exception: KeyError:" in str(error):
        message = "Invalid warn ID!"
    else:
        message = "**" + str(error) + "**"
    if "not found" not in str(error):
        em = discord.Embed(title="Error", description=str(message), colour=discord.Colour.blue())
        await ctx.send(embed=em)

@client.command(aliases=['url', 'link', 'server'])
async def invite(ctx):
  embed=discord.Embed(
    title='Click below to invite the bot to any server!',
    colour=discord.Colour.blue()
  )
  embed.add_field(name='Link', value='[Invite](https://discordapp.com/api/oauth2/authorize?client_id=694229303964991529&permissions=0&scope=bot)')
  await ctx.send(embed=embed)

@client.command()
async def coolo2(ctx):
  embed=discord.Embed(
    title='Coolo2',
    description='A person that helped me a ton making this bot',
    colour=discord.Colour.blue()
  )
  embed.add_field(name='Youtube', value='[Click here](https://www.youtube.com/channel/UClqTOwlCslNUDzwnO0r0-Ow)')
  embed.add_field(name='Twitter', value='[Click here](https://twitter.com/ItsCoolo2)')
  embed.add_field(name='Reddit', value='[Click here](https://www.reddit.com/user/Coolo2)')
  embed.add_field(name='Twitch', value='[Click here](https://www.twitch.tv/itscoolo2)')
  embed.set_image(url='https://images-ext-2.discordapp.net/external/4DLB4sp_I8gAkSnzN42TmLXTZX-_GIyZTWDsd8a72NQ/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/368071242189897728/86546110c062cff41b8694ef0d349bed.webp')
  await ctx.send(embed=embed)

@client.command(aliases=['about'])
async def botinfo(ctx):
    embed=discord.Embed(
        title='Information about Bop',
        description='A fun bot with moderation commands and many fun commands!',
        colour=discord.Colour.blue()
    )
    embed.add_field(name='ID', value='694229303964991529')
    embed.add_field(name='Creator', value='Suteki#3477')
    embed.set_thumbnail(url='https://images-ext-1.discordapp.net/external/VSgY9tM_E0q2ihF7jLLhSafPyweBiESWlRRIGYw5LSM/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/694229303964991529/176125221fdfd75cc1a13f7a81691697.webp?width=502&height=502')
    embed.add_field(name='Server count', value=len(client.guilds))
    embed.add_field(name='Created with', value='Python 3.8, Visual Studio Code')
    embed.add_field(name='Created at', value='March 30, 2020')
    await ctx.send(embed=embed)

@client.command()
async def servercount(ctx):
  await ctx.send('I am currently in **{}** servers' .format (len(client.guilds)))


@client.event
async def on_member_join(member):
    try:
        channel=discord.utils.get(member.guild.channels, name='bjoins')
        await channel.send(f'{member.mention} has joined **{member.guild.name}**.')
    except:
        pass

@client.command()
async def joinmessage(ctx):
    await ctx.send('If you would like join and leave messages from Bop, please create a channel named #bjoins and #bleaves. Currently, they cannot be custom messages.')

@client.event
async def on_member_remove(member):
  try:
    channel=discord.utils.get(member.guild.channels, name='bleaves')
    await channel.send(f'{member.name} has left **{member.guild.name}**.')
  except:
    pass


  
@client.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def suggest(ctx, *, suggestion):
  await client.get_user(449662597927665666).send(f'{ctx.author} has suggested something: `{suggestion}`')
  embed=discord.Embed(
    title=f'You have suggested {suggestion}',
    description='The owner will review your suggestion',
    colour=discord.Colour.blue()
  )
  await ctx.send(embed=embed)

@client.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def report(ctx, *, issue=None):
  if issue == None:
    await ctx.send(f'**What issue have you found?**\n\nCorrect Usage: `{Prefix.getprefix(ctx.guild)}report <issue>')
  else:
    await client.get_user(449662597927665666).send(f'{ctx.author} has found an **issue**: `{issue}`')
    embed=discord.Embed(
      title=f'You have reported {issue}',
      description='The owner will review it soon..',
      colour=discord.Colour.blue()
    )
    await ctx.send(embed=embed)

@client.command()
async def doesthiswork(ctx):
  await ctx.send('well, ya')


extensions = ['fun', 'misc', 'image', 'utility']

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
            print('Loaded {}'.format(extension))
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))


token = os.environ.get("Token")
client.run(token)
