import discord
import os
import json
import random
import datetime
from datetime import datetime, timedelta, timezone
import keep_alive



intents =discord.Intents.all()
intents.members = True

with open('setting.json', mode="r",encoding="utf8") as jfile:
    jdata=json.load(jfile)

from discord.ext import commands

bot= commands.Bot(command_prefix="%",intents=intents,help_command = None)  
bot.remove_command("help")

tz_utc_8 = timezone(timedelta(hours=8)) # 建立時區UTC+8:00


@bot.event
async def on_ready():
    print(">>Bot is online<<")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name="%help | 歡迎使用"))
                                                        #activity=discord.Streaming(name="【乾離震】哈哈哈!",url=jdata["twitch_url"]) 直播
                                                        #activity=discord.Game(name="a game")
                                                        #activity=discord.Activity(type=discord.ActivityType.listening, name="a song")
                                                        #activity=discord.Activity(type=discord.ActivityType.watching, name="a movie")



@bot.event
async def on_member_join(maber):
    pass

@bot.event
async def on_member_remove(maber):
    pass
    

for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(f'cmds.{Filename[:-3]}')


if __name__=="__main__":
    keep_alive.keep_alive()
    bot.run(jdata["token"])
