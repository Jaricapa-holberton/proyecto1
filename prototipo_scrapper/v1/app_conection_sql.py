#!/usr/bin/python3
"""
dbDao to connect the user's queries to the database
"""
import pymysql
import config

# https://www.youtube.com/watch?v=xJzu7BlpqSc

# Connect to the database
def get_connection():
    connection = pymysql.connect(**config.bd_connection_data)
    return connection

# execute every query required
def query_execute(query, params = ""):
    db_conn = get_connection()
    db_cursor = db_conn.cursor()
    if (params == ""):
        db_cursor.execute(query)
    else:
        db_cursor.execute(query, params)
    db_cursor.close()
    db_conn.commit()
    db_conn.close()
    return 1

# create the table data
def create_table_meli_houses():
    create_table_user = "CREATE TABLE IF NOT EXISTS `meli_schema`.`mercadolibre_houses` (`id_house` INT NOT NULL AUTO_INCREMENT `img_url` VARCHAR(300) NULL, `price` INT(20) NULL, `title` VARCHAR(200) NULL, `address` VARCHAR(100) CHARACTER SET `utf8` NULL, `city` VARCHAR(50) NULL, `region` VARCHAR(50) NULL, `area_size` INT(20) NULL, `rooms` INT(20) NULL, `urls` VARCHAR(300) NULL), ADD PRIMARY KEY (`id_house`, `id`), ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE;"
    query_execute(create_table_user)
    return 1

# insert the house on the database
def insert_house(house):
    insert_house_query = "INSERT INTO `meli_schema`.`mercadolibre_houses` (`img_url`, `price`, `title`, `address`, `city`, `region`, `area_size`, `rooms`, `urls`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    parameters = (house['img_url'], house['price'], house['title'], house['address'], house['city'], house['region'], house['area_size'], house['rooms'], house['urls'])
    query_execute(insert_house_query, parameters)
    return 1
