from ScienceDaily import scrape_for_search, scrape_for_top_link, scrape_for_top_sum, scrape_for_top_title
import discord
from discord.ext import commands
import json
import datetime
from Article import Article


with open('pyconfig.json') as con:
    config = json.load(con)
TOKEN = config['token']


client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('online')
    # TODO: send top link every 24 hours


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
    message = '''**multiply**: _numbers you want me to multiply separated by spaces_\n
    **add**: _numbers you want me to add separated by spaces_\n
    **factorial**: _number you want me to find the factorial of_\n
    **search**: _enter a search term (or many separated by commas) and I will find them in an article_\n'''

    embed = discord.Embed(
        title='Help',
        description=message,
        color=discord.Colour.blue(),
    )
    await ctx.send(embed=embed)


@client.command()
async def top(ctx):
    title = scrape_for_top_title()
    summary = scrape_for_top_sum()
    link = scrape_for_top_link()

    embed = discord.Embed(
        title=title,
        description=summary,
        color=discord.Colour.blue(),
        timestamp=datetime.datetime.utcnow()
    )
    embed.set_author(name="Daily News")
    embed.add_field(name="Link", value=link)

    await ctx.send(embed=embed)


@client.command()
async def search(ctx, *args):
    articles = scrape_for_search(*args)
    for a in articles:
        await ctx.send("**" + a.title + "**: " + a.summary + a.link + "\n")

client.run(TOKEN)
