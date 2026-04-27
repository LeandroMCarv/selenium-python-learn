from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

#configuracoes do navegador
configuracoes = Options()
configuracoes.add_argument("--disable-cookies")
configuracoes.add_argument("--disable-notifications")
configuracoes.add_argument("--disable-popup-blocking")
configuracoes.add_argument("--disable-blink-features=AutomationControlled")

#criacao do navegador
navegador = webdriver.Chrome(configuracoes)
navegador.get("https://www.youtube.com/")
navegador.maximize_window()

pesquisar = navegador.find_element("name","search_query")
pesquisar.send_keys("Como jogar bola")


#Forma 1 de clicar no botao (sem esperar)
# botao_pesquisa = navegador.find_element(
#     By.XPATH, "//button[contains(@aria-label, 'Search') or contains(@aria-label, 'Pesquisar')]"
# )
# botao_pesquisa.click()

#Forma 2 de clicar no botao (esperando ele ser clicavel)
botao_pesquisa = WebDriverWait(navegador,10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Search') or contains(@aria-label, 'Pesquisar')]"))
)
botao_pesquisa.click()

botao_login = WebDriverWait(navegador,10).until(
    EC.element_to_be_clickable((By.XPATH, '//a[@aria-label="Fazer login"]'))
)

#tempo necessario para o youtube carregar o botao de fazer login
time.sleep(2)

botao_login.click()

usuario = WebDriverWait(navegador,5).until(
    EC.element_to_be_clickable(("id","identifierId"))
)
usuario.send_keys("admin@gmail.com")

botao_avancar = WebDriverWait(navegador,5).until(
    EC.element_to_be_clickable((By.ID, "identifierNext"))
)
botao_avancar.click()

time.sleep(20)