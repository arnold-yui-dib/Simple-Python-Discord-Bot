import discord
from discord.ext.commands import Bot
from discord.ext import commands

client = discord.Client()
bot_prefix= "m"
Client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print ("Github https://github.com/arnold-yui-dib/Simple-Python-Discord-Bot/")
   
@client.command(pass_context=True)
async def M(ctx):
    await client.say("Are you trying to get dirty on me?")
    print ("You trying to get dirty perv?")

client.run("MToken")
