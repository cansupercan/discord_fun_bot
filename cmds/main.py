import discord
import json
import datetime
from datetime import datetime, timedelta, timezone
from discord.ext.commands import has_permissions,MissingPermissions
from discord.ext import commands
from pip import main
from opencc import OpenCC
import wikipedia
from core.classes import Cog_Extension
with open('setting.json', mode="r",encoding="utf8") as jfile:
    jdata=json.load(jfile)


class main(Cog_Extension):
    @commands.command(name="severbanner")
    async def server_banner(self, ctx):
        if not ctx.guild.banner:
            return await ctx.send("這個伺服器沒有橫幅...")
        await ctx.send(f"伺服器 **{ctx.guild.name}**的橫幅\n{ctx.guild.banner.with_format('png')}")    
    @commands.command()
    async def wiki(self,ctx,word):
        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
        wikipedia.set_lang("zh-tw")
        cc = OpenCC('s2twp')#s2tw
        page1 = wikipedia.page(word)
        embed = discord.Embed(title=f"**維基百科:({cc.convert(page1.title)})**",description=cc.convert(wikipedia.summary(word,sentences=10,chars=300)), timestamp=dt)
        embed.set_footer(icon_url=jdata["bot_head_url"],text=jdata["bot_name"])
        embed.add_field(name='🖇網址', value=f'{page1.url}', inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}ms')
    @commands.command()
    async def invite(self,ctx):
        await ctx.send("")
    
    @commands.command()
    async def severavatar(self,ctx):
        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
        pfp=ctx.guild.icon_url
        name=ctx.guild.name
        embed=discord.Embed(title=str(name)+"的頭像",  color=0x4DFFFF, timestamp=dt) 
        embed.set_image(url=pfp)
        embed.set_footer(icon_url=jdata["bot_head_url"],text=jdata["bot_name"])
        await ctx.send(embed=embed)

    @commands.command()
    async def sever(self,ctx):
        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
        embed = discord.Embed(title=f"{ctx.guild.name} 內容", description="關於伺服器的內容", color=0xF9F900,timestamp=dt)
        embed.add_field(name='🆔伺服器ID', value=f"{ctx.guild.id}", inline=True)
        ye=int(ctx.guild.created_at.strftime("%Y"))
        yeroc=str(ye-1911)
        anye="民國"+yeroc+str(ctx.guild.created_at.strftime("(%Y)年 %m月 %d日"))
        embed.add_field(name='📆創建於', value=anye, inline=True)
        embed.add_field(name='👑擁有者', value=f"{ctx.guild.owner.mention}", inline=True)
        embed.add_field(name='👥成員數', value=f'{ctx.guild.member_count} 位成員', inline=True)
        embed.add_field(name='💬頻道數', value=f'{len(ctx.guild.text_channels)} 個文字頻道 | {len(ctx.guild.voice_channels)} 個語音頻道', inline=True)
        embed.add_field(name='🌎地區', value=f'{ctx.guild.region}', inline=True)
        embed.set_thumbnail(url=ctx.guild.icon_url) 
        embed.set_footer(icon_url=jdata["bot_head_url"],text=jdata["bot_name"])    
        embed.set_author(name=f'{ctx.author.name}', icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)

 
    @commands.command()
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def now(self,ctx):
        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
        ct=int(dt.strftime("%Y"))-1911  #民國
        et=dt.strftime("(%Y)年%m月%d日 %H:%M")#西元
        msg="民國"+str(ct)+et
        await ctx.send(msg)
        
    @commands.command()
    async def userstats(self,ctx,member: discord.Member = None):
        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
        pfp=member.avatar_url
        embed=discord.Embed(title=member,  color=0xB15BFF, timestamp=dt) 
        embed.set_thumbnail(url=pfp)
        embed.add_field(name="用戶暱稱", value=member.nick, inline=False)
        embed.add_field(name="用戶ID", value=member.id, inline=False)
        it=member.created_at
        ct=it.strftime("(%Y)年%m月%d日 %H:%M")#西元
        chan1=int(it.strftime("%Y"))-1911  #民國
        al1="民國"+str(chan1)+ct
        embed.add_field(name="帳號建立時間", value=al1, inline=False) 
        it2=member.joined_at
        ct2=it2.strftime("(%Y)年%m月%d日 %H:%M")
        chan2=int(it2.strftime("%Y"))-1911  #民國
        al2="民國"+str(chan2)+ct2
        embed.add_field(name="甚麼時候加入的", value=al2, inline=False) 
        st=member.raw_status
        if (st=="online"):
            embed.add_field(name="當前狀態", value="上線", inline=False)
        elif (st=="idle"):
            embed.add_field(name="當前狀態", value="閒置", inline=False)
        elif (st=="dnd"):
            embed.add_field(name="當前狀態", value="請勿打擾", inline=False)
        elif (st=="offline"):
            embed.add_field(name="當前狀態", value="不在線", inline=False)
        else:
            embed.add_field(name="當前狀態", value=member.raw_status, inline=False)
        fd=str(member.activity)
        if(fd=="None"):
          embed.add_field(name="當前活動",  value="名字:[無]", inline=False)
        else:
          embed.add_field(name="當前活動",  value=f"名字:[{member.activity.name}]", inline=False)
        a1=str(member.activity.state)
        if(a1=="None"):
            a2=str(member.activity.name)
            if(a2=="None"):
                embed.add_field(name="當前活動", value=f"無", inline=False)               
        else:
            a2=str(member.activity.name)
            embed.add_field(name="當前活動", value=f"活動:[{a1}] \n 名字:[{a2}] \n ", inline=False)
        embed.set_footer(icon_url=jdata["bot_head_url"],text=jdata["bot_name"])
        await ctx.send(embed=embed)
    
    @commands.command()
    async def avatar(self,ctx,member: discord.Member = None):
        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
        pfp=member.avatar_url
        name=member.name
        embed=discord.Embed(title=str(name)+"的頭像",  color=0x4DFFFF, timestamp=dt) 
        embed.set_image(url=pfp)
        embed.set_footer(icon_url=jdata["bot_head_url"],text=jdata["bot_name"])
        await ctx.send(embed=embed)
        
    

    @commands.group(invoke_without_command=True,name="help")        
    async def help(self,ctx):
        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
        embed=discord.Embed(title="指令列表", description="這裡有這個機器人所有的指令", color=0x00aaff, timestamp=dt) 
        embed.set_thumbnail(url=jdata["authur_icon"])
        embed.set_author(name=jdata["bot_name"], icon_url=jdata["bot_head_url"])
        embed.add_field(name="%ping", value="可以查詢當下的PING值", inline=False)
        embed.add_field(name="%help author", value="有關機器人作者的資訊", inline=False)
        embed.add_field(name="%mth", value="數學計算", inline=False)
        embed.add_field(name="%sayd", value="讓機器人說你想要說的話", inline=False)
        embed.add_field(name="%avatar", value="帳號頭像", inline=False)
        embed.add_field(name="%severavatar", value="查詢伺服器頭像", inline=False)
        embed.add_field(name="%userstats", value="帳號資訊", inline=False)
        embed.add_field(name="%sever", value="查詢伺服器資訊", inline=False)
        embed.add_field(name="%severbanner", value="查詢當前伺服器的橫幅", inline=False)
        embed.add_field(name="%now", value="查詢現在的時間", inline=False)
        embed.add_field(name="%fun", value="查詢玩樂類指令", inline=False)
        embed.add_field(name="%wiki", value="在維基百科上查詢並返回網址與部分內文", inline=False)
        await ctx.send(embed=embed)
    
    @help.command()
    async def fun(self,ctx):
        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
        embed=discord.Embed(title="fun指令列表", description="這裡有這個機器人所有的fun指令", color=0x00aaff, timestamp=dt) 
        embed.set_thumbnail(url=jdata["authur_icon"])
        embed.set_author(name=jdata["bot_name"], icon_url=jdata["bot_head_url"])
        embed.add_field(name="%fortune", value="占卜運勢", inline=False)
        embed.add_field(name="%slot", value="玩角子老虎機乙次", inline=False)
        embed.add_field(name="%coin", value="執硬幣(正反面)", inline=False)
        embed.add_field(name="%confess", value="告白(例:%confess <member> <message>)", inline=False)
        embed.add_field(name="%flirt", value="撩人(例:%flirt <member> <message>)", inline=False)
        embed.add_field(name="%ship", value="匹配程度(例:%ship <member1> <member2>)", inline=False)
        embed.add_field(name="%draw", value="抽籤(%draw <內容>)", inline=False)
        embed.add_field(name="%drawall", value="抽籤(含不在線成員)(%draw <內容>)", inline=False)
        await ctx.send(embed=embed)

    @help.command()
    async def mth(self,ctx):
        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
        embed2=discord.Embed(title="mth指令列表", description="這裡有這個機器人所有關於mth的指令", color=0x00aaff, timestamp=dt) 
        embed2.set_thumbnail(url=jdata["authur_icon"])
        embed2.set_footer(text="請勿超過16位數")
        embed2.set_author(name=jdata["bot_name"], icon_url="https://i.imgur.com/ZZiRnlt.jpg")
        embed2.add_field(name="add {x} {y}", value="x+y", inline=False)
        embed2.add_field(name="reduce {x} {y}", value="x-y(可以縮寫成re {X} {y})", inline=False)
        embed2.add_field(name="multiplication {x} {y}", value="x*y(可以縮寫成mu {X} {y})", inline=False)
        embed2.add_field(name="division {x} {y}", value="x/y(可以縮寫成di {X} {y})", inline=False)
        embed2.add_field(name="pow {x} {y}", value="x^y(Y次方的X)", inline=False)
        embed2.add_field(name="pos {x} ", value="x^3(立方)", inline=False)
        embed2.add_field(name="pot {x} ", value="x^2(平方)", inline=False)
        embed2.add_field(name="pon {x} ", value="10^X(10的X次)", inline=False)
        embed2.add_field(name="sq {x} ", value="√x(開根號)", inline=False)
        embed2.add_field(name="fa {x} ", value="x!(階乘x)", inline=False)
        embed2.add_field(name="c {x} {y}", value="c x/y (排列組合的C=x!/y!/(x-y)!)", inline=False)
        embed2.add_field(name="p {x} {y}", value="p x/y (排列組合的P=x!/y!)", inline=False)
        embed2.add_field(name="loo {x} ", value="logX/10(底數為10真數為X)", inline=False)
        embed2.add_field(name="log {x} {y}", value="logx/y (底數為Y真數為X))", inline=False)
        embed2.add_field(name="pi", value="查詢圓周率", inline=False)
        embed2.add_field(name="sam {x} ", value="|x|(x的絕對值)", inline=False)
        await ctx.send(embed=embed2)
    
    @help.command()
    async def author(self,ctx):
        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
        embed2=discord.Embed(title="author指令列表", description="這裡有這個機器人所有關於author的指令", color=0x00aaff, timestamp=dt) 
        embed2.set_thumbnail(url=jdata["authur_icon"])
        embed2.set_author(name=jdata["bot_name"], icon_url=jdata["bot_head_url"])
        embed2.add_field(name="%yt", value="作者的yt頻道", inline=False)
        embed2.add_field(name="%icon", value="作者的頭像", inline=False)
        embed2.add_field(name="%name", value="作者的帳號", inline=False)
        await ctx.send(embed=embed2)
def setup(bot):
    bot.add_cog(main(bot))
