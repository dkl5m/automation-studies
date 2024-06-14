from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

#acessar site https://www.novaliderinformatica.com.br/computadores
driver = webdriver.Chrome()
driver.get('https://www.novaliderinformatica.com.br/computadores')

#extrair todos os titulos e precos
titles = driver.find_elements(By.XPATH,"a[@class='nome-produto']")
prices = driver.find_elements(By.XPATH,"strong[@class='preco-promocional]")

#cria planilha
workbook = openpyxl.workbook()
#cria pagina 'produtos'
workbook.create_sheet('products')
#seleciona a pagina produtos
sheet_products = workbook['products']
#cria colunas product e price
sheet_products['A1'].value = 'Product'
sheet_products['B1'].value = 'Price'

#inserir todos os titulos e precos na planilha
for title, price in zip(titles, prices):
    sheet_products.append([title.text, price.text])
    
#salva planilha
workbook.save('products.xlsx')
