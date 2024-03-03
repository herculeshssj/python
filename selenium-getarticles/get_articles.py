from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    print('Busca automática de artigos')

    # Configura o WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Abre a página da web
    url = 'https://google.com/'  # Substitua pela URL desejada
    driver.get(url)

    # Sleep
    sleep(3)

    # Procura o texto
    #texto_desejado = 'Home'  # Substitua pelo texto desejado
    
    #try:
    #    driver.find_element_by_xpath(f"//*[contains(text(), '{texto_desejado}')]")
    #    print(f"'{texto_desejado}' foi encontrado na página.")
    #except:
    #    print(f"'{texto_desejado}' não foi encontrado na página.")

    driver.find_element(By.TAG_NAME, "body").click()


    #ActionChains(driver).send_keys(Keys.CONTROL, "f").perform()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('F').key_up(Keys.CONTROL).perform()

    #text_input = driver.find_element(By.TAG_NAME, 'textArea')
    #ActionChains(driver).send_keys_to_element(text_input, "abc").perform()

    sleep(3)


    sleep(3)

    # Fecha o navegador
    driver.quit()
