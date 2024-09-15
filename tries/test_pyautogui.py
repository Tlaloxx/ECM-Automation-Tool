import pandas as pd
import pyautogui
import time

# Minimize all windows
pyautogui.hotkey('win', 'd')
time.sleep(1)  # Esperar a que se minimicen las ventanas

# Open Chrome
pyautogui.hotkey('win', 'r')  # Abrir cuadro de diálogo 'Ejecutar'
time.sleep(0.5)
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)  # Esperar a que abra Chrome

# Maximize Chrome window
pyautogui.hotkey('win', 'up')  # Maximizar la ventana
time.sleep(1)

# Open the specific URL
url = "https://jnj-ecm-prod.lightning.force.com/lightning/page/home"
pyautogui.write(url)
pyautogui.press('enter')
time.sleep(5)  # Esperar a que cargue la página

# Locate the keyword 'Search'
# Nota: La localización puede necesitar ajustes, una alternativa es usar la función locateOnScreen con una imagen de la palabra "Search"
search_button_location = pyautogui.locateOnScreen('search.png')  # Necesitas una captura de pantalla del botón "Search"
if search_button_location:
    pyautogui.click(search_button_location)
    time.sleep(1)

    # Write 'Master' in the search box
    pyautogui.write('Master')
    pyautogui.press('enter')
    time.sleep(5)  # Esperar a que cargue la nueva página

else:
    print("No se encontró el botón 'Search' en la pantalla.")

print("Secuencia completada.")







