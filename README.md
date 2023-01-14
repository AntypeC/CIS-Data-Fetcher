# CIS-Data-Fetcher
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
Usage: ```!find <firstname> <lastname>```

To store student data locally in database.json, run dbupdater.py.
