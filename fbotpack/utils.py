from botfiles.bot_data import prefix, servers
from botfiles.myCommands import commandDict

class Parser:
  def __init__(self):
    pass
  def say(message, mention=False, details=None):
    translated = ""
    if type(mention) is not bool or type(message) is not str:
      return False
    if type(details) is list:
      if len(details) != 2:
        return False
      elif details[0] not in servers.keys():
        return False
      elif details[1] not in servers[details[0]][1].keys():
        return False
      else:
        translated += "\tchannel = servers[" + details[0]+ "][1][" + details[1] + "]\n\tawait channel.send("
    else:
      translated += "\tawait message.channel.send("
    if mention:
      translated += "\tmessage.author.mention + "
    translated += message + ")"
    return translated
  def erase(self, details=None):
    translated = ""
    if details:
      if "m" in details:
        translated += "\tawait message.delete()\n"
      if "u" in details:
        translated += "\tmessage.author.kick()\n"
      if "c" in details:
        translated += "\tmessage.channel.delete()\n"
    else:
      translated += "message.delete()\n"
    return translated
  def check_contains(self, target, do, command=False):
    if target in commandDict.keys():
      return False
    if command:
      cmdtxt = "async def " + target + "(message):\n" + do(**kwargs)
      #write to file myCommands.py
    else:
      pass # write to separate file that is run through before the if message.content.startswith(prefix) part of main.py
