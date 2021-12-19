import unittest
from selenium import webdriver
from time import sleep #este modulo es para realizar las pausas y ver lo que sucede en el navegador

class NavigationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://google.com/')

    def test_browser_navigation(self):
        driver = self.driver

        #identificamos la barra de busqueda
        search_field = driver.find_element_by_name('q')
        #limpiamos
        search_field.clear()
        #enviamos el termino de busqueda
        search_field.send_keys('Platzi')
        #envio la busqueda
        search_field.submit()

        #retrocedo una pagina atras en el navegador
        driver.back()
        #pongo una pausa para ver lo que hace el navegafor
        sleep(3)
        #avanzo una pagina adelante
        driver.forward()
        #pongo una pausa para ver lo que hace el navegafor
        sleep(3)
        #refresco la ventana del navegador
        driver.refresh()
        #pongo una pausa para ver lo que hace el navegafor
        sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)