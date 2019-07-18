import discord
from botfiles.bot_data import default_embed_color
import datetime

def create_embed(title, content, color=default_embed_color, description=discord.Embed.Empty, author=discord.Embed.Empty, emb_type="rich", time_stamp=datetime.now(), url=discord.Embed.Empty):
  embed = discord.Embed(title=title, content=content, color=color, description=description, author=author, type=emb_type, timestamp=time_stamp, url=url)
  return embed
