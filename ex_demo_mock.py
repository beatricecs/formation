import requests
import prettyprinter
from dataclasses import dataclass

@dataclass
class User:
    gender: str
    title: str
    firstname: str
    lastname: str
    email: str
    username: str

def
response = requests.get('https://randomuser.me/api/')

#print(response.status_code)
result = response.json()

prettyprinter.cpprint(result)
#print(result)


record = result['results'][0]
record_name = record['name']
record_login = record['login']
#print (record['gender'],
#       record_name['title'],
#       record_name['first'],
#       record_name['last'],
#       record['email'],
#       record_login['username']
#       )
user = User(record['gender'],record_name['title'], record_name['first'],
            record_name['last'],record['email'],record_login['username']
            )

print(user.firstname)
