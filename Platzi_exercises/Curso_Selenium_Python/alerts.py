import unittest
from selenium import webdriver

class CompareProducts(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = './chromedriver')
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("http://demo-store.seleniumacademy.com/")
	
	def test_compare_products_removal_alert(self):
		driver = self.driver
		search_field = driver.find_element_by_name('q')
		#como buena práctica se recomienda limpiar los campos
		search_field.clear()


		search_field.send_keys('tee')
		search_field.submit()

		driver.find_element_by_class_name('link-compare').click()
		driver.find_element_by_link_text('Clear All').click()
		
		#creamos una variable para interactuar con el pop-up
		alert = driver.switch_to_alert()
		#vamos a extraer el texto que muestra
		alert_text = alert.text

		#vamos a verificar el texto de la alerta
		self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)
		
		alert.accept()

	def tearDown(self):
		self.driver.implicitly_wait(3)
		self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)