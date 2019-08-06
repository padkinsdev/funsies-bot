import asyncio
import discord
import os, datetime
import botfiles.bot_data as bot_data
import random

client = bot_data.client
gatekeeper = bot_data.gatekeeper

servers = bot_data.servers

@gatekeeper.serverSpecific([servers["5htp"]])
async def hello(message):
  await message.channel.send("Hello, " + message.author.mention)

@gatekeeper.serverSpecific([servers["5htp"]])
async def commands(message):
  cmd_list = "My Commands:\n"
  for cmd in commandDict.keys():
    cmd_list = cmd_list + cmd + "\n"
  await message.channel.send(cmd_list)

@gatekeeper.serverSpecific([servers["5htp"]])
async def rnum(message):
  params = message.content.split(" ")
  try:
    await message.channel.send(str(random.randint(int(params[1]), int(params[2]))))
  except:
    await message.channel.send("Something went wrong???")

@gatekeeper.serverSpecific([servers["5htp"]])
async def xkcd(message):
  await message.channel.send("https://xkcd.com/{}/".format(str(random.randint(1, 2181))))
    
@gatekeeper.serverSpecific([servers["5htp"]])
async def backup(message):
  success, err = gatekeeper.upload_db()
  if not success:
    await message.channel.send(err)
  else:
    await message.channel.send("Success!")
    
#@gatekeeper.serverSpecific([servers["5htp"]])
#async def daily(message):
#  increase_amount = str(random.randint(50, 100))
#  gatekeeper.userDB.add_to_bal(message.author.id, increase_amount)
#  await message.channel.send("Your balance was increased by " + increase_amount + " funsies")

@gatekeeper.serverSpecific([servers["5htp"]])
async def affirm(message):
  await message.delete()
  await message.channel.send("That's valid, and I hope you feel better soon")
  
@gatekeeper.serverSpecific([servers["5htp"]])
async def stats(message):
  embed = discord.Embed(title="User Stats", color=bot_data.default_embed_color, description="{} stats:\nLevel:\t {}".format(message.author.mention, str(gatekeeper.userDB.get_field(message.author.id, "level"))))
  embed.set_thumbnail(url=bot_data.embed_thumburl)
  await message.channel.send(embed=embed)

def mapNameToFunc(name):
  if name in commandDict.keys():
    return commandDict[name]
  else:
    #print("CMD DNE")
    return None

commandDict = {"hello": hello, "help": commands, "rnum": rnum, "r_num": rnum, "xkcd": xkcd, "backup": backup, "affirm": affirm, "stats": stats}
