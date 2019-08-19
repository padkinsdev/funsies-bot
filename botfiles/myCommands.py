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
    
@gatekeeper.serverSpecific([servers["5htp"]])
async def daily(message):
  increase_amount = str(random.randint(50, 100))
  last_claim = gatekeeper.userDB.get_field(message.author.id, "lastClaim")
  if last_claim:
    last_claim = str(last_claim)
    if last_claim != str(datetime.date.today()):
      gatekeeper.userDB.write_field(message.author.id, "lastClaim", datetime.date.today())
      gatekeeper.userDB.add_to_field(message.author.id, "balance", increase_amount)
      await message.channel.send("Your balance was increased by " + increase_amount + " credits")
    else:
      await message.channel.send("You already claimed today!")
  else:
    gatekeeper.userDB.write_field(message.author.id, "lastClaim", datetime.date.today())
    gatekeeper.userDB.add_to_field(message.author.id, "balance", increase_amount)
    await message.channel.send("Your balance was increased by " + increase_amount + " credits")


@gatekeeper.serverSpecific([servers["5htp"]])
async def slots(message):
  args = message.content.split(" ")
  try:
    bet = int(args[1])
  except:
    await message.channel.send(message.author.mention + " Try `" + bot_data.prefix + "slots <bet_amount>`")
    return None
  cur_bal = gatekeeper.userDB.get_field(message.author.id, "balance")
  if not cur_bal or int(cur_bal) < bet:
    await message.channel.send(message.author.mention + " You don't have enough credits to bet that! Try using `" + bot_data.prefix + "daily`")
    return None
  gatekeeper.userDB.add_to_field(message.author.id, "balance", -1*bet)
  await message.channel.send(message.author.mention + " Rolling...")
  asyncio.sleep(2)
  result_one = random.randint(0,9)
  result_two = random.randint(0,9)
  result_three = random.randint(0,9)
  await message.channel.send(message.author.mention + "Your roll:\n {} {} {}".format(result_one, result_two, result_three))
  if result_one == result_two and result_two == result_three:
    await message.channel.send("Three in a row! You won {} credits".format(bet*10))
    gatekeeper.userDB.add_to_field(message.author.id, "balance", bet*10)
  elif result_one == result_two or result_two == result_three or result_one == result_three:
    await message.channel.send("Two of a kind. Not bad :thinking: . You won {} credits.".format(bet*3))
    gatekeeper.userDB.add_to_field(message.author.id, "balance", bet*3)
  else:
    await message.channel.send(":confused: You didn't win anything...")

@gatekeeper.serverSpecific([servers["5htp"]])
async def affirm(message):
  await message.delete()
  await message.channel.send("That's valid, and I hope you feel better soon")
  
@gatekeeper.serverSpecific([servers["5htp"]])
async def stats(message):
  gatekeeper.userDB.add_to_field(message.author.id, "balance", 0)
  embed = discord.Embed(title="User Stats", color=bot_data.default_embed_color, description="{} stats:\nLevel:\t {} \nBalance:\t {}".format(message.author.mention, str(gatekeeper.userDB.get_field(message.author.id, "level")), str(gatekeeper.userDB.get_field(message.author.id, "balance"))))
  embed.set_thumbnail(url=bot_data.embed_thumburl)
  await message.channel.send(embed=embed)

@gatekeeper.serverSpecific([servers["5htp"]])
async def afk(message):
  if " " not in message.content:
    await message.channel.send("Try `" + bot_data.prefix + "afk <message>`")
    return False
  args = message.content.split(" ")
  args.pop(0)
  gatekeeper.userDB.write_field(message.author.id, "afk", " ".join(args))
  afk_nick = "[AFK] " + message.author.display_name
  await message.author.edit(nick=afk_nick, mute=False, deafen=False)
  await message.channel.send("I set your afk as " + " ".join(args))

@gatekeeper.serverSpecific([servers["5htp"]])
async def not_afk(message):
  success = gatekeeper.userDB.delete_field(message.author.id, "afk")
  if success:
    await message.channel.send("I removed your afk, " + message.author.display_name)
    if message.author.display_name[0:5] == "[AFK] ":
      await message.author.edit(nick=message.author.display_name[6:])
  else:
    await message.channel.send("Something went wrong...")

def mapNameToFunc(name):
  if name in commandDict.keys():
    return commandDict[name]
  else:
    #print("CMD DNE")
    return None

commandDict = {"hello": hello, "help": commands, "rnum": rnum, "r_num": rnum, "xkcd": xkcd, "backup": backup, "affirm": affirm, "stats": stats, "daily": daily, "slots": slots, "afk": afk, "not_afk": not_afk}
