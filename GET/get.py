#!/usr/bin/python3
import requests

ses = requests.session()

payload = {
    'id':'2241',
    'holdthedoor':'Enviar'
}

response = ses.post(url="http://158.69.76.135/level0.php",data=payload)

print(response.status_code)
print("============")
print(response.content)


