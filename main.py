import os
import discord
import botfiles.bot_data as bd
import botfiles.myCommands as mc

client = bd.client
prefix = bd.prefix
pickle_count = 0

@client.event
async def on_message(message):
  if message.author == client.user:
    pass
  else:
    bd.gatekeeper.markovian.update(message)
    if pickle_count >= 10:
      bd.gatekeeper.markovian.pickle_me()
      pickle_count = 0
    else:
      pickle_count += 1
    if client.user.mentioned_in(message) and "@everyone" not in message.content:
      await message.channel.send("My prefix is " + prefix + " " + message.author.mention)
    elif message.content == "y":
      mc.confirm(message.author.id)
      await message.channel.send("Confirmed!")
    elif message.content == "n":
      mc.deconfirm(message.author.id)
    elif message.content.startswith(prefix):
      if " " in message.content:
        command = mc.mapNameToFunc(message.content[2:message.content.find(" ")])
      else:
        command = mc.mapNameToFunc(message.content[2:])
      try:
        await command(message)
      except:
        await message.channel.send(message.author.mention + " This command doesn't exist, or you don't have access to it")

@client.event
async def on_ready():
  bd.gatekeeper.markovian.unpickle_me()
  print("Ready. Signed in as " + client.user.name)

bd.client.run(os.environ['TOKEN'])
