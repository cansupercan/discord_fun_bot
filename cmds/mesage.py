from time import sleep
import discord
import json
import random
import datetime


from core.classes import Cog_Extension
with open('setting.json', mode="r",encoding="utf8") as jfile:
    jdata=json.load(jfile)

from discord.ext import commands



class mesage(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self,msg):
        

        if msg.content=="早安" and msg.author != self.bot.user :
            rely=await msg.reply("早安 你好")
            await rely.add_reaction("☀")
            
        if msg.content=="goodmorning" and msg.author != self.bot.user :
            rely=await msg.reply("早安 你好")
            await rely.add_reaction("☀")
            
        if msg.content=="午安" and msg.author != self.bot.user :
            rely=await msg.reply("午安 吃飯了!!")
            await rely.add_reaction("🍽")
            
        if msg.content=="晚安" and msg.author != self.bot.user :
            rely=await msg.reply("晚安 該睡覺了喔!")
            await rely.add_reaction("🌜")
            
        if "歡迎"in (" " +msg.content+ " ") and msg.author != self.bot.user :
            rely=await msg.reply("歡迎")
            await msg.channel.send("https://i.imgur.com/sIdEGUR.gifv")
            await rely.add_reaction("🥳")
            
        if "wellcome"in (" " +msg.content+ " ") and msg.author != self.bot.user :
            rely=await msg.reply("歡迎 ")
            await msg.channel.send("https://i.imgur.com/sIdEGUR.gifv")
            await rely.add_reaction("🥳")
            
        if "你好"in (" " +msg.content+ " ") and msg.author != self.bot.user :
            await msg.reply("你好 ")
            await msg.channel.send("https://i.imgur.com/Yb4jLsa.gifv")
            
        if msg.content=="hi" and msg.author != self.bot.user :
            await msg.reply("你好")
            await msg.channel.send("https://i.imgur.com/Yb4jLsa.gifv")
            
        if "驚訝"in (" " +msg.content+ " ") and msg.author != self.bot.user :
            await msg.reply("https://i.imgur.com/vyQ6wFr.mp4")
            
        if "抽獎"in (" " +msg.content+ " ") and msg.author != self.bot.user :
            await msg.reply("https://i.imgur.com/EybKWgR.png")
            
        if "自信"in (" " +msg.content+ " ") and msg.author != self.bot.user :
            await msg.reply("https://i.imgur.com/ZEQ1GIO.mp4")
            
        if "無限"in (" " +msg.content+ " ") and msg.author != self.bot.user : #第1次大更新
            await msg.reply("https://i.imgur.com/eeJ8q4l.png")
            
        if "黑暗大法師"in (" " +msg.content+ " ") and msg.author != self.bot.user :
            await msg.reply("https://i.imgur.com/eeJ8q4l.png")
            
        if "泡影"in (" " +msg.content+ " ") and msg.author != self.bot.user :
            await msg.reply("https://i.imgur.com/6bjHkN4.jpg")
            
        if "校分"in (" " +msg.content+ " ") and msg.author != self.bot.user :
            await msg.reply("https://i.imgur.com/d7kz0wL.jpg")
            
        if "蟑螂"in (" " +msg.content+ " ") and msg.author != self.bot.user :
            await msg.reply("https://i.imgur.com/huFaOEt.jpg")
            
        if "拷問"in (" " +msg.content+ " ") and msg.author != self.bot.user :
            await msg.reply("https://i.imgur.com/i1gfqdR.jpg")
            
        if "康師父"in (" " +msg.content+ " ") and msg.author != self.bot.user :
            await msg.reply("https://i.imgur.com/jS8eIkS.jpg")
            
        if "鳳凰人"in (" " +msg.content+ " ") and msg.author != self.bot.user :
            await msg.reply("https://i.imgur.com/7pG10y4.jpg")
            
        if "掃地"in (" " +msg.content+ " ") and msg.author != self.bot.user :
            await msg.reply("https://i.imgur.com/NNn9vyn.jpg")
            
        if "一滴"in (" " +msg.content+ " ") and msg.author != self.bot.user :
            await msg.reply("https://i.imgur.com/6WG6icM.jpg")
            
        if "無效"in (" " +msg.content+ " ") and msg.author != self.bot.user :
            await msg.reply("https://i.imgur.com/zb14tRF.jpg")
            
        if "灰了"in (" " +msg.content+ " ") and msg.author != self.bot.user :
            await msg.reply("https://i.imgur.com/zb14tRF.jpg")
            
        



def setup(bot):
    bot.add_cog(mesage(bot))
