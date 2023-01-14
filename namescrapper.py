import requests
from bs4 import BeautifulSoup

url = "https://my.cis.edu.sg/resource/all/search?keyword=shaun&type=all&p=1"

payload={
    "username": "",
    "password": ""
}

name = 'lucas'
index = []

with requests.Session() as s:
    p = s.post('https://my.cis.edu.sg/login/', data=payload)
    r = s.get("https://my.cis.edu.sg/resource/user/search?keyword="+name+"&type=user&p=1")
    soup = BeautifulSoup(r.content, "html.parser")
    for i in soup.find_all('a'):
        index.append(i)
    for a in index:
        id = a["href"].split("/user/")[1]
        url = "https://my.cis.edu.sg/search/user/"+id 
        r = s.request("GET", url)
        soup = BeautifulSoup(r.text, 'html.parser')
        data = str(soup.getText().encode("utf-8"))

        data = data.replace("\n", "")

        pt = None
        e = None
        
        if "Title" in data:
            indexs = data.index("Email:")-40
            for i in range(50):
                if (data[indexs-i]) == " " and (data[indexs-i-1]) == " ":
                    pt = data[indexs-i:indexs]
                    break

        if "Email:" in data:
            endindex = data.index("2023")-52
            for i in range(50):
                if (data[endindex-i]) == ":" and (data[endindex-i-1]) == "l":
                    e = data[endindex-i+5:endindex]
                    break

        n = a.getText().replace("\n", "")

        data = {
            "position_title": pt,
            "email": e,
            "name": n
        }
        print(data, id)

            
