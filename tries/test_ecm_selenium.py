import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Función para leer la primera columna del archivo Excel y devolver una lista de items
def leer_primer_columna_excel():
    df = pd.read_excel('pclist.xlsx', sheet_name='pc')
    items = df.iloc[:, 0].tolist()
    return items

# Configuración del navegador Chrome
chrome_driver_path = 'chromedriver.exe'  # Asegúrate de que esta ruta sea correcta
options = Options()
options.add_argument('--start-maximized')  # Inicia el navegador maximizado
options.add_argument('--disable-infobars')  # Oculta la leyenda de control de automatización

# Iniciar el navegador Chrome
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

# Ruta que abrirá el navegador
ruta = "https://jnj-ecm-prod.lightning.force.com/lightning/page/home"

# Abrir la URL inicial
driver.get(ruta)

# Esperar a que la página se cargue completamente
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Leer los items desde el archivo Excel
items = leer_primer_columna_excel()

# Recorrer la lista de items y realizar acciones en la página
for item in items:
    driver.get(ruta)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input-202"))
    )
    search_box.clear()
    search_box.send_keys(str(item))
    search_box.send_keys(Keys.RETURN)
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "result-class-name"))  # Ajusta la clase del elemento que indica que los resultados se cargaron
    )

# Cerrar el navegador al finalizar
driver.quit()


