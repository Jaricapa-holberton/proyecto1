import unittest
from selenium import webdriver
from time import sleep

class MercadoLibre(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://www.mercadolibre.com")

    def test_ps4_search(self):
        driver = self.driver
        articles = []
        prices = []
        driver.find_element_by_link_text('Colombia').click()

        search_field = driver.find_element_by_xpath('/html/body/header/div/form/input')
        search_field.send_keys('playstation 4')
        search_field.submit()

        driver.find_element_by_xpath('/html/body/main/div/div/aside/section[2]/dl[7]/dd[1]/a').click()

        driver.find_element_by_xpath('//*[@id="root-app"]/div/div/aside/section[3]/dl[7]/dd[1]/a').click()
        price = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/aside/section[2]/div[2]/div[1]/div/div/button').click()
        driver.find_element_by_xpath('//*[@id="root-app"]/div/div/aside/section[2]/div[2]/div[1]/div/div/div/ul/li[3]/div/div/a').click()

        for i in range(5):
            article_name = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[1]/a/h2').text
            articles.append(article_name)
            articles_price = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[2]/div/div/span[1]/span[2]').text
            prices.append(articles_price)
        print("")
        for i in range(5):
            print(articles[i] + " : " + prices[i])


    def tearDown(self):
        driver = self.driver
        sleep(5)
        driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)