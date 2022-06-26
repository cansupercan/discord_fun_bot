from cmath import sqrt
import discord
import json
import datetime
from datetime import datetime, timedelta, timezone
from discord.ext import commands
import math
from math import factorial
from decimal import Decimal

tz_utc_8 = timezone(timedelta(hours=8)) # 建立時區UTC+8:00

from core.classes import Cog_Extension



with open('setting.json', mode="r",encoding="utf8") as jfile:
    jdata=json.load(jfile)


class mah(Cog_Extension):
    
    @commands.group(invoke_without_command=True,name="mth")
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
    @mth.command()
    async def add(self,ctx,a,b):#加法
        answer=Decimal(a)+Decimal(b)
        await ctx.send(f'答案是({answer})')
    @mth.command()
    async def reduce(self,ctx,a,b):#減法
        answer=Decimal(a)-Decimal(b)
        await ctx.send(f'答案是 ({answer}) ')
    @mth.command()
    async def re(self,ctx,a,b):#減法2
        answer=Decimal(a)-Decimal(b)
        await ctx.send(f'答案是 ({answer}) ')
    @mth.command()
    async def multiplication(self,ctx,a,b):#乘法
        answer=Decimal(a)*Decimal(b)
        await ctx.send(f'答案是 ({answer}) ')
    @mth.command()
    async def mu(self,ctx,a,b):#乘法2
        answer=Decimal(a)*Decimal(b)
        await ctx.send(f'答案是 ({answer}) ')
    @mth.command()
    async def division(self,ctx,a,b):#除法
        answer=Decimal(a)/Decimal(b)
        await ctx.send(f'答案是 ({answer}) ')
    
    @mth.command()
    async def di(self,ctx,a,b):#除法2
        answer=Decimal(a)/Decimal(b)
        await ctx.send(f'答案是 ({answer}) ')
    @mth.command()
    async def sq(self,ctx,a:int):#開根號
        answer=Decimal(sqrt(a))
        await ctx.send(f'答案是 ({answer}) ')
    @mth.command()
    async def fa(self,ctx,a:int):#階乘
        answer=factorial(a)
        await ctx.send(f'答案是 ({answer}) ')
    @mth.command()
    async def p(self,ctx,a:int,b:int):#排列P
        answer=int(factorial(a)/factorial(a-b))
        await ctx.send(f'答案是 ({answer}) ')
    @mth.command()
    async def c(self,ctx,a:int,b:int):#組合C
        answer=int(factorial(a)/(factorial(b)*factorial(a-b)))
        await ctx.send(f'答案是 ({answer}) ')
    @mth.command()
    async def pow(self,ctx,a,b):#次方
        answer=Decimal(a)**Decimal(b)
        await ctx.send(f'答案是 ({answer}) ')
    @mth.command()
    async def pot(self,ctx,a):#平方
        answer=Decimal(a)**2
        await ctx.send(f'答案是 ({answer}) ')
    @mth.command()
    async def pos(self,ctx,a):#立方
        answer=Decimal(a)**3
        await ctx.send(f'答案是 ({answer}) ')
    @mth.command()
    async def pon(self,ctx,a):#10的X次
        answer=10**Decimal(a)
        await ctx.send(f'答案是 ({answer}) ')
    @mth.command()
    async def loo(self,ctx,a):#對數10
        answer=math.log(Decimal(a),10)
        await ctx.send(f'答案是 ({answer}) ')
    @mth.command()
    async def log(self,ctx,a,b):#對數
        answer=math.log(Decimal(a),Decimal(b))
        await ctx.send(f'答案是 ({answer}) ')
    @mth.command()
    async def pi(self,ctx):#pi
        await ctx.send('pi=3.14159265358979323846264338327950288419716939937510582097494459230781640628620899')
    @mth.command()
    async def sam(self,ctx,a):#絕對值
        if(a<0):
            answer=Decimal(a)*-1
        if(a>0):
            answer=a
        if(a==0):
            answer=0
        await ctx.send(f'答案是 ({answer}) ')
    
    


def setup(bot):
    bot.add_cog(mah(bot))
