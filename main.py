import os
import discord
import botfiles.bot_data as bd
import botfiles.myCommands as mc

client = bd.client
prefix = bd.prefix

@client.event
async def on_message(message):
  if client.user.mention in message.content.mentions:
    await message.channel.send("My prefix is " + prefix + " " + message.author.mention)
  if message.content.startswith(prefix):
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
