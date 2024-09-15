import pandas as pd
import pyautogui
import time


# Lee la primera columna de la pestaÃ±a 'pc' del archivo de Excel y almacena los datos en una lista llamada 'items'
def leer_primer_columna_excel():
    # Cargar la hoja 'pc' del archivo de Excel en un DataFrame de Pandas
    df = pd.read_excel('pclist.xlsx', sheet_name='pc')
    
    # Obtener la primera columna y almacenarla en una lista
    items = df.iloc[:, 0].tolist()

    return items


# Define la ruta que abrira el navegador
ruta = "https://jnj-ecm-prod.lightning.force.com/lightning/page/home"

# Configura la velocidad de movimiento y el tiempo de espera entre acciones
pyautogui.PAUSE = 1
pyautogui.MINIMUM_DURATION = 0.5

# Abre el navegador de internet
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# Espera a que se abra el navegador
time.sleep(5)

# Maximiza la ventana del navegador
pyautogui.hotkey('win', 'up')

# Recorre la lista de items
items = leer_primer_columna_excel()
for item in items:
    # Escribe la ruta en la barra de direcciones
    pyautogui.write(ruta)
    pyautogui.press('enter')
    time.sleep(5)

    # Escribe el item en el buscador
    pyautogui.click(x=800, y=100)
    pyautogui.write(str(item))  # Convierte el nÃºmero entero a cadena de texto
    pyautogui.press('enter')
    time.sleep(5)
    # Abre un nuevo tab
    pyautogui.hotkey('ctrl', 't')
    time.sleep(3)


