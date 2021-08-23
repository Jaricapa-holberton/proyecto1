#!/usr/bin/python3
"""
First prototype for scrap flats in Mercadolibre
"""

# failed to acces with webdriver
"""
from selenium import webdriver
# open firefox for selenium
driver = webdriver.Chrome('./chromedriver.exe')
url = "https://listado.mercadolibre.com.co/inmuebles/arriendo/valle-del-cauca/cali/#applied_filter_id%3Dcity%26applied_filter_name%3DCiudades%26applied_filter_order%3D2%26applied_value_id%3DTUNPQ0NBTDYyZDA0%26applied_value_name%3DCali%26applied_value_order%3D4%26applied_value_results%3D3152%26is_custom%3Dfalse"
driver.get(url)
"""

# using request
import requests
from bs4 import BeautifulSoup
web_page_url = "https://listado.mercadolibre.com.co/inmuebles/arriendo/valle-del-cauca/cali/#applied_filter_id%3Dcity%26applied_filter_name%3DCiudades%26applied_filter_order%3D2%26applied_value_id%3DTUNPQ0NBTDYyZDA0%26applied_value_name%3DCali%26applied_value_order%3D4%26applied_value_results%3D3152%26is_custom%3Dfalse"
# Add a User-Agent header to simulate a real web browser to send the requests. The User-Agent header should be saved in a dictionary object.
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}
# Make an HTTP get requests to the webserver by the requests module get method, and the get method returns a response object.
response = requests.get(url=web_page_url, headers=headers)
# Get the request web page text content by the response.text attribute
page_content = response.text
"""
# Write the web page content to a local file to save it
with open('./mercadolibre_aptos.html', 'w', encoding='utf8') as fw:
    fw.write(page_content)

# Open the local file with read permission.
with open('./mercadolibre_aptos.html', 'r', encoding='utf8') as fr:
    line = fr.readline() # read one line text.
    # Only when the read-out text's length is 0 then quit the loop.
    while len(line) > 0:
        print(line)
        # read the next line.
        line = fr.readline()
"""

# scrap and parse from the html page
soup = BeautifulSoup(page_content, 'lxml')
# the 'li' items with the class 'ui-search-layout__item' have the flats
# find the 'li' items with the class 'ui-search-layout__item'
all_house_li = soup.find_all("li", class_="ui-search-layout__item")
# find the images of the flats
# because of new internet protocols... after a few donwloads of some items
# the browser dont donwload the url from source, instead, just write were to find it
# if you want (see lazy-loadable for details)
# in Mercadolibre apears the real link in the key "data-src"
# So... to donwload images is required search on the 'src' and 'data-src' keys
idx1 = 0
list_img = []
while(idx1 < len(all_house_li)):
    try:
        img_url = all_house_li[idx1].find("img")['data-src']
        list_img.append(img_url)
    except:
        img_url = all_house_li[idx1].find("img")['src']
        list_img.append(img_url)
    idx1 += 1
print("###")
print(len(list_img))
# find the price of the flats
idx2 = 0
list_prices = []
while(idx2 < len(all_house_li)):
    price = str(all_house_li[idx2].find(class_="price-tag-fraction").text)
    price = int(price.replace('.', ''))
    list_prices.append(price)
    idx2 += 1
print("###")
print(list_prices)
# find the title ads of the flats
idx3 = 0
list_titles = []
while(idx3 < len(all_house_li)):
    title = str(all_house_li[idx3].find(class_="ui-search-item__title").text)
    list_titles.append(title)
    idx3 += 1
print("###")
print(list_titles)
# find the locations of the flats
idx4 = 0
list_locations = []
while(idx4 < len(all_house_li)):
    location = str(all_house_li[idx4].find(class_="ui-search-item__group__element ui-search-item__location").text)
    list_locations.append(location)
    idx4 += 1
print("###")
print(list_locations)
# because the area and rooms share the same class... i made two list indepently for save the data
# but, i first required split the two elements
# find the area and the number of rooms of the flats
idx5 = 0
list_area = []
list_rooms = []
while(idx5 < len(all_house_li)):
    array_loc_rooms = all_house_li[idx5].find_all(class_="ui-search-card-attributes__attribute")
    area = "NA"
    rooms = "NA"
    # save the areas
    if(len(array_loc_rooms) > 0):
        just_meters = str(array_loc_rooms[0].text)
        just_meters = just_meters.split()
        area = just_meters[0]
        area = int(area.replace(',', ''))
    # save the number of rooms
    if (len(array_loc_rooms) == 2):
        just_rooms = str(array_loc_rooms[1].text)
        just_rooms = just_rooms.split()
        rooms = int(just_rooms[0])
    list_area.append(area)
    list_rooms.append(rooms)
    idx5 += 1
print("###")
print(list_area)
print("###")
print(list_rooms)
# find the url of the flats
idx6 = 0
list_url = []
while(idx6 < len(all_house_li)):
    urls = str(all_house_li[idx6].find("a")["href"])
    list_url.append(urls)
    idx6 += 1
print("###")
print(len(list_url))
