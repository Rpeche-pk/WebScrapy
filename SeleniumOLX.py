import random
from time import sleep
from selenium import webdriver

#almacenas el driver en una variabel
driver= webdriver.Chrome('./chromedriver.exe')

#utilizamos el driver
driver.get('https://www.olx.com.pe/autos_c378')
sleep(3)
driver.refresh() # Solucion de un bug extraño en Windows en donde los anuncios solo cargan al hacerle refresh o al darle click a algun elemento
sleep(5)
#ANTES DE RECORRER , VAMOS A DARLE CLICK EN EL BOTON CARGAR MAS, DAREMOS 3 VECES
#encontramos el boton
boton=driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')

for i in range(3):
    try:
        boton.click()
        sleep(random.uniform(8.0,10.0))
        boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
    except:
        break

#instancia una variable donde guardare todos los items
#se almacena una lista
autos= driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

#recorreremos la lista
for auto in autos:
    precio= auto.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text
    print(precio)
    descripcion = auto.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text
    print(descripcion)