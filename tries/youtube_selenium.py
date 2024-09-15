from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ruta al controlador de Chrome WebDriver
chrome_driver_path = 'chromedriver.exe'

# Configurar el servicio del controlador de Chrome
service = Service(chrome_driver_path)
service.start()

# Configurar las opciones del navegador Chrome
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')  # Inicia Chrome maximizado

# Iniciar el navegador Chrome
driver = webdriver.Chrome(service=service, options=options)

# Abrir YouTube
driver.get("https://www.youtube.com/")

# Esperar a que el campo de búsqueda esté presente y sea visible
search_box = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "search_query"))
)

# Limpiar el campo de búsqueda y escribir la consulta
search_box.clear()
search_box.send_keys("Bad bunny - por ti soy peor")
search_box.send_keys(Keys.RETURN)  # Presionar Enter para buscar

# Esperar a que el primer resultado esté presente y sea visible
first_result = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "video-title"))
)

# Hacer clic en el primer resultado
first_result.click()


 
 