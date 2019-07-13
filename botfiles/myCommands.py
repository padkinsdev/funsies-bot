import asyncio
import botfiles.bot_data as bot_data
#import required.random_quote as rq
client = bot_data.client
gatekeeper = bot_data.gatekeeper

servers = {"5htp":509550635146805269}

@gatekeeper.serverSpecific([servers["5htp"]])
async def hello(message):
  await message.channel.send("Hello, " + message.author.mention)

@gatekeeper.serverSpecific([servers["5htp"]])
async def marry(message):
  if len(message.mentions) > 1:
    await message.channel.send("Polyamory isn't supported quite yet!" + message.author.mention)
  elif len(message.mentions) < 1:
    await message.channel.send("Info on command `<marry>`: Use `" + bot_data.prefix + "marry <@user_to_marry>` to marry a user.")
  else:
    user = message.mentions[0]
    await message.channel.send(user.mention + " Would you like to marry " + message.author.mention + " ? (y/n)")
    pending_marriages.update({user.id:["n", message.author.id]})
    await asyncio.sleep(150)
    if user.id in pending_marriages.keys():
      if pending_marriages[user.id][0] == "n": # technically unnecessary
        await message.channel.send(user.mention + " " + message.author.mention + " Marriage request timed out")
      pending_marriages.pop(user.id)

def confirm(user_id):
  if user_id in pending_marriages.keys():
    pending_marriages[user_id][0] = "y"
    gatekeeper.userDB.new_marriage(user_id, pending_marriages[user_id][1])

def deconfirm(user_id):
  if user_id in pending_marriages.keys():
    pending_marriages.pop(user_id)

def mapNameToFunc(name):
  if name in commandDict.keys():
    return commandDict[name]
  else:
    #print("CMD DNE")
    return None

commandDict = {"hello": hello, "marry": marry}

