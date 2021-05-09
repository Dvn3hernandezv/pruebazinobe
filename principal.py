from selenium import webdriver

# Crear un sesión de Chrome
driver = webdriver.Chrome(executable_path=r"C:\Users\Zinobe\PycharmProjects\pythonProject\chromedriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()

# Accerder a la aplicación web
driver.get("https://www.lineru.com/iniciar-sesion/")

# Se rechaza la ntoficación flotante
driver.find_element_by_id("wzrk-cancel").click()

# Se diligencia formulario de login
driver.find_element_by_xpath('//*[@id="routify-app"]/div[3]/div[3]/div/znb-input').send_keys("9517534268")
driver.find_element_by_xpath('//*[@id="routify-app"]/div[3]/div[3]/div/znb-password').click()
driver.find_element_by_xpath('//*[@id="routify-app"]/div[3]/div[3]/div/znb-password').send_keys("PruebaQA1")
driver.save_screenshot('login.png')
driver.find_element_by_xpath('//*[@id="routify-app"]/div[3]/div[3]/div/button').click()

# Se cierra el navegador
driver.quit()
