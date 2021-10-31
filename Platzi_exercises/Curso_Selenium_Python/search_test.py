import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class HelloWorld(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    cls.driver = webdriver.Chrome(executable_path = './chromedriver' , options=options)
    driver = cls.driver
    url = 'http://demo-store.seleniumacademy.com/'
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(15) # segundos


  def test_search_text_fild(self):
    search_field = self.driver.find_element_by_id("search")


  def test_search_text_field_by_name(self):
    search_field = self.driver.find_element_by_name("q")


  def test_search_text_field_class_name(self):
    search_field = self.driver.find_element_by_class_name("input-text")


  def test_search_button_enabled(self):
    button = self.driver.find_element_by_class_name("button")


  def test_count_of_promo_banner_images(self):
    banner_list = self.driver.find_element_by_class_name("promos") #Buscamos la clase "promos"
    banners = banner_list.find_elements_by_tag_name("img") #Buscamos las etiquetas img dentro de promos
    self.assertEqual(3, len(banners)) #Hacemos una assertion para ver si efectivamente es la cantidad de imágenes que esperamos
    # NO son 3 imágenes, son 4, pero recordemos que se cuenta: [0,1,2,3]


  def test_vip_promo(self):
    vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')


  def test_shopping_cart(self):
    shopping_cart_icon = self.driver.find_element_by_css_selector("div.header-minicart span.icon")


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == '__main__':
  unittest.main(verbosity = 2)