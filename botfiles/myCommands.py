import asyncio
import botfiles.bot_data as bot_data
import required.some_utils as su
import random

client = bot_data.client
gatekeeper = bot_data.gatekeeper

servers = {"5htp":509550635146805269}

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
async def test_bucket(message):
  success, error = gatekeeper.bucket_handler.get_as_file("test.txt")
  if success:
    with open("test.txt", "r") as test:
      text = test.read()
      await message.channel.send(text)
  else:
    await message.channel.send(str(error))
    
@gatekeeper.serverSpecific([servers["5htp"]])
async def backup(message):
  success, error = gatekeeper.bucket_handler.upload_file("userDB.db", "userDB.db")
  if success:
    await message.channel.send("Data was successfully backed up")
  else:
    await message.channel.send(str(error))

def mapNameToFunc(name):
  if name in commandDict.keys():
    return commandDict[name]
  else:
    #print("CMD DNE")
    return None

commandDict = {"hello": hello, "help": commands, "rnum": rnum, "r_num": rnum, "xkcd": xkcd, "test_bucket": test_bucket}

pending_marriages = {}

help_info = {}
