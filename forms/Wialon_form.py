# Preámbulos
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

#class WialonDatos:
#   def __init__(self):
placasWialon = ["JTV645", "LPN816", "LPN821"]

opcionesNavegador = webdriver.ChromeOptions()
lugarDescargasWialon = os.getcwd() + r"\outputWialon"
if not os.path.exists(lugarDescargasWialon):
    os.makedirs(lugarDescargasWialon)

opcionDescarga = {
    "download.default_directory": lugarDescargasWialon,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
}

opcionesNavegador.add_experimental_option("prefs", opcionDescarga)
driver = webdriver.Chrome(options= opcionesNavegador)
driver.set_window_size(1280, 720)


####################################
#### Entrada e inicio de sesión ####
####################################


# Entrada a página web de Wialon
driver.get("https://hosting.wialon.com/?lang=en")
WebDriverWait(driver,50).until(EC.presence_of_element_located((By.ID,"LoginInputControl")))


# Usuario
driver.find_element(By.ID,"LoginInputControl").send_keys("DEIMER")

# Contraseña
driver.find_element(By.CSS_SELECTOR,".PasswordInput").send_keys("Deimer*1")

# Botón ingreso
driver.find_element(By.ID,"monitoringLoginMainSubmitButton").click()


####################################
##### Selección Informe General ####
####################################



# Seleccionar template "INFORME DETALLADO POR UNIDAD".
WebDriverWait(driver,50).until(EC.presence_of_element_located((By.ID,"report_templates_filter_reports")))
time.sleep(2)
driver.find_element(By.ID,"report_templates_filter_reports").click()
time.sleep(1)
driver.find_element(By.ID,"report_templates_filter_reports").send_keys("INFORME GENERAL")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[13]/div/div/div[3]/div/div[1]/div[1]/div[2]/div/div/div[2]/div/ul/li").click()


####################################
####### Descargar por placa ########
####################################

for placa in placasWialon:
    # Seleccionar la placa.
    driver.find_element(By.ID,"report_templates_filter_units").click()
    time.sleep(1)
    driver.find_element(By.ID,"report_templates_filter_units").send_keys(placa)
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[13]/div/div/div[3]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div/ul/li").click()


    # Oprimir el botón execute.
    WebDriverWait(driver,50).until(EC.presence_of_element_located((By.ID,"report_templates_filter_params_execute")))
    driver.find_element(By.ID,"report_templates_filter_params_execute").click()


    # Oprimir botón Export.
    WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#report_result_export > div:nth-child(2)")))
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[14]/div[6]/div/div/div[1]/div[7]/div/span/div").click()

    # Descargar en Excel para el día seleccionado. ES POSIBLE QUE SE TENGA QUE CAMBIAR PARA LOS DÍAS QUE SE PIDAN.
    WebDriverWait(driver,50).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.dropdown-option:nth-child(1)")))
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,"div.dropdown-option:nth-child(1)").click()


####################################
####### Cierre del Webdriver #######
####################################


if len(os.listdir(lugarDescargasWialon)) >= 2:
    time.sleep(5)
    driver.quit()
else:
    time.sleep(5)