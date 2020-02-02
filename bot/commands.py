import discord
from discord.ext import commands
import json

from ScienceDaily import scrape_for_title, scrape_for_sum


with open('config.json') as con:
    config = json.load(con)
TOKEN = config['token']


client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('online')


@client.command()  # addition
async def add(ctx, *args):
    sum = 0
    for num in args:
        nums = int(num)
        sum += nums

    await ctx.send(sum)


@client.command()  # multiplication
async def multiply(ctx, *args):
    product = 1
    for num in args:
        nums = int(num)
        product *= nums

    await ctx.send(product)


@client.command()  # factorial
async def factorial(ctx, *args):
    product = 1
    for num in args:
        nums = int(num)
        for x in range(1, nums + 1):
            product *= x

    await ctx.send(product)


@client.command()  # github
async def github(ctx):
    await ctx.send('https://github.com/Pacutacatete100/AINewsBotV2')


@client.command()  # help
async def commandhelp(ctx):
    message = '**multiply**: _numbers you want me to multiply separated by spaces_\n**add**: _numbers you want me to add separated by spaces_\n**factorial**: _number you want me to find the factorial of_\n **search**: _enter a search term (or many separated by commas) and I will find them in an article_\n'

    embed = discord.Embed(
        title='Help',
        description=message,
        color=discord.Colour.blue()

    )
    await ctx.send(embed=embed)


client.run(TOKEN)
