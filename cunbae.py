import discord, datetime, asyncio, random, re, command
from Dtime import Uptime
intents = discord.Intents.all()
token = "Nzc1NjE1OTYwOTcwNTU5NDg4.X6o6pw.YhJwrHMIGrb_mXMJ2xYdFIouejw" #봇 토큰 설정하기
client = discord.Client(intents=intents) #client 설정하기



@client.event
async def on_ready(): #봇이 준비되었을때
    print("the bot is started.")
    print(client.user)
    print("============================")
    print("봇이 들어가있는 서버")
    import asyncio
    await client.change_presence(status=discord.Status.offline)
    game = discord.Game("으아아아아아앙아")
    guild_list = client.guilds
    for i in guild_list:
        print("서버 ID: {} / 서버 이름: {}".format(i.id, i.name)) 
    await client.change_presence(status=discord.Status.online, activity=game)
    user = len(client.users)
    server = len(client.guilds)
    message = ["춘배를 쓰는 유저 수는 " + str(user) + "명이에요!","춘배가 있는 서버는 " + str(server) + "개에요!"]
    while True:
        await client.change_presence(status=discord.Status.online, activity=discord.Game(message[0]))
        message.append(message.pop(0))
        await asyncio.sleep(4)


@client.event
async def on_message(message): #사용자가 메세지를 입력했을때
    if message.content == "춘배야": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("왜 부르시오? :thinking: ") #봇이 "ㅂㅇ" 라고 답한다.    
    if message.content == "춘배야 ㅗ": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("왜 엿을쓰시오 ㅠㅠ 실망이오 :sob:") #봇이 "ㅂㅇ" 라고 답한다.    
    if message.content == "춘배야 안녕": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("안녕하시오 춘배요 :wave:") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "춘배야 ㅎ2": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("안녕하시오 춘배요 :wave:") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "춘배야 ㅎㅇ": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("안녕하시오 춘배요 :wave:") #봇이 "ㅂㅇ" 라고 답한다. 
    if message.content == "춘배야 하이": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("안녕하시오 춘배요 :wave:") #봇이 "ㅂㅇ" 라고 답한다.    
    if message.content == "춘배 ㅎㅇ": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("안녕하시오 :wave:") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "춘배야 밥해줘": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("싫소 :x:") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "춘배야 밥줘": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("싫소 :x:") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "춘배야 밥": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("난 밥이아니오") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "춘배야 민초": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("호불호 갈리는 음식 이오") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "춘배야 민초": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("맛있는 음식이오") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "춘배야 1학년7반": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("역시 킹갓7반^^") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "춘배야 쮸쮸": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("트롤이니 조심하시오") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "춘배야 ㅗㅜㅑ": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("음란마귀가 단단이 꼈소") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "춘배야 동하": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("음......어.....음....") #봇이 "ㅂㅇ" 라고 답한다
    if message.content == "춘배야 코로나19": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("나는 코로나 싫소") #봇이 "ㅂㅇ" 라고 답한다
    if message.content == "춘배야 이현민": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("나의 창조자의 절친이오") #봇이 "ㅂㅇ" 라고 답한다
    if message.content == "춘배야 백지연 선생님": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("폭력적이니 주의하시오") #봇이 "ㅂㅇ" 라고 답한다
    if message.content == "춘배야 잘자": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("당신도 잘자시오") #봇이 "ㅂㅇ" 라고 답한다
    if message.content == "춘배야 좋은꿈꿔": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("고맙소") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "춘배야 김진용": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("공부를 잘하는 사람이오") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "춘배야 남자야 여자야?": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("웹툰 보시오") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "춘배야 너의 창조자는 누구야?": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("백규승 이라는 아주 멋진분이오") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "춘배야 이스터에그": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("https://youtu.be/SHLIFx_Selw") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "춘배야 사랑해": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("나도 사랑하오ㅎㅎ") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "춘배야 배불러": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("배부르면 나의 음식은 못먹겠구려 ㅠㅠ") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "춘배야 너 냥패 어딨어?": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("그건 알려줄수 없소") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "으악핑":  #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("그거좀 그만해라고!!")#봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "@김춘배": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("왜부르시오?") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "춘배야 뭐해?": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("우리 창조주를 창양하고 있었소")
    if message.content == "춘배야 뭐해": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("우리 창조주를 창양하고 있었소") 
    if message.content == "춘배야 머해?": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("우리 창조주를 창양하고 있었소") 
    if message.content == "춘배야 머해": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("우리 창조주를 창양하고 있었소")
    if message.content == "춘배야 백규승": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("백규승은 나를 창조하신 멋진 분이오") #봇이 "ㅂㅇ" 라고 답한다.    if message.content == "백규승": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
    if message.content == "백규승": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("우리 창조주 왜부르는거요!!")
    if message.content == "춘배야 정주원": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("씨발 나 흑화함 그 개새끼왜부름? 왜 나한태서 찾냐고 존나 이기적인 개새기")
    if message.content == "춘배야 깔대기 대가리": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("씨발 나 흑화함 그 개새끼왜부름? 왜 나한태서 찾냐고 존나 이기적인 개새기")
    if message.content == "춘배야 깔대기대가리": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("씨발 나 흑화함 그 개새끼왜부름? 왜 나한태서 찾냐고 존나 이기적인 개새기")
    if message.content == "춘배야 가정서": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("ㅘ 정서 머단하오")
    
    
    
    
    if message.content == "춘배야 내정보":
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{message.author.mention}의 가입일 : {date.year}/{date.month}/{date.day}")
        await message.channel.send(f"{message.author.mention}의 이름 / 아이디 / 닉네임 : {user.name}/{user.id}/{user.display_name}")
        await message.channel.send(message.author_url)




    if message.content == "핑":
        la = client.latency
        await message.channel.send(f'퐁 {str(round(la * 1000))}ms')


    if message.content.startswith("clean"):
        number = not number.isdecimal(message.content.split(" ")[1])
        await message.delete()
        await message.channel.pruge(linmit=number)
        a = await message.channel.send("읍읍")
        await asyncio.sleep(2)
        await a.delete()




    if  message.content == "춘배야 창조주 컴사양":
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.blurple(), title="창조주님의 컴사양이오", description=" ")
        embed.set_image(url="https://cdn.discordapp.com/attachments/749248180272758795/775675969011712010/cats.jpg")
        await message.channel.send(embed=embed)





    if message.content == "춘배와 나의 우정 점수":
        await message.channel.send(random.randint(1, 100))
    
    if message.content == "라면 꼬들면 타이머":
        await message .channel.send("알았오 좀있다 알려주겠소")
        await asyncio.sleep(270)
        await message.channel.send(f"{message.author.mention}, 라면 다됬소")

    if message.content == "라면 퍼진면 타이머":
        await asyncio.sleep(300)
        await message.channel.send(f"{message.author.mention}, 라면 다됬소")

    if message.content == "춘배야추천음식":
        r = ["치킨", "짜장면", "피자", "국수","밥", "걍 처먹지마"]
        embed=discord.Embed(color=0x000000, title=f"추천음식", description=random.choice(r))
        await message.channel.send(embed=embed)


    if message.content == '춘배야 업타임':
        uptime = str(Uptime.uptime()).split(":")
        hours = uptime[0]
        minitues = uptime[1]
        seconds = uptime[2].split(".")[0]
        await message.channel.send(f"{hours}시간 {minitues}분 {seconds}초")




    if message.content.startswith("!청소"):
        if message.content == '!청소':
            await message.channel.send(f"{message.author.mention} ,  \n그래서 몇 개를 치우라고요?\n올바른 명령어는 `!청소 (숫자)` 에요..!")
        else:
            if message.author.guild_permissions.administrator:
                number = int(message.content.split(" ")[1])
                await message.delete()
                await message.channel.purge(limit=number)
                a = await message.channel.send(f"{message.author.mention} ,  \n{number}개의 메시지를 삭제했습니다.\n(이 메시지는 잠시 후에 삭제됩니다.)")
                await asyncio.sleep(2)
                await a.delete()
            else:
                await message.channel.send(f"{message.author.mention} ,  \n명령어를 수행할 관리자 권한을 소지하고 있지 않습니다.")




    if message.content == "춘배야 나 뭐할까?":
        r = ["유로트럭", "잼민크레프트", "옵치", "그타","왓챠", "넷플", "반로란트"]
        embed=discord.Embed(color=0x000000, title=f"할만한거", description=random.choice(r))
        await message.channel.send(embed=embed)


    if message.content.startswith('춘배야타이머'): # `!타이머` 라는 메시지를 받았을 때
        if message.content == '춘배야타이머': # 만약 메시지가 숫자 없이 `!타이머` 만 있다면
            await message.channel.send(f"{message.author.mention} \n그래서 몇 초를 맞출지 정해주시오\n올바른 명령어는 `!타이머 (숫자(초))` 이오!") # 몇 초를 맞추라는지 출력한다.
        else: #그렇지 않다면
            timer = int (message.content.split(" ")[1]) # 타이머를 숫자만큼 지정한다.
            await message.channel.send(f"{message.author.mention} ,\n타이머가 설정되었소.\n시간이 끝나면 맨션해드리겠소") # 설정 완료 메시지를 보낸다.
            await asyncio.sleep(timer) # 그 숫자만큼 대기한다.
            await message.channel.send(f"{message.author.mention} ,\n타이머가 끝났소!") # 타이머가 끝났음을 알린다.

    if message.content.startswith(".주사위"):
        embed=discord.Embed(title="랜덤 주사위",description=':game_die: :one:')
        embed1=discord.Embed(title="랜덤 주사위",description=':game_die: :two:')
        embed2=discord.Embed(title="랜덤 주사위",description=':game_die:  :three:')
        embed3=discord.Embed(title="랜덤 주사위",description=':game_die: :four:')
        embed4=discord.Embed(title="랜덤 주사위",description=':game_die: :five:')
        embed5=discord.Embed(title="랜덤 주사위",description=':game_die: :six:')
        random_list = [embed, embed1, embed2, embed3, embed4, embed5]
        embed = random.choice(random_list)
        await message.channel.send(embed=embed)



    if message.content.startswith('!킥'):
        if message.author.guild_permissions.administrator:
            member = message.guild.get_member(int(message.content[3:21]))
            git = message.content[22:]
            await message.guild.kick(member)       
            embed = discord.Embed(title="사유\n"+git, description=None, color=0x00afff)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send("권한이 없습니다.")
        
    if message.content.startswith('!밴'):
        if message.author.guild_permissions.administratorr:        
            member = message.guild.get_member(int(message.content[3:22]))
            git = message.content[22:]
            await message.guild.ban(member)       
            embed = discord.Embed(title="사유\n"+git, description=None, color=0x00afff)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send("권한이 없습니다.") 


    if message.content.startswith(".정보"):
        status = str(message.author.status)
        if status == "online":
            status = "온라인🟢"
        elif status == "dnd":
            status = "방해금지⛔"
        elif status == "idle":
            status = "자리비움🟡"
        else:
            status = "오프라인⚪"
        if message.author.bot == False:
            bot = "유저"
        else:
            bot = "봇"
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(title=f'{message.author.name}의 정보')
        embed.add_field(name="이름", value=message.author.name, inline=False)
        embed.add_field(name="별명", value=message.author.display_name)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=False)
        embed.add_field(name="아이디", value=message.author.id)
        embed.add_field(name="상태", value=f"{status}", inline=False)
        embed.add_field(name="최상위 역할", value=message.author.top_role.mention, inline=False)
        embed.add_field(name="봇", value=bot)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)




    



    if message.content == "!가위바위보 가위" or message.content == "!가위바위보 바위" or message.content == "!가위바위보 보":
        random_ = random.randint(1, 3)

        if random_ == 1:
            if message.content == "!가위바위보 가위":
                await message.channel.send(f"{message.author.mention}님은 가위, 저도 가위! 비겼습니다.")
            elif message.content == "!가위바위보 바위":
                await message.channel.send(f"{message.author.mention}님은 바위, 저는 가위! {message.author.mention}님이 이겼습니다.")   
            elif message.content == "!가위바위보 보":
                await message.channel.send(f"{message.author.mention}님은 보, 저는 가위! 제가 이겼습니다.")   
        elif random_ == 2:
            if message.content == "!가위바위보 가위":
                await message.channel.send(f"{message.author.mention}님은 가위, 저는 바위! 제가 이겼습니다.")
            elif message.content == "!가위바위보 바위":
                await message.channel.send(f"{message.author.mention}님은 바위, 저도 바위! 비겼습니다.")   
            elif message.content == "!가위바위보 보":
                await message.channel.send(f"{message.author.mention}님은 보, 저는 바위! {message.author.mention}님이 이겼습니다.")
        elif random_ == 3:
            if message.content == "!가위바위보 가위":
                await message.channel.send(f"{message.author.mention}님은 가위, 저는 보! {message.author.mention}님이 이겼습니다.")
            elif message.content == "!가위바위보 바위":
                await message.channel.send(f"{message.author.mention}님은 바위, 저는 보! 제가 이겼습니다.")   
            elif message.content == "!가위바위보 보":
                await message.channel.send(f"{message.author.mention}님은 보, 저도 보! 비겼습니다.")

        




















client.run(token)
