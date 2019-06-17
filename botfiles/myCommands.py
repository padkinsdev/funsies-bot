import asyncio
import botfiles.bot_data as bot_data
client = bot_data.client
gatekeeper = bot_data.gatekeeper

async def hello(message):
  await message.channel.send("Hello, " + message.channel.mention)

def mapNameToFunc(name):
  if name in commandDict.keys():
    return commandDict[name]
  else:
    return None

commandDict = {"hello": hello}
