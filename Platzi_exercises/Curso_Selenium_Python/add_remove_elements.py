import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElements(unittest.TestCase):

	def setUp(self): #ejecutar todo lo necesario antes de hacer la prueba
		self.driver = webdriver.Chrome(executable_path = './chromedriver')
		driver = self.driver
		driver.implicitly_wait(10)
		driver.maximize_window()
		driver.get('http://the-internet.herokuapp.com/')
		driver.find_element_by_xpath('/html/body/div[2]/div/ul/li[2]/a').click()


	def test_browser_navigation(self):
		driver = self.driver
		elements_added = int(input('How many elements will you add? '))
		elements_removed = int(input('How many elements will you remove? '))
		total_elements_in_screen = elements_added - elements_removed

		add_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/button')

		if total_elements_in_screen > 0:

			for i in range(elements_added):
				add_button.click()

			for i in range(elements_removed):
				delete_button = driver.find_element_by_class_name('added-manually')
				delete_button.click()

			print('There are {} elements to show'.format(total_elements_in_screen))

		elif total_elements_in_screen == 0:
			print('There are not elements to show')

		else:
			print('you are trying to delete more items than you could add')


	def tearDown(self): #acciones para finalizar
		sleep(3)
		self.driver.implicitly_wait(3)
		self.driver.close()

if __name__ == '__main__':
	unittest.main(verbosity = 2)