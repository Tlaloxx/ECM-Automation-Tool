import pandas as pd
import pyautogui
import time

# Lee la primera columna de una hoja específica de un archivo Excel
def leer_primera_columna(ruta_excel, hoja):
    """
    Lee la primera columna de una hoja en un archivo Excel y la convierte en una lista.
    Filtra los valores vacíos.
    """
    df = pd.read_excel(ruta_excel, sheet_name=hoja)
    items = df.iloc[:, 0].dropna().tolist()  # Obtiene la primera columna y elimina filas vacías
    return items

# Configuración de PyAutoGUI para que las acciones no sean demasiado rápidas
pyautogui.PAUSE = 0.5  # Pausa automática entre comandos para dar tiempo a la máquina a reaccionar
pyautogui.MINIMUM_DURATION = 0.2  # Duración mínima de cualquier movimiento de PyAutoGUI

# Abre Chrome, maximiza la ventana, y navega a una URL dada
def abrir_chrome(url):
    """
    Abre el navegador Chrome, lo maximiza, y navega a la URL proporcionada.
    """
    pyautogui.hotkey('win', 'r')  # Abre el cuadro de diálogo 'Ejecutar'
    time.sleep(0.3)
    pyautogui.write('chrome')  # Escribe 'chrome' para abrir el navegador
    pyautogui.press('enter')  # Presiona Enter para ejecutar
    time.sleep(1.5)  # Espera a que Chrome se abra
    pyautogui.hotkey('win', 'up')  # Maximiza la ventana de Chrome
    time.sleep(0.5)
    pyautogui.write(url)  # Escribe la URL en la barra de direcciones
    pyautogui.press('enter')  # Presiona Enter para navegar a la URL
    time.sleep(5)  # Espera a que la página cargue

# Busca un elemento en la página y lo envía al campo de búsqueda
def buscar_elemento(item):
    """
    Busca el botón 'Search' en la página y escribe el elemento proporcionado en el campo de búsqueda.
    """
    buscar_boton = pyautogui.locateOnScreen('search.png')  # Busca la imagen del botón "Search"
    if buscar_boton:
        pyautogui.click(buscar_boton)  # Hace clic en el botón si se encuentra
        time.sleep(0.2)
        pyautogui.write(item)  # Escribe el texto del elemento
        pyautogui.press('enter')  # Presiona Enter para buscar
        time.sleep(3)  # Espera a que la página de resultados cargue
    else:
        print("Botón 'Search' no encontrado.")  # Muestra un mensaje si no se encuentra el botón

# Leer los elementos del archivo Excel
archivo_excel = 'pclist.xlsx'
hoja = 'Processing'
elementos = leer_primera_columna(archivo_excel, hoja)

# Minimiza todas las ventanas abiertas para despejar el área de trabajo
pyautogui.hotkey('win', 'd')
time.sleep(1)

# Abre Chrome, navega a la URL inicial, y busca el primer elemento
url = "https://jnj-ecm-prod.lightning.force.com/lightning/page/home"
abrir_chrome(url)
if elementos:
    buscar_elemento(elementos[0])  # Busca el primer elemento en la primera pestaña abierta

# Abre nuevas pestañas en Chrome para buscar los otros elementos
for item in elementos[1:]:
    pyautogui.hotkey('ctrl', 't')  # Abre una nueva pestaña
    time.sleep(1)
    pyautogui.write(url)  # Escribe la URL en la nueva pestaña
    pyautogui.press('enter')
    time.sleep(5)  # Espera a que la página cargue
    buscar_elemento(item)  # Busca el siguiente elemento en la nueva pestaña

print("Tarea completada.")  # Indica que la secuencia ha finalizado




