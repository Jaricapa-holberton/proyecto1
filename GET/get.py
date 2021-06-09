#!/usr/bin/python3
import requests

url = "https://jsonplaceholder.typicode.com/posts"

r = requests.get(url)

data = r.json()

print(data)