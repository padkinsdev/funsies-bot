import asyncio
import botfiles.bot_data as bot_data
import required.some_utils as su

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
    await message.channel.send("Info on command `<marry>`: Use `" + bot_data.prefix + "marry <@user_to_marry>` to marry a user, and commit to loving them until forever and ever (or something like that).")
  else:
    user = message.mentions[0]
    await message.channel.send(user.mention + " Would you like to marry " + message.author.mention + " ? (y/n)")
    pending_marriages.update({user.id:["n", message.author.id]})
    await asyncio.sleep(150)
    if user.id in pending_marriages.keys():
      #if pending_marriages[user.id][0] == "n": # technically unnecessary
      await message.channel.send(user.mention + " " + message.author.mention + " Marriage request timed out")
      pending_marriages.pop(user.id)
      
@gatekeeper.serverSpecific([servers["5htp"]])
async def check_marriages(message):
  marriages = gatekeeper.userDB.get_marriages_for_user(str(message.author.id))
  if len(marriages) > 0:
    embed_format = ""
    for item in marriages:
      embed_format = embed_format + "<@!" + str(item) + ">\n"
    #embed = su.create_embed(title="Marriages", content=message.author.name + " has married:\n" + embed_format)
    await message.channel.send(message.author.mention + " has married:\n" + embed_format)
  else:
    await message.channel.send("You, my friend, are single as a Pringle")

@gatekeeper.serverSpecific([servers["5htp"]])
async def divorce(message):
  if len(message.mentions) == 1:
    gatekeeper.userDB.delete_marriage(message.author.id, message.mentions[0].id)
    await message.channel.send(message.author.mention + " I pronounce you not married")
  else:
    await message.channel.send("Info on command `<divorce>`: Use " + bot_data.prefix + "divorce <@user_to_divorce> to divorce from a user and suffer from intense feelings of guilt.")

@gatekeeper.serverSpecific([servers["5htp"]])
async def imitate_me(message):
  if message.author.id in gatekeeper.markovian.probabilities.keys():
    await message.channel.send(gatekeeper.markovian.gen_text(message.author.id))
  else:
    await message.channel.send("Sorry " + message.author.mention + " I don't have enough data to imitate you")

@gatekeeper.serverSpecific([servers["5htp"]])
async def help(message):
  cmd_list = "My Commands:\n"
  for cmd in commandDict.keys():
    cmd_list = cmd_list + cmd + "\n"
  await message.channel.send(cmd_list)

def confirm(user_id):
  if user_id in pending_marriages.keys():
    pending_marriages[user_id][0] = "y"
    gatekeeper.userDB.new_marriage(user_id, pending_marriages[user_id][1])
    pending_marriages.pop(user_id)

def deconfirm(user_id):
  if user_id in pending_marriages.keys():
    pending_marriages.pop(user_id)

def mapNameToFunc(name):
  if name in commandDict.keys():
    return commandDict[name]
  else:
    #print("CMD DNE")
    return None

commandDict = {"hello": hello, "marry": marry, "check_marriages": check_marriages, "divorce": divorce, "imitate_me": imitate_me}

pending_marriages = {}

help_info = {}
