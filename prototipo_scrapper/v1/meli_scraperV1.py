#!/usr/bin/python3
"""
First prototype for scrap house in Mercadolibre
"""
#https://www.youtube.com/watch?v=w04Vi54pSxo&t=3116s
import app_conection_sql

# paser for the location string to split adress, city and region
def get_address(data):
    part = data.split(',')
    partAmount = len(part)
    if(partAmount == 3):
        return {'address': part[0], 'city': part[1], 'region': part[2]}
    elif(partAmount > 3):
        return {'address': " ".join(part[:len(part)-3]), 'city': part[partAmount-2], 'region': part[partAmount-1]}
    elif(partAmount < 3):
        for i in range(0, 100):
            print("error: ")
            print(data)
            return {'address': 'NA', 'city': 'NA', 'region': 'NA'}

# get the data of the house and convert it as object
def house_li_html_to_obj(house_li_html):
        # find the images of the house
        # because of new internet protocols... after a few donwloads of some items
        # the browser dont donwload the url from source, instead, just write were to find it
        # if you want (see lazy-loadable for details)
        # in Mercadolibre apears the real link in the key "data-src"
        # So... to donwload images is required search on the 'src' and 'data-src' keys
        img = house_li_html.find("img")
        try:
            img_url = img['data-src']
        except:
            img_url = img['src']
        # find the price of the house
        price = str(house_li_html.find(class_="price-tag-fraction").text)
        price = int(price.replace('.', ''))
        # find the title ads of the house
        title = str(house_li_html.find(class_="ui-search-item__title").text)
        # find the locations of the house
        address = str(house_li_html.find(class_="ui-search-item__group__element ui-search-item__location").text)
        address = get_address(address)
        # because the area and rooms share the same class... i made two list indepently for save the data
        # but, i first required split the two elements
        # find the area size and the number of rooms of the house
        all_attributes = house_li_html.find_all(class_="ui-search-card-attributes__attribute")
        area_size = "NA"
        rooms = "NA"
        # save the areas
        if(len(all_attributes) > 0):
            just_meters = str(all_attributes[0].text)
            just_meters = just_meters.split()
            area_size = just_meters[0]
            area_size = int(area_size.replace(',', ''))
        # save the number of rooms
        if (len(all_attributes) == 2):
            just_rooms = str(all_attributes[1].text)
            just_rooms = just_rooms.split()
            rooms = int(just_rooms[0])
        # find the url of the house
        urls = str(house_li_html.find("a")["href"])
        # return the object
        return {"img_url" : img_url, "price" : price, "title" : title, 
        "address" : address['address'], "city" : address['city'], 
        "region" : address['region'], "area_size" : area_size, 
        "rooms" : rooms, "urls" : urls}
        

if __name__ == "__main__":
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
    # scrap and parse from the html page
    soup = BeautifulSoup(page_content, 'lxml')
    # the 'li' items with the class 'ui-search-layout__item' have the house
    # find the 'li' items with the class 'ui-search-layout__item'
    all_house_li = soup.find_all("li", class_="ui-search-layout__item")
    # print every house parsed from the url
    idx0 = 0
    while(idx0 < len(all_house_li)):
        house_obj = house_li_html_to_obj(all_house_li[idx0])
        app_conection_sql.insert_house(house_obj)
        idx0 += 1
