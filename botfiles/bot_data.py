import discord
import required.commandutils as cu
import os

client = discord.Client()
gatekeeper = cu.Commandler()

prefix = "f."

default_embed_color = "#f57542"

bucket_name = os.environ["AWS_BUCKET_NAME"]
