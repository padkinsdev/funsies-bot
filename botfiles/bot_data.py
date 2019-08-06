import discord
import required.commandutils as cu
import os

client = discord.Client()
gatekeeper = cu.Commandler()

prefix = "f."

default_embed_color = 0xf57542

bucket_name = os.environ["AWS_BUCKET_NAME"]

servers = {"5htp":509550635146805269}

embed_thumburl = "https://i.imgur.com/o4Hqucc.gif"
