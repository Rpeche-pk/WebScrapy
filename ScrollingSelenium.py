from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import random


scrollingScript="""
    document.getElementsByClassName('section-layout section-scrollbox cYB2Ge-oHo7ed cYB2Ge-ti6hGc')[0].scroll(0,2000)
"""

opts=Options()
opts.add_argument(
    'USER_AGENT:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/80.0.3987.149 Safari/537.36'
)

driver= webdriver.Chrome('./chromedriver.exe', chrome_options=opts)
driver.get("https://www.google.com/maps/place/Restaurante+Amazonico/@40.4237431,-3.6873174,17z/data=!3m1!4b1!4m5!3m4!1s0xd422899dc90366b:0xce28a1dc0f39911d!8m2!3d40.4237336!4d-3.6851277")

sleep(random.uniform(4.0,5.0))

scroll=0

while (scroll != 3):
    driver.execute_script(scrollingScript)
    sleep(random.uniform(1,2))
    scroll+=1

reviews_restaurante= driver.find_elements(By.XPATH,'//div[@class="ODSEW-ShBeI NIyLF-haAclf gm2-body-2"]')

for review in reviews_restaurante:
    user_link=review.find_element_by_xpath(".//div[@class='ODSEW-ShBeI-tXxcle ODSEW-ShBeI-tXxcle-SfQLQb-menu']")

    try:
        user_link.click()
        #devuelve la pestaña 1 de las que tienes abiertas
        #switvh_to.windows es para decirle cambia de pestaña y le paso el argumento de que pestaña quiero estar
        driver.switch_to.window(driver.window_handles[2])
        boton_opniones= WebDriverWait(driver,10).until(
            EC.presence_of_element_located(By.XPATH,'//button[@class="s4ghve-AznF2e-ZMv3u-AznF2e NIyLF-haAclf s4ghve-AznF2e-ZMv3u-AznF2e-selected"]')
        )
        boton_opniones.click()

        WebDriverWait(driver,10).until(
            EC.presence_of_element_located(By.XPATH,'//div[@class="section-layout section-scrollbox cYB2Ge-oHo7ed cYB2Ge-ti6hGc"]')
        )

        USER_SCROLL=0
        while USER_SCROLL != 3:
            driver.execute_script(scrollingScript)
            sleep(random.uniform(5,6))
            USER_SCROLL+=1

        userReview= driver.find_elements(By.XPATH,'//div[contains(@class,"ODSEW-ShBeI NIyLF-haAclf"])')

        for user in userReview:
            texto=user.find_elements_by_xpath('.//span[@class="ODSEW-ShBeI-text"]').text
            raiting= user.find_elements_by_xpath('.//span[@class="ODSEW-ShBeI-H1e3jb"]').get_attribute('aria-label')

            print(texto)
            print(raiting)

        driver.close()
        driver.switch_to.window(driver.window_handles[1])

    except Exception as e:
        print(e)
        driver.close()
        driver.switch_to.window(driver.window_handles[1])
