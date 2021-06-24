from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from selenium.webdriver.chrome.options import Options

opts=Options()
opts.add_argument(
    'USER_AGENT:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/80.0.3987.149 Safari/537.36'
)


driver = webdriver.Chrome('./chromedriver.exe', chrome_options=opts)
driver.get("https://listado.mercadolibre.com.pe/repuestos-autos-camionetas-bujias")

pagimax=10
pagmin=1

while pagmin<pagimax:
    lista_productos = driver.find_elements_by_xpath('//a[@class="ui-search-item__group__element ui-search-link"]')
    lista_url = []
    data=[]
    for tag_a in lista_productos:
        lista_url.append(tag_a.get_attribute("href"))

    for link in lista_url:
        try:
            driver.get(link)
            titulo=driver.find_element_by_xpath("//h1").text
            simbolo = driver.find_element_by_xpath("//span[@class='price-tag-symbol']").text
            precio=driver.find_element_by_xpath("//span[@class='price-tag-fraction']").text
            union= simbolo+". "+precio
            data.append({'Titulo':titulo,'Precio':union})
            #print(titulo)
            #print(union)
            driver.back()
        except Exception as e:
            print(e)
            driver.back()
    try:
        botonSiguiente= driver.find_element_by_xpath('//span[text()="Siguiente")]')
        botonSiguiente.click()
    except:
        break

    pagmin+=1

df=pd.DataFrame(data)
df.to_csv("MERCADOLIBRE.csv",index=True)
print(df)



