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
import pyperclip
from selenium.webdriver.common.action_chains import ActionChains

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
time.sleep(2)

# escrever mensagem para Meu Numero
pyperclip.copy(message)
nav.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.CONTROL + "V")
time.sleep(5)
nav.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
time.sleep(3)

# encaminhar mensagem para a lista de contatos
element_list = nav.find_elements('class name', '_2AOIt')
for item in element_list:
    message = message.replace("\n", "")
    text1 = item.text.replace("\n","")
    if message in text1:
        element1 = item
        break

ActionChains(nav).move_to_element(element1).perform()
element1.find_element('class name', '_3u9t-').click()
time.sleep(1)
nav.find_element('xpath', '//*[@id="app"]/div/span[4]/div/ul/div/li[4]/div').click()
nav.find_element('xpath', '//*[@id="main"]/span[2]/div/button[4]/span').click()
time.sleep(1)

# escrever nome contato
nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys("Meu Numero")
time.sleep(1)
# apertar ENTER
nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
time.sleep(1)
# apagar nome contato
nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.BACKSPACE)
time.sleep(1)

contact_qtt = len(contact_list)
contact_qtt_num = 3

if contact_qtt % contact_qtt_num == 0:
    block_qtt = contact_qtt / contact_qtt_num
else:
    block_qtt = int(contact_qtt / 5) + 1
    
