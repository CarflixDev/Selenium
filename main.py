from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select  # Agrega esta línea
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
from selenium.common.exceptions import NoSuchElementException


# Inicializar el controlador de Chrome WebDriver antes del bucle
driver = Chrome()
driver.maximize_window()

# Abrir la página Remedy
driver.get('https://pauticgencat.onbmc.com/arsys/forms/onbmc-s/SHR%3ALandingConsole/Default+Administrator+View/?cacheid=148cf69d')

# Esperar a que el elemento de nombre de usuario esté presente en la página
wait = WebDriverWait(driver, 10)
elemento_usuario = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="user"]')))

# Insertar las credenciales en el formulario de inicio de sesión
elemento_usuario.send_keys('')
elemento_contraseña = driver.find_element(By.XPATH, '//*[@id="password"]')
elemento_contraseña.send_keys('')

# Presionar el botón de inicio de sesión
boton_inicio_sesion = driver.find_element(By.XPATH, '//*[@id="Login"]/div[3]/input')
boton_inicio_sesion.click()
time.sleep(3)

# Esperar a que el campo "Compañía" esté presente en la página
wait = WebDriverWait(driver, 20)
company = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="WIN_2_302845100"]/a/img')))
company.click()
#Esperar a que el campo desplegable
botondesplegable = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="arid_WIN_2_302845100"]')))
botondesplegable.send_keys('I')
botondesplegable.send_keys('I')
botondesplegable.send_keys(Keys.ENTER)
time.sleep(3)



# Esperar a que el campo "organization" esté presente en la página
wait = WebDriverWait(driver, 20)
organization = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="WIN_2_2000204034"]/a/img')))
organization.click()
# Esperar a que el elemento de la tabla esté presente en la página
desc_organization = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="arid_WIN_2_2000204034"]')))
desc_organization.send_keys(Keys.ARROW_DOWN)
desc_organization.send_keys('G')
desc_organization.send_keys('G')
desc_organization.send_keys('G')
desc_organization.send_keys('G')
desc_organization.send_keys('G')
desc_organization.send_keys('G')
desc_organization.send_keys('G')
desc_organization.send_keys(Keys.ENTER)
time.sleep(3)

# Esperar a que el camopo "Departament" Hospital de viladecans
wait = WebDriverWait(driver, 20)

departament = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="WIN_2_2000204035"]/a')))
departament.click()

# Esperar a que el elemento de la tabla esté presente en la página
desc_departament = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="arid_WIN_2_2000204035"]')))
desc_departament.send_keys(Keys.ARROW_DOWN)
desc_departament.send_keys('H')
desc_departament.send_keys('H')
desc_organization.send_keys(Keys.ENTER)
time.sleep(3)

# Vamos a la seccion Work order console
wait = WebDriverWait(driver, 20)
woconsolecompany = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="WIN_3_302845100"]/a')))
woconsolecompany.click()

# Esperar a que el elemento de la tabla WOCONSOLE ,campo Company esté presente en la página
desc_woconsolecompany = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="arid_WIN_3_302845100"]')))
woconsolecompany.send_keys('I')
woconsolecompany.send_keys('I')
woconsolecompany.send_keys(Keys.ENTER)
time.sleep(3)

# Esperar a que el elemento de la tabla WOCONSOLE ,campo organization esté presente en la página
wait = WebDriverWait(driver, 20)
woconsole_departament = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="WIN_3_2000204034"]/a')))
woconsole_departament.click()
# Esperar a que el elemento de la tabla esté presente en la página
desc_woconsole_organization = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="arid_WIN_3_2000204034"]')))
desc_woconsole_organization.send_keys(Keys.ARROW_DOWN)
desc_woconsole_organization.send_keys('G')
desc_woconsole_organization.send_keys('G')
desc_woconsole_organization.send_keys('G')
desc_woconsole_organization.send_keys('G')
desc_woconsole_organization.send_keys('G')
desc_woconsole_organization.send_keys('G')
desc_woconsole_organization.send_keys('G')
desc_woconsole_organization.send_keys(Keys.ENTER)
time.sleep(3)

# Esperar al elemento de la tabla WOCONSOLE , Departament
wait = WebDriverWait(driver, 20)
departament_woconsole = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="WIN_3_2000204035"]/a')))
departament_woconsole.click()

# Esperar a que el elemento de la tabla esté presente en la página
desc_departament_woconsole = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="arid_WIN_3_2000204035"]')))
desc_departament_woconsole.send_keys(Keys.ARROW_DOWN)
desc_departament_woconsole.send_keys('H')
desc_departament_woconsole.send_keys('H')
desc_departament_woconsole.send_keys(Keys.ENTER)
time.sleep(3)

# Esperar al elemento de la tabla OVERVIEW CONSOLE
wait = WebDriverWait(driver,20)
show = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="WIN_4_303174300"]/div/a')))
show.click()
# Esperar a el elemento que este presente en la tabla
desc_show = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="arid_WIN_4_303174300"]')))
desc_show.send_keys(Keys.ARROW_DOWN)
desc_show.send_keys(Keys.ARROW_DOWN)
desc_show.send_keys(Keys.ENTER)
time.sleep(3)



# Mantener el navegador abierto hasta que se cierre manualmente
while True:
    time.sleep(30)  # Esperar 30 segundos antes de verificar si el navegador sigue abierto.
