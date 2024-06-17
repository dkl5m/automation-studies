# Automacao de encaminhamento de mensagens no whatsapp
# Usando a funcionalidade nativa do whatsapp de encaminhar mensagem
# Encaminhar de 3 em 3
# install selenium pyperclip webdriver-manager

# pip install selenium pyperclip webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get("https://web.whatsapp.com")
time.sleep(2*60)

message = """Oi!
Estou testando um recurso no whatsapp web.
Entao, calma e nao bloqueia kk
"""

contact_list = ["Meu Numero", "Me, Myself and I", "Nós e eu", "EU, eu mesmo", "Grupo bom", "Gripe Mundial", "WTF is happening man"]

# Enviar a mensagem para o Meu Numero para depois poder encaminhar
# clicar na lupa
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/buttom/div[2]/span').click()
# escrever Meu Numero
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys("Meu Numero")
# dar enter
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
# escrever mensagem para Meu Numero
# encaminhar mensagem para a lista de contatos