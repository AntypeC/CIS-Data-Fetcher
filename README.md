# CIS-Data-Retriever
A live bot is hosted currently, and can be invited to a server by following this link: https://discord.com/api/oauth2/authorize?client_id=1064070252306120765&permissions=8&scope=bot

To enable web scraping, enter the username and password at https://my.cis.edu.sg/login/ to the payload in main.py.
```
payload={
    "username": "example@cis.edu.sg",
    "password": "example_password"
}
```

Enter the discord bot token to enable on the script on Discord. 
```
client.run("MTAxMDQxNzk1NTExNDDdDA3OA.Ge_aos.E3LTKkrxv7RktFt3ZpYxYzfw6U1JtdgBXQa8")
```

To get started, run (on Darwin):
```
# create & activate a virtual environment
python3 -m venv env
source env/bin/activate
# install the dependencies
pip install -r requirements.txt
# run
python3 main.py
```
Usage: 
```!find <firstname> <lastname>```
```!searchclass <grade>```

To store student data locally in database.json, run dbupdater.py (required for ```!searchclass``` function).
