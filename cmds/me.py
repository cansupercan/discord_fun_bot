from asyncio import tasks
import discord
import os
import json
import random

from core.classes import Cog_Extension
from discord.ext import commands
with open('setting.json', mode="r",encoding="utf8") as jfile:
    jdata=json.load(jfile)

class me(Cog_Extension):
    @commands.command()
    async def yt(self,ctx):
        await ctx.send(jdata['yt_url'])
    
    @commands.command()
    async def twitch(self,ctx):
        await ctx.send(jdata['twitch_url'])

    @commands.command()
    async def name(self,ctx):
        await ctx.send("yt_乾離震#2233")

    @commands.command()
    async def icon(self,ctx):
        await ctx.send("https://i.imgur.com/0fwh9sf.jpg")
    
    



def setup(bot):
    bot.add_cog(me(bot))
