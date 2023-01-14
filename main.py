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
