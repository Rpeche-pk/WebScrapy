from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
#almacenas el driver en una variabel
driver= webdriver.Chrome('./chromedriver.exe')

#utilizamos el driver
driver.get('https://www.olx.com.pe/autos_c378')

#ANTES DE RECORRER , VAMOS A DARLE CLICK EN EL BOTON CARGAR MAS, DAREMOS 3 VECES
#encontramos el boton
boton=driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')

for i in range(3):
    try:
        #espera por eventos
        #espera 10 hasta que el elemnto exista, cual elemento el boton
        #no pasara a la siguiente linea hasta que encuentre el elemento del xpath
        boton=WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//button[@data-aut-id="btnLoadMore"]'))
        )
        boton.click()
        #esperamos hasta que mis anuncios se encuentren llenos, osea las cajitas grises cuando carga informacion
        WebDriverWait(driver,10).until(
            #no va avanzar si los elemntos del xpath no existen
            EC.presence_of_all_elements_located((By.XPATH,'//li[@data-aut-id="itemBox"]//span[@data-aut-id="itemPrice"]'))
        )
    except:
        break

#instancia una variable donde guardare todos los items
#se almacena una lista
autos= driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')
data=[]
#recorreremos la lista
for auto in autos:
    precio= auto.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text
    descripcion = auto.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text

    data.append({'precio':precio,'descripcion':descripcion})

df=pd.DataFrame(data)

df.to_csv('olx.csv', index=True)
df=pd.read_csv('olx.csv')
print(df)
