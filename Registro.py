from selenium import webdriver

# Crear un sesión de Chrome
driver = webdriver.Chrome(executable_path=r"C:\Users\Zinobe\PycharmProjects\pythonProject\chromedriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()

# Accerder a la aplicación web
driver.get("https://www.lineru.com/registro/")

# Se rechaza la ntoficación flotante
driver.find_element_by_id("wzrk-cancel").click()

# Se diligencian los datos del formulario
driver.find_element_by_xpath('//*[@id="routify-app"]/div[3]/div[3]/div/div/znb-input[1]').send_keys("Prueba1")
driver.find_element_by_xpath('//*[@id="routify-app"]/div[3]/div[3]/div/div/znb-select').click()
driver.save_screenshot('formulario.png')
driver.find_element_by_xpath('//*[@id="routify-app"]/div[3]/div[3]/div/div/znb-select').send_keys("Cédula de ciudadanía")
driver.find_element_by_xpath('//*[@id="routify-app"]/div[3]/div[3]/div/div/znb-input[2]').send_keys("9517534268")
driver.find_element_by_xpath('//*[@id="routify-app"]/div[3]/div[3]/div/div/znb-input[3]').send_keys("3049999999")
driver.find_element_by_xpath('//*[@id="routify-app"]/div[3]/div[3]/div/div/znb-input[4]').send_keys("pruebaQa1@gmail.com")
driver.find_element_by_xpath('//*[@id="routify-app"]/div[3]/div[3]/div/div/znb-password').click()
driver.find_element_by_xpath('//*[@id="routify-app"]/div[3]/div[3]/div/div/znb-password').send_keys("Contraseña123")
driver.find_element_by_xpath('//*[@id="routify-app"]/div[3]/div[3]/div/div/znb-checkbox[1]').click()
driver.find_element_by_xpath('//*[@id="routify-app"]/div[3]/div[3]/div/div/znb-checkbox[2]').click()

# Doy click en Crear mi cuenta
driver.find_element_by_xpath('//*[@id="routify-app"]/div[3]/div[3]/div/button').click()

# Se cierra el navegador
driver.quit()

