import discord
import botfiles.bot_data as bd
import botfiles.myCommands as mc

client = bd.client
prefix = bd.prefix

@client.event
async def on_message(message):
  if message.content.startswith(prefix):
    command = mc.mapNameToFunc(message.content[2:message.content.find(" ")])
    if command is not None:
      await command(message)
    else:
      await message.channel.send(message.author.mention + " This command doesn't exist")

@client.event
async def on_ready():
  print("Ready. Signed in as " + client.user.name)

bd.client.run(bd.token)
