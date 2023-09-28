pip install selenium
pip install pyperclip
pip install pyautogui

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
import pyautogui
import time
from selenium.webdriver.common.action_chains import ActionChains

# Configuração do navegador Chrome
navegador = webdriver.Chrome()
action = ActionChains(navegador)

# Abre a página inicial do Instagram
navegador.get("https://www.instagram.com/")
time.sleep(2)

# Preenche o campo de e-mail e senha
navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("seu email")
navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("sua senha")

# Pressiona a tecla Enter para fazer login
navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(Keys.ENTER)
time.sleep(60)  # Espera 45 segundos para entrar na publicação desejada

# Loop para realizar ações repetidas
for _ in range(3000):
        # Realiza ação de teclado
    action.send_keys('O', "k").key_down(Keys.ENTER).perform()
    # Espera 45 segundos ate o proximo comentario e o Instagram não te bloquear por Spam.
    time.sleep(45)