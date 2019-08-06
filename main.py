import os, signal
import sys
import discord
import asyncio
import botfiles.bot_data as bd
import botfiles.myCommands as mc
import botfiles.preprocess as pp

client = bd.client
prefix = bd.prefix

@client.event
async def on_message(message):
  if message.author == client.user:
    pass
  else:
    pp.preprocess_list(message)
    if client.user.mentioned_in(message) and "@everyone" not in message.content:
      await message.channel.send("My prefix is " + prefix + " " + message.author.mention)
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
  bd.gatekeeper.get_db()
  print("Ready. Signed in as " + client.user.name)

async def store_db():
  while True:
    await asyncio.sleep(600)
    success, err = bd.gatekeeper.upload_db()
    #if success:
    #  print("Autostored db")
    #else:
    #  print(str(err))

bd.client.loop.create_task(store_db())
bd.client.run(os.environ['TOKEN'])
