from time import sleep
import discord
import json
import random
import datetime
from datetime import datetime, timedelta, timezone


from core.classes import Cog_Extension
with open('setting.json', mode="r",encoding="utf8") as jfile:
    jdata=json.load(jfile)

from discord.ext import commands
from random import choice



class mesage(Cog_Extension):
    @commands.command()
    async def guess(self, ctx):
    
        def check(number):
            return number.author == ctx.author and number.channel == ctx.message.channel
        global lowernumber
        global highernumber
    
        lowernumber = 1
        highernumber = 100

        time=7
    
        number = random.randint(lowernumber, highernumber)
        # print(number)
    
        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
        embed=discord.Embed(title="猜數字遊戲開始!", description="請輸入數字範圍1~100", color=0xffffff, timestamp=dt) 
        embed.set_thumbnail(url="https://i.imgur.com/8BtJsXc.jpg")
        embed.set_footer(text=f"還剩下7次機會", icon_url=jdata["bot_head_url"])
        await ctx.send(embed=embed)

    
        for i in range(0, 8):    
            response = await self.bot.wait_for('message', check = check)
            time=time-1
        
            try : 
                guess = int(response.content) 
        
            except:
                dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
                dt = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
                embed=discord.Embed(title="猜數字遊戲", description="請輸入數字", color=0xffffff, timestamp=dt) 
                embed.set_thumbnail(url="https://i.imgur.com/97olOK4.jpg")
                embed.set_footer(text=f"需要重新開始", icon_url=jdata["bot_head_url"])
                await ctx.send(embed=embed)

            if time==0:
                dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
                dt = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
                embed=discord.Embed(title="猜數字遊戲結束!", description=f"{ctx.author.mention}你已經使用7次機會了!答案是{number}", color=0xffffff, timestamp=dt) 
                embed.set_thumbnail(url="https://i.imgur.com/97olOK4.jpg")
                await ctx.send(embed=embed)
                break
            
            if guess == number : 
                dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
                dt = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
                embed=discord.Embed(title="恭喜你!", description=f"{ctx.author.mention}猜對了", color=0x008000, timestamp=dt) 
                embed.set_thumbnail(url="https://i.imgur.com/Gi6vnEn.jpg")
                await ctx.send(embed=embed)
                break
            
            if guess > 100 or guess==0:
                dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
                dt = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
                embed=discord.Embed(title="猜數字遊戲", description="超過100,格式錯誤!請輸入數字範圍1~100", color=0xffffe8, timestamp=dt) 
                embed.set_thumbnail(url="https://i.imgur.com/97olOK4.jpg")
                embed.set_footer(text=f"還剩下{time}次機會", icon_url=jdata["bot_head_url"])
                await ctx.send(embed=embed, mention_author=False)

            
            if guess < number and guess <= 100 and guess!=0:
                lowernumber = guess
                dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
                dt = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
                embed=discord.Embed(title="猜數字遊戲", description=f"{ctx.author.name}", color=0xffffe8, timestamp=dt) 
                embed.set_thumbnail(url="https://i.imgur.com/8BtJsXc.jpg")
                embed.set_footer(text=f"還剩下{time}次機會", icon_url=jdata["bot_head_url"])
                embed.add_field(name=f"比 {lowernumber}大，比 {highernumber} 小", value="祝猜對", inline=False)
                await ctx.send(embed=embed, mention_author=False)
            
            if guess > number and guess <= 100 and guess!=0:
                highernumber = guess
                dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
                dt = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
                embed=discord.Embed(title="猜數字遊戲", description=f"{ctx.author.name}", color=0xffffe8, timestamp=dt) 
                embed.set_thumbnail(url="https://i.imgur.com/8BtJsXc.jpg")
                embed.set_footer(text=f"還剩下{time}次機會", icon_url=jdata["bot_head_url"])
                embed.add_field(name=f"比 {lowernumber}大，比 {highernumber} 小", value="祝猜對", inline=False)
                await ctx.send(embed=embed, mention_author=False)
            
    

    @commands.command()
    async def draw(self,ctx,*,msg):
        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
        member_list = []
        for member in ctx.guild.members:
            
            if str(member.status) != "offline":
                # print(user)
                member_list.append(member)
        member_answer=choice(member_list)
        embed=discord.Embed(title="抽籤結果", description="輸入%draw <內容>來使用本功能", color=0xFF00FF, timestamp=dt) 
        php=member_answer.avatar_url
        embed.set_thumbnail(url=php)
        embed.set_footer(text=jdata["bot_name"], icon_url=jdata["bot_head_url"])
        embed.add_field(name=f"ID:{member_answer.id}", value=f"{member_answer.mention}", inline=False)
        embed.add_field(name="內容", value=msg, inline=False)
        rely=await ctx.message.reply(embed=embed, mention_author=False)
        await rely.add_reaction("🎉")
        await ctx.message.add_reaction("👍")
        await ctx.message.add_reaction("😈")
    
    @commands.command()
    async def drawall(self,ctx,*,msg):
        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
        member_list = []
        for member in ctx.guild.members:
            member_list.append(member)
        member_answer=choice(member_list)
        embed=discord.Embed(title="抽籤結果", description="輸入%draw <內容>來使用本功能", color=0xFF00FF, timestamp=dt) 
        php=member_answer.avatar_url
        embed.set_thumbnail(url=php)
        embed.set_footer(text=jdata["bot_name"], icon_url=jdata["bot_head_url"])
        embed.add_field(name=f"ID:{member_answer.id}", value=f"{member_answer.mention}", inline=False)
        embed.add_field(name="內容", value=msg, inline=False)
        rely=await ctx.message.reply(embed=embed, mention_author=False)
        await rely.add_reaction("🎉")
        await ctx.message.add_reaction("👍")
        await ctx.message.add_reaction("😈")

    @commands.command()
    async def ship(self,ctx,mem1:discord.Member = None,mem2:discord.Member = None):  #匹配程度
        mem1id=int(mem1.id)
        mem2id=int(mem2.id)
        if (mem1id==mem2id):
            dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
            dt = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
            embed=discord.Embed(title="匹配程度", description=f"<@!{mem1id}>和<@!{mem2id}>", color=0xffc0cb, timestamp=dt) 
            embed.set_thumbnail(url="https://i.imgur.com/gBwxhCl.jpg")
            embed.set_footer(icon_url=jdata["bot_head_url"],text=jdata["bot_name"])
            embed.add_field(name="100%", value="自己跟自己一定是親暱的", inline=False)
        else:
            num=random.randrange(101)
            dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
            dt = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
            embed=discord.Embed(title="匹配程度", description=f"<@!{mem1id}>和<@!{mem2id}>", color=0xffc0cb, timestamp=dt) 
            embed.set_thumbnail(url="https://i.imgur.com/gBwxhCl.jpg")
            embed.set_footer(icon_url=jdata["bot_head_url"],text=jdata["bot_name"])
            if(num>=70):
                embed.add_field(name=f"{num}%", value="恭喜!看來你們很親密呢", inline=False)
            elif(num>=40):
                embed.add_field(name=f"{num}%", value="雖然沒有很親密但還不錯", inline=False)
            elif(num>=10):
                embed.add_field(name=f"{num}%", value="有點慘喔", inline=False)
            else:
                embed.add_field(name=f"{num}%", value="永遠沒機會", inline=False)
            await ctx.send(embed=embed)
        await ctx.message.add_reaction("👍")

    @commands.command()
    async def confess(self,ctx,mem:discord.Member = None,*,msg):  #告白
        memid=int(mem.id)
        if (memid==ctx.message.author.id):
            await ctx.send(f"請不要自戀<@!{memid}>")
        else:
            await ctx.send(f'<@!{memid}>')
            dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
            dt = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
            embed=discord.Embed(title="告白時間", description=f"<@!{ctx.message.author.id}>向告白<@!{memid}>了", color=0xffc0cb, timestamp=dt) 
            embed.set_thumbnail(url="https://i.imgur.com/gBwxhCl.jpg")
            embed.set_footer(icon_url=jdata["bot_head_url"],text=jdata["bot_name"])
            embed.add_field(name="內容", value=msg, inline=False)
            await ctx.send(embed=embed)
    
    @commands.command()
    async def flirt(self,ctx,mem:discord.Member = None,*,msg):  #撩人
        memid=int(mem.id)
        if (memid==ctx.message.author.id):
            await ctx.send(f"撩自己有意義嗎?<@!{memid}>")
        else:
            await ctx.send(f'<@!{memid}>')
            dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
            dt = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
            embed=discord.Embed(title="撩人時間", description=f"<@!{ctx.message.author.id}>撩<@!{memid}>了", color=0xffc0cb, timestamp=dt) 
            embed.set_thumbnail(url="https://i.imgur.com/gBwxhCl.jpg")
            embed.set_footer(icon_url=jdata["bot_head_url"],text=jdata["bot_name"])
            embed.add_field(name="內容", value=msg, inline=False)
            await ctx.send(embed=embed)
   
    @commands.command()
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

    @commands.command()      #角子老虎機
    async def slot(self,ctx):
        num=[1,2,3,4,5,6,7,8,9]
        a=num[random.randrange(9)]
        b=num[random.randrange(9)]
        c=num[random.randrange(9)]
        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
        embed=discord.Embed(title="角子老虎機",  color=0xfff700, timestamp=dt) 
        embed.set_thumbnail(url="https://i.imgur.com/EybKWgR.png")
        embed.set_footer(icon_url=jdata["bot_head_url"],text=jdata["bot_name"])
        if(a==b and b==c and c==a):
            embed.add_field(name=f"[{a},{b},{c}]", value="恭喜你全中", inline=False)
        elif(a==b or b==c or c==a):
            embed.add_field(name=f"[{a},{b},{c}]", value="恭喜你中兩個", inline=False)
        else:
            embed.add_field(name=f"[{a},{b},{c}]", value="很遺憾你沒有中", inline=False)
        await ctx.send(embed=embed)
        await ctx.message.add_reaction("👍")
    
    @commands.command()
    async def fortune(self,ctx):
        an=["大凶","凶","吉","大吉"]
        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
        nu=random.randrange(4)
        embed=discord.Embed(title="占卜",  color=0xfff700, timestamp=dt)  
        ss=str(an[nu])
        embed.set_footer(icon_url=jdata["bot_head_url"],text=jdata["bot_name"])
        embed.add_field(name="結果", value=ss, inline=False)
        if(nu==0 or nu==1):
            embed.set_image(url="https://i.imgur.com/fsHNJMB.png")#凶
            embed.add_field(name="可惜了", value="下次加油", inline=False)
        else:
            embed.set_image(url="https://i.imgur.com/maN8fik.png") #吉
            embed.add_field(name="不錯喔", value="再接再厲", inline=False)
        await ctx.send(embed=embed)
        await ctx.message.add_reaction("👍")
    
    @commands.command()
    async def coin(self,ctx):
        pic=["https://i.imgur.com/1icSqAQ.png","https://i.imgur.com/rlvyUDA.png"]
        z=random.randrange(2)
        msg=str(pic[z])
        await ctx.send(msg)
        await ctx.message.add_reaction("👍")




def setup(bot):
    bot.add_cog(mesage(bot))