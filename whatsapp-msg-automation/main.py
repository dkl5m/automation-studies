# Automacao de encaminhamento de mensagens no whatsapp
# Usando a funcionalidade nativa do whatsapp de encaminhar mensagem
# Encaminhar de 3 em 3
# install selenium pyperclip webdriver-manager

# pip install selenium pyperclip webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get("https://web.whatsapp.com")
time.sleep(2*60)

