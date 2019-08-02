import os
import discord
import botfiles.bot_data as bd
import botfiles.myCommands as mc

client = bd.client
prefix = bd.prefix

@client.event
async def on_message(message):
  if message.author == client.user:
    pass
  else:
    if client.user.mentioned_in(message) and "@everyone" not in message.content:
      await message.channel.send("My prefix is " + prefix + " " + message.author.mention)
    elif message.content.lower() == "y":
      mc.confirm(message.author.id)
      await message.channel.send("Confirmed!")
    elif message.content.lower() == "n":
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
  print("Ready. Signed in as " + client.user.name)

bd.client.run(os.environ['TOKEN'])
