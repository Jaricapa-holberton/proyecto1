import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path= r'./chromedriver')
        driver = cls.driver
        driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_hello_world(self):
        driver = self.driver
        url = 'https://www.platzi.com'
        driver.get(url)

    def test_visit_wikipedia(self):
        driver = self.driver
        url = 'https://www.wikipedia.org'
        driver.get(url)

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output= 'reportes', report_name= 'hello_world_report'))
