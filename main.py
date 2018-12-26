# Anti Swear Bot

#Discord Imports
import discord
from discord.ext import commands

#Other Imports
import json

#Requirements
TOKEN = 'NoToken4U'
prefix = "-"
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")

#Other main vars
#serversCount = len(bot.guild) + 1

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    #await bot.change_presence(game=discord.Game(name="Used by " + str(serversCount) + " servers!"))

#General Bot
@bot.command(pass_context=True)
async def help(ctx):
    embedC = 0xff0000
    embed = discord.Embed(title="**- Commands -**", description="", color=embedC)
    embed.add_field(name="{}help".format(prefix), value="Shows this message", inline=False)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def getemoji(ctx, emoji):
    with open('reactions.json') as u:
        data = json.load(u)

    data['users'].append({"name": str(ctx.message.author),"react": str(emoji)})
    
    with open('reactions.json', 'w') as f:
        json.dump(data, f, indent=2)

@bot.event
async def on_message(message):
    if not message.author.bot:
        with open('reactions.json') as u:
            data = json.load(u)

        for user in data['users']:
            name = user['name']
            toAdd = user['react']
            if str(name) == str(message.author):
                await message.add_reaction(toAdd)

    await bot.process_commands(message)

bot.run(TOKEN)
