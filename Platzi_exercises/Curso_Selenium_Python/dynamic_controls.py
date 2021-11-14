import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class ExplicitWaitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Dynamic Controls').click()

    def test_clickable_checkbox(self):
        driver = self.driver
        remove_checkbox = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form[1]/button')
        remove_checkbox.click()

        add_checkbox = WebDriverWait(self.driver, 8).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/form[1]/button')))
        add_checkbox.click()

    def test_enable_bar(self):
        driver = self.driver
        enable_bar = WebDriverWait(self.driver, 8).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/form[2]/button')))
        enable_bar.click()

        bar = WebDriverWait(self.driver, 8).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/form[2]/input')))
        bar.click()
        bar.send_keys('Hecho')
        sleep(3)

        disable_bar = WebDriverWait(self.driver, 8).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/form[2]/button')))
        disable_bar.click()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()