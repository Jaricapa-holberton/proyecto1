#!/usr/bin/python3
import urllib.request
import json

limit = 2

url_base = "https://jsonmock.hackerrank.com/api/articles?page="
num_pg = 1
art_list = []
num_list = []
url = str(url_base + str(num_pg))
operUrl = urllib.request.urlopen(url)
if(operUrl.getcode()==200):
    data = operUrl.read()
    jsonData = json.loads(data)
else:
    print("Error receiving data", operUrl.getcode())
data_page = jsonData.get('data')
idx1 = 0
while idx1 < len(data_page):
    dict_to_check = data_page[idx1]
    check_title = str(dict_to_check.get('title'))
    check_story = str(dict_to_check.get('story_title'))
    if dict_to_check.get('num_comments') == None:
        check_comments = int(0)
    else:
        check_comments = int(dict_to_check.get('num_comments'))
    if check_title != "None":
        art_list.append(check_title)
        num_list.append(check_comments)
    elif check_story != "None":
        art_list.append(check_story)
        num_list.append(check_comments)
    else:
        continue
    idx1 += 1
dict_titles = dict(zip(num_list, art_list))
best_com = sorted(num_list)
best_best = best_com[len(best_com) - limit : len(best_com)]
sort_sort = []
num1 = 0
num2 = -1
while num1 <= len(best_best):
    print(best_best[num2])
    num2 -= 1
idx3 = 0
print(dict_titles)
print(sort_sort)
titless = []
while idx3 < len(sort_sort):
    titless.append(dict_titles[sort_sort[idx3]])
    idx3 += 1
print(titless)
