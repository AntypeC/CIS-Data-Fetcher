import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import random

payload={
    "username": "",
    "password": ""
}

payload2={
    
}

#https://cissg.managebac.com/student/timetables
mb_header1 = {
  'authority': 'cissg.managebac.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'accept-language': 'es-ES,es;q=0.9,en;q=0.8,zh-TW;q=0.7,zh;q=0.6',
  'cache-control': 'max-age=0',
  'cookie': '__utmz=58354037.1661010968.4.2.utmcsr=lucamehl.netlify.app|utmccn=(referral)|utmcmd=referral|utmcct=/; _gcl_au=1.1.653633245.1661013225; _fbp=fb.1.1661013224952.1940194090; messagesUtk=8d4e973fce6e4440a18925334a9a3d46; __hstc=58354037.4098ab289c19b5028aa3300d659a98c9.1661013227559.1661013227559.1661013227559.1; hubspotutk=4098ab289c19b5028aa3300d659a98c9; intercom-id-jm2sktyg=acc6f3c8-a4b8-487e-b84a-6ac07f27a3eb; _ga_LF1CBJ6YGW=GS1.1.1661013224.1.1.1661013273.0.0.0; _ga_SW993313D5=GS1.1.1661013224.1.1.1661013273.0.0.0; _ga_PRJ8C9EXQR=GS1.1.1661013224.1.1.1661013273.0.0.0; _ga_F6FP8X4R65=GS1.1.1661013224.1.1.1661013273.0.0.0; _ga=GA1.2.1837622448.1661013225; cf_clearance=1oQ7bGobUQ9oE7NU0_NLY1J3T3Skgso7rAhHHJq_EbA-1661583137-0-150; __utma=58354037.2067564641.1653992567.1661010968.1663663448.5; _managebac_session=CxTMRoL9oWYA0jRKSWndSPwGx92IltP8FxOsPdT5ifXyO0iz325wShSe6%2FINrLuNDP8p1VmDSo80FdSAWRdffKPXIYOYNcroIbZA1bWev%2BFZVRHE67zYX2CQs6EWXPHMFCRSh%2FUdKQK2qRP%2FbxAKjaSosDEB%2BCPV8%2FbrmkSV4tWiV8i441QVTgtrZ1OYH1TqnT6XPIkVwPTEvhyTgzpdSjfdpzSyDdCKeKqlJMSO%2Brr2uLTCM9UtuyELVohA30V2qzqWYnHV40z3zqpqp%2FD%2B5m51XV%2FYsw6GGIIkbtSqTUpNExaNNeiUVt7ChVDGcddpcohUKgWIWLEYEbnOUWv2sFx9RasZ%2FnB20JFjvjTYOaFYVBwGTA7XBB3zg%2F2E3bZyvDZY6z1k1FqncMtzgk1jZBooZFgJ1gv%2By3o5tO27dFuynUXEqXva6bGgmxn0CNpB27rpvaG6dp7jmKrwnItlPxrkPm9H00bcVxYQ2peC6yE9kh4LnSdavNcyXq3AU30j%2BYL%2Fs4xHefD3p%2FRhpCnyLEf7zIeUW4%2F4bfLFP%2BqPN8iHD6WUB%2BQt4QsvUtLiyDoy--0aC2zuxZeCc5WkuY--UGUx8BZezG7UzDAwN5q1yg%3D%3D; _managebac_session=7zHA0EwVyzTNFmrE009lRjy%2BxNUy6wxqRj7nUJC4dbGy5LMz8qB8vqf87DAT5L2UFIdSaS9fRjKV9ULjiBGPO1CDvgmF0%2FilQRrnLkFJdhvWJFfd2br1AJtMgqGharpZAyVQuhx07fAuYE2mDz9P7CQ%2FTm5OGVoGpJeld5tK99zwOATwyYFADmzlXem1mg1O7s7BLtIoiPWp%2BRs6rP6qm%2Fgu57qJ1vqu%2B0RIXGc1wZYYDs%2BPiz8aTSX5YYE0L7yg5aP3UG5N1npckUtJIJGTOWxMokLEnCN7dXgImDqxELgjwOr2izvP6i7x9vqnyD0dXHkgX3Dqnb1QofpY8w2BQs7Bj%2FeIuGalD%2BRHTggXkfPQTQQIHPxiPtKjODCits0meBOXJ70Wl%2Bzh5rgwPZuKu%2FrZNXSmtTkW0MQikDMpfqNGP5aeukkKJ7CPYlKlveeybv6rB4bCdvJgKhZbSBDhBjQpc9KRIgETs%2BYN1bunmyb4y7a%2FW294OYnZFqF6j2DkKdPOg%2FEpVI1%2F62w1BfI%2B32B9riN0iOIHf9D10M%2FSJGmtAHryF1HHBp6Ao7uiihQG--yM8GHSlYIuHMhUCJ--PToIaOzb0KXc2WSOrKDh9w%3D%3D',
  'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

def login():
    global s, r
    login_url = "https://my.cis.edu.sg/login/"
    s = requests.session()
    r = s.get(login_url)
    r = s.post(login_url, data=payload, headers=dict(referer=login_url))

def getStudentData(name):
    global index, data, ids
    index = []
    data = []
    ids = []
    r = s.get("https://my.cis.edu.sg/resource/user/search?keyword="+name+"&type=user&p=1")
    soup = BeautifulSoup(r.content, "html.parser")
    for i in soup.find_all('a'):
        index.append(i)
    for a in index:
        _id = a["href"].split("/user/")[1]
        url = "https://my.cis.edu.sg/search/user/"+_id 
        r = s.request("GET", url)
        soup = BeautifulSoup(r.text, 'html.parser')
        scrapped = str(soup.getText().encode("utf-8"))
        scrapped = scrapped.replace("\n", "")

        pt = None
        e = None
        
        if "Title" in scrapped:
            indexs = scrapped.index("Email:")-40
            for i in range(50):
                if (scrapped[indexs-i]) == " " and (scrapped[indexs-i-1]) == " ":
                    pt = scrapped[indexs-i:indexs]
                    break

        if "Email:" in scrapped:
            endindex = scrapped.index("2023")-52
            for i in range(50):
                if (scrapped[endindex-i]) == ":" and (scrapped[endindex-i-1]) == "l":
                    e = scrapped[endindex-i+5:endindex]
                    break

        n = a.getText().replace("\n", "")

        scrapped = {"position_title": pt, "email": e, "name": n}
        data.append(scrapped)
        ids.append(_id)

def getStudentPortrait(id):
    url = "https://my.cis.edu.sg/portrait.php?id="+id+"&size=constrain200"
    img = s.get(url, headers=dict(referer=url))
    f= open("image.png", "wb")
    f.write(img.content)
    f.close

def get_class_data(name):
    r = requests.get("https://cissg.managebac.com/student/timetables", headers=mb_header1)
    soup = str(BeautifulSoup(r.content, 'html.parser').getText()).split('Classes')[2].split('\n\n\n\n')
    classes = []
    for i in range(1, 7):
        classes.append(soup[i])
    return classes

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!", intents=intents, activity=discord.Game(name=random.choice(['Minecraft', 'Grand Theft Auto V', 'Roblox', 'League of Legends', 'PUBG: Battlegrounds'])))

@client.event
async def on_ready():
    print('Logged on as', client.user)

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content == '!help':
#         await message.channel.send('!findstudent <name>')

#     await client.process_commands(message)

@client.event
async def onCommandError(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        em = discord.Embed(title=f"Error!", description=f"Command not found.", color=ctx.author.color) 
        await ctx.send(embed=em)

@client.command()
async def find(ctx, firstname=None, lastname=''):
    login()
    if firstname!=None:
        fullMatch = False
        count = 0
        _count = -1
        getStudentData(firstname)

        for dict in data:
            _count += 1
            fullname = dict["name"].lower().split()
            if fullname[1]+" "+fullname[-1]=="{} {}".format(firstname.lower(), lastname.lower()):
                fullMatch = True
                break
            else:
                print(fullMatch)
                print(_count)
                print(data[_count]["name"])
                print(fullname[1]+" "+fullname[-1])

        if fullMatch == False:
            for dict in data:
                getStudentPortrait(ids[count])
                embed=discord.Embed(title=dict["name"], description="""
                {}
                {}
                """.format(dict["position_title"], dict["email"]))
                embed.set_author(name="CIS Data Retriever", url="https://my.cis.edu.sg/")
                file = discord.File("image.png")
                embed.set_image(url="attachment://image.png")
                await ctx.send(file=file, embed=embed)
                count += 1

        else:
            getStudentPortrait(ids[_count])
            embed=discord.Embed(title=data[_count]["name"], description="""
            {}
            {}
            """.format(data[_count]["position_title"], data[_count]["email"]))
            embed.set_author(name="CIS Data Retriever", url="https://my.cis.edu.sg/")
            file = discord.File("image.png")
            embed.set_image(url="attachment://image.png")
            await ctx.send(file=file, embed=embed)
    else:
        msg = '`{}`'.format('Error! Expected a <firstname> <lastname>.')
        await ctx.send(msg)

@client.command()
async def myclasses(ctx):
    classes = get_class_data(name="")
    embed=discord.Embed(title="Your Classes", description="""
    {}
    {}
    {}
    {}
    {}
    {}
    """.format(classes[0], classes[1], classes[2], classes[3], classes[4], classes[5]))
    embed.set_author(name="CIS Data Retriever", url="https://cissg.managebac.com/student/timetables")
    await ctx.send(embed=embed)

client.run("")
