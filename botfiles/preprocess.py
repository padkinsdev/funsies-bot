import botfiles.bot_data as bd
import math
import discord

gatekeeper = bd.gatekeeper

def update_activity(message):
  uptick(message.author.id, "activity")

async def check_level_up(message):
  curLevel = gatekeeper.userDB.get_field(message.author.id, "level")
  if not curLevel:
    gatekeeper.userDB.write_field(message.author.id, "level", 1)
  elif gatekeeper.userDB.get_field(message.author.id, "activity") == 100*math.pow((int(curLevel)+1), bd.level_up_factor):
    # Did the message sender level up?
    uptick(message.author.id, "level")
    await message.channel.send(message.author.mention + " Congrats! You are now level {}".format(curLevel))

### Bullet list of things the bot needs to do before checking the command list
def preprocess_list(message):
  update_activity(message)
  await check_level_up(message)

### Utilities
def uptick(user_id, field_name):
  curVal = gatekeeper.userDB.get_field(user_id, field_name)
  if curVal:
    gatekeeper.userDB.write_field(user_id, field_name, int(curVal)+1)
  else:
    gatekeeper.userDB.write_field(user_id, field_name, 1)
