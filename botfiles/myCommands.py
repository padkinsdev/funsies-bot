#import discord
import asyncio
import botfiles.bot_data as bot_data
client = bot_data.client
gatekeeper = bot_data.gatekeeper

servers = {"5htp":509550635146805269}

@gatekeeper.serverSpecific([servers["5htp"]])
async def hello(message):
  await message.channel.send("Hello, " + message.author.mention)

@gatekeeper.serverSpecific([servers["5htp"]])
async def marry(message):
  await message.channel.send("Coming soon to a theater near you")

@gatekeeper.requiresPermission(["owner"])
@gatekeeper.serverSpecific([servers["5htp"]])
async def begone(message):
  await message.channel.send("K then. Be like that smh")
  await client.logout()

@gatekeeper.serverSpecific([servers["5htp"]])
async def randommeme(message):
  pass

def mapNameToFunc(name):
  if name in commandDict.keys():
    return commandDict[name]
  else:
    #print("CMD DNE")
    return None

commandDict = {"hello": hello, "marry": marry, "begone": begone}

