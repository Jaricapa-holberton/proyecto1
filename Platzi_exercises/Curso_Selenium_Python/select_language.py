import unittest
from selenium import webdriver
#submodulo  para usar el dropdown
from selenium.webdriver.support.ui import Select

class LanguageOptions(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = './chromedriver')
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("http://demo-store.seleniumacademy.com/")

	def test_select_language(self):
		#el orden respeta como aparecen en la página
		exposed_options = ['English', 'French', 'German']
		#para almacenar las opciones que elijamos
		active_options = []
		#para acceder a las opciones del dropdown
		select_language = Select(self.driver.find_element_by_id('select-language'))
		#para comprobar que si esté la cantidad de  opciones correcta
		#'options' permite ingresar directamente a las opciones del dropdown
		self.assertEqual(3, len(select_language.options))

		for option in select_language.options:
			active_options.append(option.text)

		#verifico que la lista de opciones disponibles y activas sean indénticas
		self.assertListEqual(exposed_options,active_options)

		#vamos a verificar la palabra "English" sea la primera opción seleccionada del dropdown
		self.assertEqual('English', select_language.first_selected_option.text)

		#seleccionamos "German" por el texto visible
		select_language.select_by_visible_text('German')

		#verificamos que el sitio cambio a Alemán
		#preguntamos a selenium si la url del sitio contiene esas palabras
		self.assertTrue('store=german' in self.driver.current_url)

		select_language = Select(self.driver.find_element_by_id('select-language'))
		select_language.select_by_index(0)

	def tearDown(self):
		self.driver.implicitly_wait(3)
		self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)