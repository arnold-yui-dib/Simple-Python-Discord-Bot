import discord
from discord.ext.commands import Bot
from discord.ext import commands

client = discord.Client()
bot_prefix= "m"
Client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print ("Github https://github.com/arnold-yui-dib/Simple-Python-Discord-Bot/")
   
@client.event
async def on_message(message):
    if message.content == "M":
        await client.send_message(message.channel, "You are getting real dirty")
    print ("Dirty people pervs")
    if message.content == "Bad-stuff":
        await client.send_message(message.channel, ":middle_finger:")
        print ("Bad-stuff")
client.run("MToken")
