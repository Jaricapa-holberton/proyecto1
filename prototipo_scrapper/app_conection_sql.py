#!/usr/bin/python3
"""
First prototype for scrap flats in Mercadolibre
"""
import pymysql

""" house = {"img_url" : img_url, "price" : price, "title" : title, 
        "address" : address['address'], "city" : address['city'], 
        "region" : address['region'], "area_size" : area_size, 
        "rooms" : rooms, "urls" : urls} """

# Connect to the database
def get_connection():
    connection = pymysql.connect(host='localhost',
                                user='root',
                                # the actual config of mysql dont need the pass option, in fact, fails if was gived in the command
                                #password='root',
                                database='meli_schema',
                                cursorclass=pymysql.cursors.DictCursor)

def create_table_meli_houses():
    conn = get_connection()
    create_table_user = "CREATE TABLE IF NOT EXISTS `meli_schema`.`mercadolibre_houses` (`idmercadolibre_houses` INT NOT NULL, `img_url` VARCHAR(300) NULL, `price` INT(20) NULL, `title` VARCHAR(200) NULL, `address` VARCHAR(100) CHARACTER SET `utf8` NULL, `city` VARCHAR(50) NULL, `region` VARCHAR(50) NULL, `area_size` INT(20) NULL, `rooms` INT(20) NULL, `urls` VARCHAR(300) NULL, PRIMARY KEY (`idmercadolibre_houses`), UNIQUE INDEX `idmercadolibre_houses_UNIQUE` (`idmercadolibre_houses` ASC) VISIBLE);"
    db_cursor = conn.cursor()
    db_cursor.execute(create_table_user)
    db_cursor.close()
    conn.close()

https://www.youtube.com/watch?v=xJzu7BlpqSc
INSERT INTO `meli_schema`.`mercadolibre_houses`