import requests
import json

token = input("Token: ")

header_payload = {
    'Authorization' : token,
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
}

r = requests.get('https://discord.com/')
cookie_payload = {
    '__cfduid' : r.cookies['__cfduid'],
}

r = requests.get('https://discordapp.com/api/v6/users/@me/relationships',cookies=cookie_payload,headers=header_payload)

response_data = json.loads(r.text)

for i in response_data:
    if i['type'] == 2:
        try:
            print(i['user']['username']+"#"+i['user']['discriminator']) 
        except:
            pass
