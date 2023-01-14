import requests
from bs4 import BeautifulSoup
import os
import json

payload={
    "username": "",
    "password": ""
}

filename = "database.json"

if not os.path.exists(filename):
    open(filename, "w").close()

data_list = []

with requests.Session() as s:
    p = s.post('https://my.cis.edu.sg/login/', data=payload)
    for _id in range(20000, 29000): #29000
        try:
            url = "https://my.cis.edu.sg/search/user/"+str(_id) 
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
            
            n = data.split('.')[3].split('Position')[0][:-32]

            data = {
                "id": _id,
                "position_title": pt,
                "email": e,
                "name": n
            }
            data_list.append(data)
        except:
            pass

with open(filename, "w") as outfile:
    json.dump(data_list[0], outfile)
    outfile.write('\n')
    for i in range(1, len(data_list)):
        json.dump(data_list[i], outfile)
        outfile.write('\n')
