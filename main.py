import discord.ext.commands
#from discord.ext.commands import Bot
#from discord.ext.commands import MemberConverter

signOffKey = random.randint(1,1000000)
ownerId = # insert owner's discord id here
last_messages = {}

TOKEN = # insert token here

client = discord.Client()

@client.event
async def on_message(message):
    if (message.content.startswith("$$")):
        # commands go here. the bot's prefix is $$
        if (message.content.startswith("$$sayhello")):
            await message.channel.send("Hello World!")

@client.event
async def on_ready():
  #await client.change_presence(game=Game(name="with your feelings"))
  print("Logged in as " + client.user.name)
  print("Sign Off Key: " + str(signOffKey))


async def list_servers():
  await client.wait_until_ready()
  while not client.is_closed:
    print("Current servers:")
    for server in client.servers:
      print(server.name)
    await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)
