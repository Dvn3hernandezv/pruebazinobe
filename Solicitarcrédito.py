from selenium import webdriver

# Crear un sesión de Chrome
driver = webdriver.Chrome(executable_path=r"C:\Users\Zinobe\PycharmProjects\pythonProject\chromedriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()

# Accerder a la aplicación web
driver.get("https://www.lineru.com/calcula-tu-credito")

# Se rechaza la ntoficación flotante
driver.find_element_by_id("wzrk-cancel").click()

# Seleccionar monto y fecha
driver.find_element_by_xpath('//*[@id="routify-app"]/div[1]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div/div/div').click()
driver.find_element_by_xpath('//*[@id="routify-app"]/div[1]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/div[3]/div[1]/div[4]/button').click()

# Perdir crédito
driver.find_element_by_xpath('//*[@id="routify-app"]/div[1]/div/div/div/div[2]/div[1]/div[3]/button').click()

# Se cierra el navegador
driver.quit()

